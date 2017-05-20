import pandas as pd
import resources
from base import CCS
from clinvoc.icd10 import ICD10CM, ICD10PCS

icd10cm_vocab = ICD10CM(use_decimals=False)
icd10pcs_vocab = ICD10PCS(use_decimals=False)
def get_icd10_codes(filename, level, code_type):
    vocab = icd10cm_vocab if code_type == 'dx' else icd10pcs_vocab
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
            code = vocab.standardize(code.strip('\''))
            code_set.add(code)
        
        result[category] = code_set
    
    return result
        
def get_single_level_codes(filename, code_type):
    codes = get_icd10_codes(filename, 'single', code_type)
    return codes
        
def get_multi_level_1(filename, code_type):
    codes = get_icd10_codes(filename, 'multi_1', code_type)
    return codes
     
def get_multi_level_2(filename, code_type):
    codes = get_icd10_codes(filename, 'multi_2', code_type)
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
        self.dx_single_level_codes = get_single_level_codes(dx_csv, code_type='dx')
        self.dx_level_1_codes = get_multi_level_1(dx_csv, code_type='dx')
        self.dx_level_2_codes = get_multi_level_2(dx_csv, code_type='dx')
        self.px_single_level_codes = get_single_level_codes(px_csv, code_type='px')
        self.px_level_1_codes = get_multi_level_1(px_csv, code_type='px')
        self.px_level_2_codes = get_multi_level_2(px_csv, code_type='px')


        
if __name__ == '__main__':
    pass
        
