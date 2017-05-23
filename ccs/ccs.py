from . import icd10
from . import icd9
from toolz.dicttoolz import merge
from clinvoc.code_collections import CodeCollection


code_sets = CodeCollection(*merge(icd10.code_sets_dict, icd9.code_sets_dict).items(), name='ccs')
