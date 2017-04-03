# from clinvoc.icd10 import ICD10PCS, ICD10CM

import pandas as pd
import resources
from base import parse_icd10_code


def get_icd10_codes(filename, level=3): # default is most categories level
    
    file_path = resources.resources + "/" + filename
    df = pd.read_csv(file_path)

    '''
    maps single / multi-ccs values to where they are in the xls
    '''
    level_mapper = {'single': df.columns[3], 'multi_2': df.columns[7], 'multi_1': df.columns[5]}

    code_column = df.columns[0]
    categories = df[level_mapper[level]].unique()
    result = {}
    for category in categories:
        code_set = set()
        cat_codes = df.loc[df[level_mapper[level]] == category]
        raw_codes = list(cat_codes[code_column].get_values())
        for code in raw_codes:
            code = parse_icd10_code(code)
            code_set.add(code)
        
        result[category] = code_set
    
    return result
        
def get_single_level_codes(filename, ):
    # 18 categories
    codes = get_icd10_codes(filename, 'single')
    return codes
        
def get_multi_level_1(filename):
    # 136 categories
    codes = get_icd10_codes(filename, 'multi_1')
    return codes
     

def get_multi_level_2(filename):
    codes = get_icd10_codes(filename, 'multi_2')
    return codes
   
a = get_single_level_codes('ccs_dx_icd10cm_2017.csv') 
b = get_multi_level_2('ccs_dx_icd10cm_2017.csv')
c = get_multi_level_1('ccs_dx_icd10cm_2017.csv')


print(len(a.keys()))
print(len(b.keys()))
print(len(c.keys()))


