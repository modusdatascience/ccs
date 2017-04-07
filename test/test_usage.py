from ccs.icd9 import ICD9
from ccs.icd10 import ICD10
from clinvoc.icd9 import ICD9CM, ICD9PCS
from clinvoc.icd10 import ICD10CM, ICD10PCS

from nose.tools import assert_equals


def test_icd9():
    codesets = ICD9()
    dx_vocab = ICD9CM()
    px_vocab = ICD9PCS()
    
    for k, v in codesets.dx_single_level_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code)) 
    
    for k, v in codesets.px_single_level_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, px_vocab.standardize(code)) 
            
    for k, v in codesets.dx_category_level_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code))
                          
    for k, v in codesets.px_category_level_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, px_vocab.standardize(code))
                          
    for k, v in codesets.dx_multilevel_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code))
                          
    for k, v in codesets.px_multilevel_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, px_vocab.standardize(code))
    
def test_icd10():
    codesets = ICD10()
    dx_vocab = ICD10CM()
    px_vocab = ICD10PCS()

    for k, v in codesets.dx_level_1_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code))
            
    for k, v in codesets.px_level_1_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, px_vocab.standardize(code))
            
    for k, v in codesets.dx_level_2_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code))
            
    for k, v in codesets.px_level_2_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, px_vocab.standardize(code))
            
    for k, v in codesets.dx_single_level_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, dx_vocab.standardize(code))
            
    for k, v in codesets.px_single_level_codes.iteritems():
        assert isinstance(k, basestring)
        assert isinstance(v, set)
        for code in v:
            assert_equals(code, px_vocab.standardize(code))

if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])