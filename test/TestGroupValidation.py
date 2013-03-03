import unittest
from Fixtures import FixtureFiles
from Group import Group
from Reports import ValidationReport


class TestGroupValidation(unittest.TestCase):
    def setUp(self):
        self.simple_edi_document = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)
        self.transaction_count_error_edi_document = \
            FixtureFiles.documents.get(FixtureFiles.groups_included_transaction_count_error_file)

    def test_group_validate_is_valid(self):
        """Test the group being valid"""
        group = Group()
        group.header.gs06.content = "123456"
        group.trailer.ge01.content = "2"
        group.trailer.ge02.content = "123456"
        group.transaction_sets = ["1", "2"]
        report = ValidationReport()
        group.validate(report)
        self.assertTrue(report.is_document_valid())

    def test_group_control_id_mismatch(self):
        """Test the group control ids mismatching"""
        group = Group()
        group.header.gs06.content = "12345"
        group.trailer.ge01.content = "2"
        group.trailer.ge02.content = "123456"
        group.transaction_sets = ["1", "2"]
        report = ValidationReport()
        group.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual("The Group Control Number in GS06 does not match Group Control Number in GE02",
                         report.error_list[0].msg)

    def test_group_transaction_count_error(self):
        """Test the group transaction count error"""
        group = Group()
        group.header.gs06.content = "123456"
        group.trailer.ge01.content = "1"
        group.trailer.ge02.content = "123456"
        group.transaction_sets = ["1", "2"]
        report = ValidationReport()
        group.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual("The Number of Transaction Sets in GE01 value of 1 does not match the parsed count of 2",
                         report.error_list[0].msg)


if __name__ == '__main__':# pragma: no cover
    unittest.main()
