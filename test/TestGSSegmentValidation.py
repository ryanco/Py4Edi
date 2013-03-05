import unittest
import copy
from Group import GroupHeader
from Reports import ValidationReport


class TestGSSegmentValidation(unittest.TestCase):

    def setUp(self):
        self.header = GroupHeader()
        #header
        self.header.gs01.content = "IN"
        self.header.gs02.content = "8005551234A"
        self.header.gs03.content = "8005556789B"
        self.header.gs04.content = "20121126"
        self.header.gs05.content = "1610"
        self.header.gs06.content = "8234"
        self.header.gs07.content = "X"
        self.header.gs08.content = "004010"

    def field_count_string(self, field="", length="", found=0, expected=0):
        """Utility method to build the return string"""
        return "Field " + field + " is too " + length + ". Found " + str(found) + " characters, expected " + str(
            expected) + " characters."

    def test_gs_01_validation_segment_too_short(self):
        """Test the gs01 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs01.content=""
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS01", "short", 0, 2), report.error_list[0].msg)
        self.assertEqual("GS01", report.error_list[0].segment.name)

    def test_gs_01_validation_segment_too_long(self):
        """Test the gs01 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs01.content="123"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS01", "long", 3, 2), report.error_list[0].msg)
        self.assertEqual("GS01", report.error_list[0].segment.name)

    def test_gs_02_validation_segment_too_short(self):
        """Test the gs02 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs02.content="1"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS02", "short", 1, 2), report.error_list[0].msg)
        self.assertEqual("GS02", report.error_list[0].segment.name)

    def test_gs_02_validation_segment_too_long(self):
        """Test the gs02 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs02.content="1234567890123456"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS02", "long", 16, 15), report.error_list[0].msg)
        self.assertEqual("GS02", report.error_list[0].segment.name)

    def test_gs_03_validation_segment_too_short(self):
        """Test the gs03 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs03.content="1"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS03", "short", 1, 2), report.error_list[0].msg)
        self.assertEqual("GS03", report.error_list[0].segment.name)

    def test_gs_03_validation_segment_too_long(self):
        """Test the gs03 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs03.content="1234567890123456"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS03", "long", 16, 15), report.error_list[0].msg)
        self.assertEqual("GS03", report.error_list[0].segment.name)

    def test_gs_04_validation_segment_too_short(self):
        """Test the gs04 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs04.content="1234567"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS04", "short", 7, 8), report.error_list[0].msg)
        self.assertEqual("GS04", report.error_list[0].segment.name)

    def test_gs_04_validation_segment_too_long(self):
        """Test the gs03 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs04.content="123456789"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS04", "long", 9, 8), report.error_list[0].msg)
        self.assertEqual("GS04", report.error_list[0].segment.name)

    def test_gs_05_validation_segment_too_short(self):
        """Test the gs05 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs05.content="123"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS05", "short", 3, 4), report.error_list[0].msg)
        self.assertEqual("GS05", report.error_list[0].segment.name)

    def test_gs_05_validation_segment_too_long(self):
        """Test the gs05 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs05.content="12345"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS05", "long", 5, 4), report.error_list[0].msg)
        self.assertEqual("GS05", report.error_list[0].segment.name)

    def test_gs_06_validation_segment_too_short(self):
        """Test the gs06 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs06.content=""
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS06", "short", 0, 1), report.error_list[0].msg)
        self.assertEqual("GS06", report.error_list[0].segment.name)

    def test_gs_06_validation_segment_too_long(self):
        """Test the gs06 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs06.content="1234567890"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS06", "long", 10, 9), report.error_list[0].msg)
        self.assertEqual("GS06", report.error_list[0].segment.name)

    def test_gs_07_validation_segment_too_short(self):
        """Test the gs07 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs07.content=""
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS07", "short", 0, 1), report.error_list[0].msg)
        self.assertEqual("GS07", report.error_list[0].segment.name)

    def test_gs_07_validation_segment_too_long(self):
        """Test the gs06 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs07.content="123"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS07", "long", 3, 2), report.error_list[0].msg)
        self.assertEqual("GS07", report.error_list[0].segment.name)


    def test_gs_08_validation_segment_too_short(self):
        """Test the gs08 segment is too short"""
        test_header = copy.copy(self.header)
        test_header.gs08.content=""
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS08", "short", 0, 1), report.error_list[0].msg)
        self.assertEqual("GS08", report.error_list[0].segment.name)

    def test_gs_08_validation_segment_too_long(self):
        """Test the gs06 segment is too long"""
        test_header = copy.copy(self.header)
        test_header.gs08.content="1234567890123"
        report = ValidationReport()
        test_header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(self.field_count_string("GS08", "long", 13, 12), report.error_list[0].msg)
        self.assertEqual("GS08", report.error_list[0].segment.name)


if __name__ == '__main__':
    unittest.main()
