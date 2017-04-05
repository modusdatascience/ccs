from ccs.icd9 import ICD9
from clinvoc.icd9 import ICD9CM, ICD9PCS
from nose.tools import assert_equals


def test_icd9():
    codesets = ICD9()
    dx_vocab = ICD9CM()
    px_vocab = ICD9PCS()
    for k, v in codesets.dx_single_level_codes.items():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code)) 
    
    # TODO: Do these type and code formatting checks for all the other components
    



if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])