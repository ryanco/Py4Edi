import unittest
from EdiValidator import Validator
from EdiValidationErrors import IDMismatchError
from Fixtures import FixtureReader, FixtureFiles

class TestISASegmentValidator(unittest.TestCase):

    def setUp(self):
        self.simple_edi_document = FixtureReader().read_edi_file(FixtureFiles.simple_edi_file)
        self.control_id_mismatch_edi_document = \
        FixtureReader().read_edi_file(FixtureFiles.interchange_control_id_mismatch_error_document)

    def test_matching_interchange_control_ids(self):
        """Testing when ISA and IEA control IDs match"""
        self.assertTrue(Validator().is_valid_document(self.simple_edi_document))

    def test_mismatching_interchange_control_ids(self):
        """Testing when ISA and IEA control IDs do not match"""
        self.assertRaises(IDMismatchError, Validator().is_valid_document, self.control_id_mismatch_edi_document)

    def test_mismatch_interchange_control_id_validation_report(self):
        pass

if __name__ == '__main__':# pragma: no cover
    unittest.main()





