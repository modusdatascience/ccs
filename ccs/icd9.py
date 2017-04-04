# from clinvoc.icd9 import ICD9PCS, ICD9CM
import resources
import os
import re
from base import parse_dx_code, parse_px_code
from itertools import takewhile

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
        return ['header', category]
    
    elif re.match('Appendix', line) or re.match("Revised", line) or line == "\n":
        print(line)
        return ['junk']
    
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
        return ['code_set', code_set]
            
# change func name to better match icd10 
def read_single_txt_file(filename, code_type):
    
    result = {}
    with open(filename, 'rb') as infile:
        last_key = None
        for line in infile: 
            parse = parse_single_txt_line(line, code_type)
            if parse[0] == 'header': 
                result[parse[1]] = set()
                last_key = parse[1]
            elif parse[0] == 'code_set':
                codes = result[last_key]
                codes.update(parse[1])
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
        2 + 2
        
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
                result[parse['header']] = {'codes': set(), 'mapper': parse['mapper']} # need to pass it actual array
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

def get_single_level_codes(filename, code_type='dx'):
    level = 1
    data = read_multi_txt_file(filename, code_type)
    codes = get_codes_by_level(data, level)
    return codes

def get_multi_level_codes(filename, code_type='dx'):
    level = 2
    data = read_multi_txt_file(filename, code_type)
    codes = get_codes_by_level(data, level)
    return codes






test_dx = os.path.join(resources.resources, 'AppendixASingleDX.txt')
test_px = os.path.join(resources.resources, 'AppendixBSinglePR.txt')
# a = read_single_txt_file(test_dx, 'dx')
b = read_single_txt_file(test_px, 'px')
# print(len(a.keys()))
print(len(b.keys()))

test_multi_dx = os.path.join(resources.resources, 'AppendixCMultiDX.txt')
test_multi_px = os.path.join(resources.resources, 'AppendixDMultiPR.txt')
c = get_single_level_codes(test_multi_dx, 'dx')
d = get_multi_level_codes(test_multi_dx, 'dx')
e = get_single_level_codes(test_multi_px, 'px')
f = get_multi_level_codes(test_multi_px, 'px')

print(len(c.keys()))
print(len(d.keys()))
print(len(e.keys()))
print(len(f.keys()))





