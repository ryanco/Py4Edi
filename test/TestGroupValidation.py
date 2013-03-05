import unittest
import copy
from Fixtures import FixtureFiles
from Group import Group
from Reports import ValidationReport


class TestGroupValidation(unittest.TestCase):
    def setUp(self):
        self.simple_edi_document = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)
        self.transaction_count_error_edi_document = \
            FixtureFiles.documents.get(FixtureFiles.groups_included_transaction_count_error_file)
        self.group = Group()
        #header
        self.group.header.gs01.content = "IN"
        self.group.header.gs02.content = "8005551234A"
        self.group.header.gs03.content = "8005556789B"
        self.group.header.gs04.content = "20121126"
        self.group.header.gs05.content = "1610"
        self.group.header.gs06.content = "8234"
        self.group.header.gs07.content = "X"
        self.group.header.gs08.content = "004010"
        #trailer
        self.group.trailer.ge01.content = "0"
        self.group.trailer.ge02.content = "8234"


    def test_group_validate_is_valid(self):
        """Test the group being valid"""
        test_group = copy.copy(self.group)
        test_group.header.gs01.content ="00"
        test_group.header.gs06.content = "123456"
        test_group.trailer.ge01.content = "2"
        test_group.trailer.ge02.content = "123456"
        test_group.transaction_sets = ["1", "2"]
        report = ValidationReport()
        test_group.validate(report)
        self.assertTrue(report.is_document_valid())

    def test_group_control_id_mismatch(self):
        """Test the group control ids mismatching"""
        test_group = copy.copy(self.group)
        test_group.header.gs06.content = "12345"
        test_group.trailer.ge01.content = "2"
        test_group.trailer.ge02.content = "123456"
        test_group.transaction_sets = ["1", "2"]
        report = ValidationReport()
        test_group.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual("The Group Control Number in GS06 does not match Group Control Number in GE02",
                         report.error_list[0].msg)

    def test_group_transaction_count_error(self):
        """Test the group transaction count error"""
        test_group = copy.copy(self.group)
        test_group.header.gs06.content = "123456"
        test_group.trailer.ge01.content = "1"
        test_group.trailer.ge02.content = "123456"
        test_group.transaction_sets = ["1", "2"]
        report = ValidationReport()
        test_group.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual("The Number of Transaction Sets in GE01 value of 1 does not match the parsed count of 2",
                         report.error_list[0].msg)


if __name__ == '__main__':# pragma: no cover
    unittest.main()
