import unittest
from EdiParser import Parser
from EdiValidator import Validator
from EdiValidationErrors import IDMismatchError
from EdiParserErrors import SegmentTerminatorNotFoundError

class TestISASegmentValidator(unittest.TestCase):

    def setUp(self):
        self.__create_simple_edi_document()
        self.__create_control_id_edi_mismatch_document()

    def test_matching_interchange_control_ids(self):
        """Testing when ISA and IEA control IDs match"""
        self.assertTrue(Validator().is_valid_document(self.simple_edi_document))

    def test_mismatching_interchange_control_ids(self):
        """Testing when ISA and IEA control IDs do not match"""
        self.assertRaises(IDMismatchError, Validator().is_valid_document, self.control_id_mismatch_edi_document)

    def test_mismatch_interchange_control_id_validation_report(selfs):
        pass

    def __create_simple_edi_document(self):
        simple_handle = open('fixtures/General/Simple.edi', 'r')
        simple_edi_text = simple_handle.read()
        self.simple_edi_document = Parser().parse_document(document_text=simple_edi_text)
        simple_handle.close()

    def __create_control_id_edi_mismatch_document(self):
        control_id_mismatch_handle = open('fixtures/validation_errors/InterchangeControlIDMismatch.edi', 'r')
        control_id_mismatch_edi_text = control_id_mismatch_handle.read()
        self.control_id_mismatch_edi_document = Parser().parse_document(document_text=control_id_mismatch_edi_text)
        control_id_mismatch_handle.close()



