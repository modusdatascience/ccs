from nose.tools import assert_equal # @UnresolvedImport
from ccs.icd9 import parse_single_txt_line, parse_multi_txt_line
from ccs.icd10 import get_icd10_codes




def test_icd9_dx():
    header_line = '1    Tuberculosis\n'
    code_line = '     1348 1349 135 1360 1361 1362 13621 13629 1364 1365 1368 1369 1398 V120 V1200 V1203 V1209 E9500 '
    header_test = parse_single_txt_line(header_line, 'dx')
    code_test = parse_single_txt_line(code_line, 'dx')
    assert_equal(header_test, {'line_type': 'header', 'category': 'Tuberculosis'})
    assert_equal(code_test, {'line_type': 'code_set', 'code_set': set(['134.8', '134.9', '135', '136.0', '136.1', '136.2', '136.21', '136.29', '136.4', '136.5', '136.8', '136.9', '139.8', 'V12.0', 'V12.00', 'V12.03', 'V12.09', 'E950.0'])})

def test_idc9_px():
    header_line = '1    Incision and excision of CNS\n'
    code_line = '     030 0101 0109 0121 0122 0123 0124 0125  \n'
    header_test = parse_single_txt_line(header_line, 'px')
    code_test = parse_single_txt_line(code_line, 'px')
    assert_equal(header_test, {'line_type': 'header', 'category': 'Incision and excision of CNS'})
    assert_equal(code_test, {'line_type': 'code_set', 'code_set': set(['03.0', '01.01', '01.09', '01.21', '01.22', '01.23', '01.24', '01.25'])})
    
def test_multi_txt_file():
    header_line = '1.1.1     Tuberculosis [1.]                                                                     -\n'
    header_test = parse_multi_txt_line(header_line)
    assert_equal(header_test, {'line_type': 'header', 'header': 'Tuberculosis', 'mapper': ['1','1','1']})

def test_icd10():
    test_file = 'icd10_test.csv'
    test_single = get_icd10_codes(test_file, 'single')
    test_multi_1 = get_icd10_codes(test_file, 'multi_1')
    test_multi_2 = get_icd10_codes(test_file, 'multi_2')
    assert_equal(test_single, {'Tuberculosis': set(['A15.0', 'A15.4', 'A15.5', 'A15.6', 'A15.7']), 'Delirium dementia and amnestic and other cognitive disorders': set(['G31.83', 'R41.81', 'R54']), 'Developmental disorders': set(['F70', 'F71'])})
    assert_equal(test_multi_1, {'Infectious and parasitic diseases': set(['A15.0', 'A15.4', 'A15.5', 'A15.6', 'A15.7']), 'Mental Illness': set(['G31.83', 'R41.81', 'R54', 'F70', 'F71'])})
    assert_equal(test_multi_2, {'Bacterial infection': set(['A15.0', 'A15.4', 'A15.5', 'A15.6', 'A15.7']), 'Delirium dementia and amnestic and other cognitive disorders [653]': set(['G31.83', 'R41.81', 'R54']), 'Developmental disorders [654]': set(['F70', 'F71'])})



if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])