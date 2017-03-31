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

def get_single_level_codes(filename):
    file_path = resources.resources + "/" + filename
    df = pd.read_csv(file_path)
    # getting around weird strings
    category_column = df.columns[3]
    code_column = df.columns[0]
    categories = df[category_column].unique()
    result = {}
    for category in categories:
        code_set = set()
        cat_codes = df.loc[df[category_column] == category]
        raw_codes = list(cat_codes[code_column].get_values())
        for code in raw_codes:
            code = parse_icd10_code(code)
            code_set.add(code)
        
        result[category] = code_set
        print(category)
    
    return result
        
        
        
        
    
   
   
get_single_level_codes('ccs_dx_icd10cm_2017.csv')


