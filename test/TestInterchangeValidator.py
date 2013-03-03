import unittest
from Fixtures import FixtureFiles


class TestISASegmentValidator(unittest.TestCase):
    def setUp(self):
        self.simple_edi_document = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)
        self.control_id_mismatch_edi_document = \
            FixtureFiles.documents.get(FixtureFiles.interchange_control_id_mismatch_error_file)

    def test_matching_interchange_control_ids(self):
        """Testing when ISA and IEA control IDs match"""
        report = self.simple_edi_document.validate()
        self.assertTrue(report.is_document_valid())

    def test_mismatching_interchange_control_ids(self):
        """Testing when ISA and IEA control IDs do not match"""
        report = self.control_id_mismatch_edi_document.validate()
        self.assertFalse(report.is_document_valid())

    def test_mismatch_interchange_control_id_validation_report(self):
        """Testing the validation report when ISA and IEA control IDS do not match"""
        report = self.control_id_mismatch_edi_document.validate()
        self.assertFalse(report.is_document_valid())
        self.assertEqual("The Interchange Control Number in ISA13 does not match Interchange Control Number in IEA02",
                         report.error_list[0].msg)


if __name__ == '__main__':# pragma: no cover
    unittest.main()





