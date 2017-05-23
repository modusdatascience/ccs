from clinvoc.icd9 import ICD9CM, ICD9PCS
from clinvoc.icd10 import ICD10CM, ICD10PCS
from nose.tools import assert_equals, assert_equal
from ccs.ccs import code_sets
import csv
from ccs.icd9 import icd9cm_vocab
from ccs.icd10 import icd10cm_vocab

def test_code_sets():
    test_set_icd9 = code_sets['Infectious and parasitic diseases', 'Bacterial infection', 'Tuberculosis', 'DX', 'ICD9CM']
    
    test_set_icd9_correct = set(map(icd9cm_vocab.standardize, ['01000', '01001', '01002', '01003', '01004',
                                                           '01005', '01006', '01010', '01011', '01012', '01013', '01014', '01015',
                                                           '01016', '01080', '01081', '01082', '01083', '01084', '01085', '01086',
                                                           '01090', '01091', '01092', '01093', '01094', '01095', '01096', '01100',
                                                           '01101', '01102', '01103', '01104', '01105', '01106', '01110', '01111',
                                                           '01112', '01113', '01114', '01115', '01116', '01120', '01121', '01122',
                                                           '01123', '01124', '01125', '01126', '01130', '01131', '01132', '01133',
                                                           '01134', '01135', '01136', '01140', '01141', '01142', '01143', '01144',
                                                           '01145', '01146', '01150', '01151', '01152', '01153', '01154', '01155',
                                                           '01156', '01160', '01161', '01162', '01163', '01164', '01165', '01166',
                                                           '01170', '01171', '01172', '01173', '01174', '01175', '01176', '01180',
                                                           '01181', '01182', '01183', '01184', '01185', '01186', '01190', '01191',
                                                           '01192', '01193', '01194', '01195', '01196', '01200', '01201', '01202',
                                                           '01203', '01204', '01205', '01206', '01210', '01211', '01212', '01213',
                                                           '01214', '01215', '01216', '01220', '01221', '01222', '01223', '01224',
                                                           '01225', '01226', '01230', '01231', '01232', '01233', '01234', '01235',
                                                           '01236', '01280', '01281', '01282', '01283', '01284', '01285', '01286',
                                                           '01300', '01301', '01302', '01303', '01304', '01305', '01306', '01310',
                                                           '01311', '01312', '01313', '01314', '01315', '01316', '01320', '01321',
                                                           '01322', '01323', '01324', '01325', '01326', '01330', '01331', '01332',
                                                           '01333', '01334', '01335', '01336', '01340', '01341', '01342', '01343',
                                                           '01344', '01345', '01346', '01350', '01351', '01352', '01353', '01354',
                                                           '01355', '01356', '01360', '01361', '01362', '01363', '01364', '01365',
                                                           '01366', '01380', '01381', '01382', '01383', '01384', '01385', '01386',
                                                           '01390', '01391', '01392', '01393', '01394', '01395', '01396', '01400',
                                                           '01401', '01402', '01403', '01404', '01405', '01406', '01480', '01481',
                                                           '01482', '01483', '01484', '01485', '01486', '01500', '01501', '01502',
                                                           '01503', '01504', '01505', '01506', '01510', '01511', '01512', '01513',
                                                           '01514', '01515', '01516', '01520', '01521', '01522', '01523', '01524',
                                                           '01525', '01526', '01550', '01551', '01552', '01553', '01554', '01555',
                                                           '01556', '01560', '01561', '01562', '01563', '01564', '01565', '01566',
                                                           '01570', '01571', '01572', '01573', '01574', '01575', '01576', '01580',
                                                           '01581', '01582', '01583', '01584', '01585', '01586', '01590', '01591',
                                                           '01592', '01593', '01594', '01595', '01596', '01600', '01601', '01602',
                                                           '01603', '01604', '01605', '01606', '01610', '01611', '01612', '01613',
                                                           '01614', '01615', '01616', '01620', '01621', '01622', '01623', '01624',
                                                           '01625', '01626', '01630', '01631', '01632', '01633', '01634', '01635',
                                                           '01636', '01640', '01641', '01642', '01643', '01644', '01645', '01646',
                                                           '01650', '01651', '01652', '01653', '01654', '01655', '01656', '01660',
                                                           '01661', '01662', '01663', '01664', '01665', '01666', '01670', '01671',
                                                           '01672', '01673', '01674', '01675', '01676', '01690', '01691', '01692',
                                                           '01693', '01694', '01695', '01696', '01700', '01701', '01702', '01703',
                                                           '01704', '01705', '01706', '01710', '01711', '01712', '01713', '01714',
                                                           '01715', '01716', '01720', '01721', '01722', '01723', '01724', '01725',
                                                           '01726', '01730', '01731', '01732', '01733', '01734', '01735', '01736',
                                                           '01740', '01741', '01742', '01743', '01744', '01745', '01746', '01750',
                                                           '01751', '01752', '01753', '01754', '01755', '01756', '01760', '01761',
                                                           '01762', '01763', '01764', '01765', '01766', '01770', '01771', '01772',
                                                           '01773', '01774', '01775', '01776', '01780', '01781', '01782', '01783',
                                                           '01784', '01785', '01786', '01790', '01791', '01792', '01793', '01794',
                                                           '01795', '01796', '01800', '01801', '01802', '01803', '01804', '01805',
                                                           '01806', '01880', '01881', '01882', '01883', '01884', '01885', '01886',
                                                           '01890', '01891', '01892', '01893', '01894', '01895', '01896', '1370 ',
                                                           '1371 ', '1372 ', '1373 ', '1374 ', 'V1201']))
    assert_equal(test_set_icd9, test_set_icd9_correct)
    
    test_set_icd10_correct = set(map(icd10cm_vocab.standardize, 
                                     ['A150', 'A154',
                                      'A155', 'A156', 'A157', 'A158', 'A159', 'A170', 'A171', 'A1781', 'A1782',
                                      'A1783', 'A1789', 'A179', 'A1801', 'A1802', 'A1803', 'A1809', 'A1810',
                                      'A1811', 'A1812', 'A1813', 'A1814', 'A1815', 'A1816', 'A1817', 'A1818',
                                      'A182', 'A1831', 'A1832', 'A1839', 'A184', 'A1850', 'A1851', 'A1852',
                                      'A1853', 'A1854', 'A1859', 'A186', 'A187', 'A1881', 'A1882', 'A1883',
                                      'A1884', 'A1885', 'A1889', 'A190', 'A191', 'A192', 'A198', 'A199', 'B900',
                                      'B901', 'B902', 'B908', 'B909', 'J65', 'Z8611']))
    
    test_set_icd10 = code_sets['Infectious and parasitic diseases', 'Bacterial infection', 'Tuberculosis', 'DX', 'ICD10CM']
    assert_equal(test_set_icd10, test_set_icd10_correct)
    
    
#     with open('testfile.csv', 'w') as outfile:
#         writer = csv.writer(outfile)
#         for k, v in code_sets.collectlevels().items():
#             for code in v:
#                 writer.writerow(k + (code,))
#     
#                 
#         
#     code_sets['Diseases of the circulatory system',]
    
#     print code_sets['Operations on the nervous system', 'Incision and excision of CNS [1.]', 'Incision and excision of CNS', 'DX', 'ICD9CM']

# 
# def test_icd9():
#     codesets = ICD9()
#     dx_vocab = ICD9CM()
#     px_vocab = ICD9PCS()
#      
#     for k, v in codesets.dx_single_level_codes.items():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, dx_vocab.standardize(code)) 
#      
#     for k, v in codesets.px_single_level_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, px_vocab.standardize(code)) 
#      
#     for k, v in codesets.dx_category_level_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, dx_vocab.standardize(code))
#      
#     for k, v in codesets.px_category_level_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, px_vocab.standardize(code))
#      
#     for k, v in codesets.dx_multilevel_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, dx_vocab.standardize(code))
#                
#     for k, v in codesets.px_multilevel_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, px_vocab.standardize(code))
#     
# def test_icd10():
#     codesets = ICD10()
#     dx_vocab = ICD10CM()
#     px_vocab = ICD10PCS()
# 
#     for k, v in codesets.dx_level_1_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, dx_vocab.standardize(code))
#             
#     for k, v in codesets.px_level_1_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, px_vocab.standardize(code))
#             
#     for k, v in codesets.dx_level_2_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, dx_vocab.standardize(code))
#             
#     for k, v in codesets.px_level_2_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, px_vocab.standardize(code))
#             
#     for k, v in codesets.dx_single_level_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, dx_vocab.standardize(code))
#             
#     for k, v in codesets.px_single_level_codes.iteritems():
#         assert isinstance(k, basestring)
#         assert isinstance(v, set)
#         for code in v:
#             assert_equals(code, px_vocab.standardize(code))

if __name__ == '__main__':
    import sys
    import nose
    # This code will run the test in this file.'
    module_name = sys.modules[__name__].__file__

    result = nose.run(argv=[sys.argv[0],
                            module_name,
                            '-s', '-v'])