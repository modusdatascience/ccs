# from clinvoc.icd9 import ICD9PCS, ICD9CM
import resources
import os
import re

def parse_dx_code(code):
    ''' turns code into proper icd9dx object? see how this is done in clinvoc
    passes to dict
    '''
    if code == '': 
        print(code)
    else:
        return code

def parse_px_code(code):
    ''' turns code into proper icd9dx object? see how this is done in clinvoc
    passes to dict
    '''
    if code == '': 
        print(code)
    else:
        return code



def parse_txt_line(line, type):

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
            if type == 'dx':
                clean_code = parse_dx_code(code)
            elif type == 'px':
                clean_code = parse_px_code(code)
            code_set.add(clean_code)
            if None in code_set: 
                code_set.remove(None)
        return ['code_set', code_set]
            

def read_txt_file(filename, type):
    
    result = {}
    with open(filename, 'rb') as infile:
        last_key = None
        for line in infile: 
            parse = parse_txt_line(line, type)
            if parse[0] == 'header': 
                result[parse[1]] = set()
                last_key = parse[1]
            elif parse[0] == 'code_set':
                codes = result[last_key]
                codes.update(parse[1])
                result[last_key] = codes
                
    return result


test_dx = os.path.join(resources.resources, 'AppendixASingleDX.txt')
test_px = os.path.join(resources.resources, 'AppendixBSinglePR.txt')
a = read_txt_file(test_dx, 'dx')
b = read_txt_file(test_px, 'px')
print('whoop')






