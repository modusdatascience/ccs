import code


def parse_dx_code(code):
    # correctly formats 
    if code == '': 
        pass
    elif code and code[0]  == 'E':
        code = code[0:4] + '.' + code[4:]
        return code  
    elif len(code) < 4: 
        return code
    else:
        code = code[0:3] + '.' + code[3:]
        return code

def parse_px_code(code):
    if len(code) < 3 or code == '': 
        print(code)
    else:
        code = code[0:2] + '.' + code[2:]
        return code

def parse_icd10_code(code):
    # trim extra quotes 
    code = code[1:-1]
    if len(code) < 4: 
        return code
    else: 
    # insert decimal correctly in string
        code = code[0:3] +'.' + code[3:]
        return code


class CCS():
    pass


