# from clinvoc.icd9 import ICD9PCS, ICD9CM
import resources
import os
import re
from base import parse_dx_code, parse_px_code, CCS

'''
Single category parsing
'''

def parse_single_txt_line(line, code_type):
    # looks for header
    if line[0].isdigit():
        split = re.split(r" *", line)
        split = split[1:]
        split[-1] = split[-1].rstrip()
        category = ''.join(['{} '.format(word) for word in split])
        return {'line_type': 'header', 'category': category.strip()} 
    # skips junk lines within file
    elif re.match('Appendix', line) or re.match("Revised", line) or line == "\n":
        return {'line_type': 'junk'}
    # looks for codes to associate with a header
    else: 
        split = re.split(r" *", line)
        split = split[1:]
        split[-1] = split[-1].rstrip()
        code_set = set()
        for code in split:
            if code_type == 'dx':
                clean_code = parse_dx_code(code)
            elif code_type == 'px':
                clean_code = parse_px_code(code)
            code_set.add(clean_code)
            if None in code_set: 
                code_set.remove(None)
        return {'line_type': 'code_set', 'code_set': code_set}
            
def read_single_txt_file(filename, code_type):
    
    result = {}
    with open(filename, 'rb') as infile:
        last_key = None
        for line in infile: 
            parse = parse_single_txt_line(line, code_type)
            if parse['line_type'] == 'header': 
                result[parse['category']] = set()
                last_key = parse['category']
            elif parse['line_type'] == 'code_set':
                codes = result[last_key]
                codes.update(parse['code_set'])
                result[last_key] = codes
                
    return result

'''
Multi-category parsing
'''

def parse_multi_txt_line(line, code_type='dx'):

    junk_patterns = ['Appendix', 'Revised', '\n', 'Multi-level']
    
    if line[0].isdigit():
        split = re.split(r" *", line)
        split[-1] = split[-1].rstrip()
        mapper = split.pop(0) 
        mapper = mapper.split('.')
        # refactor? 
        header = filter(lambda x: not x.isdigit(), split)
        header = filter(lambda x: x.find('['), header)
        header = filter(lambda x: x.find('-'), header)
        header = ' '.join(header)
        return {'line_type': 'header', 'header': header, 'mapper': mapper}
     
    elif any(x in line.rstrip() for x in junk_patterns) or line == '\n':
        pass
        
    else: 
        split = re.split(r" *", line)
        split = split[1:]
        split[-1] = split[-1].rstrip()
        code_set = set()
        for code in split:
            if code_type == 'dx':
                clean_code = parse_dx_code(code)
            elif code_type == 'px':
                clean_code = parse_px_code(code)
            code_set.add(clean_code)
            if None in code_set: 
                code_set.remove(None)
        return {'line_type': 'code_set', 'code_set': code_set}


def read_multi_txt_file(filename, code_type):
    result= {} 
    last_key = ''
    with open(filename, 'rb') as infile:
        last_key = None
        for line in infile: 
            parse = parse_multi_txt_line(line, code_type)
            if parse == None:
                pass
            elif parse['line_type'] == 'header':
                result[parse['header']] = {'codes': set(), 'mapper': parse['mapper']}
                last_key = parse['header']
            elif parse['line_type'] == 'code_set': 
                codes = result[last_key]['codes']
                codes.update(parse['code_set'])
                result[last_key]['codes'] = codes
    return result

def get_codes_by_level(codes, set_level):
    result = {} #maybe set
    for k,v in codes.iteritems(): 
        level = set_level
        try:
            group = []
            while level > 0: 
                group.append(v['mapper'][level-1])
                level -= 1
            group = '.'.join(group)

            if group in result.keys(): 
                result[group].update(v['codes'])
            else: 
                result[group] = set()
                result[group].update(v['codes'])
        except IndexError: 
            pass # some of the headers don't have more than one level
    return result
        
def get_category_level_codes(filename, code_type='dx'):
    codes = read_single_txt_file(filename, code_type)
    return codes 

def single_level_codes(filename, code_type='dx'):
    level = 1
    data = read_multi_txt_file(filename, code_type)
    codes = get_codes_by_level(data, level)
    return codes

def get_multi_level_codes(filename, code_type='dx'):
    level = 2
    data = read_multi_txt_file(filename, code_type)
    codes = get_codes_by_level(data, level)
    return codes


class ICD9(CCS):
    
    def __init__(self):
        dx_category_file = os.path.join(resources.resources, 'AppendixASingleDX.txt')
        px_category_file = os.path.join(resources.resources, 'AppendixBSinglePR.txt')
        dx_multilevel_file = os.path.join(resources.resources, 'AppendixCMultiDX.txt')
        px_multilevel_file = os.path.join(resources.resources, 'AppendixDMultiPR.txt')
        #
        self.dx_category_level_codes = get_category_level_codes(dx_category_file, 'dx')
        self.px_category_level_codes = get_category_level_codes(px_category_file, 'px')
        self.dx_single_level_codes = single_level_codes(dx_multilevel_file, 'dx')
        self.px_single_level_codes = single_level_codes(px_multilevel_file, 'px')
        self.dx_multilevel_codes = get_multi_level_codes(dx_multilevel_file, 'dx')
        self.px_multilevel_codes = get_multi_level_codes(dx_multilevel_file, 'px')


if __name__ == '__main__':
    pass
