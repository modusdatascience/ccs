import pandas as pd
from .resources import resources
from clinvoc.icd10 import ICD10CM, ICD10PCS
import os
from toolz.dicttoolz import merge
import re

icd10cm_vocab = ICD10CM(use_decimals=False)
icd10pcs_vocab = ICD10PCS(use_decimals=False)

def _get_icd10_codes(filename, code_type):
    assert code_type in ['dx', 'px']
    vocab = icd10cm_vocab if code_type == 'dx' else icd10pcs_vocab
    file_path = os.path.join(resources, filename)
    df = pd.read_csv(file_path)
    code_column = df.columns[0]
    
    result = {}
    for _, row in df.iterrows():
        key = (re.sub('\[[^\]]*\]', '', row[5]).strip(), re.sub('\[[^\]]*\]', '', row[7]).strip(), re.sub('\[[^\]]*\]', '', row[3]).strip(), vocab.vocab_domain, vocab.vocab_name)
        if key not in result:
            result[key] = set()
        result[key].add(vocab.standardize(row[code_column].strip('\'')))
    
    return result
        


code_sets_dict = merge(_get_icd10_codes('ccs_dx_icd10cm_2017.csv', 'dx'), _get_icd10_codes('ccs_pr_icd10pcs_2017.csv', 'px'))
 

