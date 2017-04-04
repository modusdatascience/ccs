

def parse_dx_code(code):
    # correctly formats 
    if code == '': 
        print(code)
    elif len(code) < 4: 
        print(code)
        return code
    else:
        code = code[0:3] + '.' + code[3:]
        return code

def parse_px_code(code):
    if code < 3 or code == '': 
        print(code)
    else:
        code = code[0:2] + '.' + code[2:]
        if code == '.': 
            print('what')
        return code

def parse_icd10_code(code):
    # trim extra quotes 
    code = code[1:-1]
    # insert decimal correctly in string
    code = code[0:3] +'.' + code[3:]
    return code


class CCS():
    pass


