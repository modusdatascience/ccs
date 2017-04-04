import pandas as pd
import resources
from base import parse_icd10_code, CCS


def get_icd10_codes(filename, level='single'):
    
    file_path = resources.resources + "/" + filename
    df = pd.read_csv(file_path)
    # maps single / multi-ccs values to where they are in the xls
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
        
def get_single_level_codes(filename):
    codes = get_icd10_codes(filename, 'single')
    return codes
        
def get_multi_level_1(filename):
    codes = get_icd10_codes(filename, 'multi_1')
    return codes
     
def get_multi_level_2(filename):
    codes = get_icd10_codes(filename, 'multi_2')
    return codes
  
  
 
class ICD10(CCS):
    '''
    Gives methods to access single, level 1, and level 2 categorizations for ICD10 codes (both dx and px). 
    - The ICD10 single level codes contain 'external cause codes', i.e. 2615 E Codes: Suffocation | These aren't currently being filtered. 
    '''
    
    def __init__(self):
        dx_csv = 'ccs_dx_icd10cm_2017.csv'
        px_csv = 'ccs_pr_icd10pcs_2017.csv'
        # 
        self.dx_single_level_codes = get_single_level_codes(dx_csv)
        self.dx_level_1_codes = get_multi_level_1(dx_csv)
        self.dx_level_2_codes = get_multi_level_2(dx_csv)
        self.px_single_level_codes = get_single_level_codes(px_csv)
        self.px_level_1_codes = get_multi_level_1(px_csv)
        self.px_level_2_codes = get_multi_level_2(px_csv)


        
if __name__ == '__main__':
    pass
        
