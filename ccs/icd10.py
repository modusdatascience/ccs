# from clinvoc.icd10 import ICD10PCS, ICD10CM

import pandas as pd
import resources
from base import parse_icd10_code


# 
# def read_csv_file(path, filename):
#     file_path = path + "/" + filename
#     df = pd.read_csv(file_path)

    # find all unique tags in 'CCS CATEGORY DESCRIPTION'
    # then iterate through those to create a set

def get_icd10_codes(filename, level=3): # default is most categories level
    
    file_path = resources.resources + "/" + filename
    df = pd.read_csv(file_path)
    #TODO: fix this mapper (values are wrong)
    level_mapper = {'1': df.columns[7], '2': df.columns[3], '3': df.columns[5]}

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
        
def get_lvl_1_codes(filename, ):
    # 18 categories
    codes = get_icd10_codes(filename, '1')
    return codes
        
def get_lvl_2_codes(filename):
    # 136 categories
    codes = get_icd10_codes(filename, '2')
    return codes
     

def get_lvl_3_codes(filename):
    codes = get_icd10_codes(filename, '3')
    return codes
   
a = get_lvl_3_codes('ccs_dx_icd10cm_2017.csv')
b = get_lvl_2_codes('ccs_dx_icd10cm_2017.csv')
c = get_lvl_1_codes('ccs_dx_icd10cm_2017.csv')

print(len(a.keys()))
print(len(b.keys()))
print(len(c.keys()))


