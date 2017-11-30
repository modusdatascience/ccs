# from clinvoc.icd9 import ICD9PCS, ICD9CM
from . import resources
import os
import re
from clinvoc.icd9 import ICD9CM, ICD9PCS
import pandas as pd
from toolz.dicttoolz import merge

# '''
# Single category parsing
# '''
icd9cm_vocab = ICD9CM(use_decimals=False)
icd9pcs_vocab = ICD9PCS(use_decimals=False)

def _get_icd9_codes(filename, code_type):
    assert code_type in ['dx', 'px']
    vocab = icd9cm_vocab if code_type == 'dx' else icd9pcs_vocab
    file_path = os.path.join(resources.resources, filename)
    df = pd.read_csv(file_path)
    code_column = df.columns[0]
    
    result = {}
    for _, row in df.iterrows():
        key = (re.sub('\[[^\]]*\]', '', row[2]).strip(), re.sub('\[[^\]]*\]', '', row[4]).strip(), re.sub('\[[^\]]*\]', '', row[6]).strip(), vocab.vocab_domain, vocab.vocab_name)
#         if not key[2]:
#             key = key[:2] + key[1:2] + key[3:]
        if key not in result:
            result[key] = set()
        result[key].add(vocab.standardize(row[code_column].strip('\'')))
    return result

dx_code_sets_dict = _get_icd9_codes('ccs_multi_dx_tool_2015.csv', 'dx')
px_code_sets_dict = _get_icd9_codes('ccs_multi_pr_tool_2015.csv', 'px')
code_sets_dict = merge(dx_code_sets_dict, px_code_sets_dict)
