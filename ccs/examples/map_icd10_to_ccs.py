'''
Generate random ICD 10 codes and print the set of all CCS categories for each one.
'''
from ccs.ccs import code_sets
from clinvoc.code_maps import CodeMap
from clinvoc.icd10 import ICD10CM

ccs_map = CodeMap.from_code_collection(code_sets)
icd10 = ICD10CM()
for _ in range(100):
    code = icd10.random()
    print('%s: %s' % (code, str(ccs_map['ICD10CM', code])))

