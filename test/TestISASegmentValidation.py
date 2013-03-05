import unittest
import copy
from EdiParser import Parser
from Interchange import InterchangeHeader
from ParserErrors import SegmentTerminatorNotFoundError
from Fixtures import FixtureFiles
from Reports import ValidationReport


class TestISASegmentValidation(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.simpleEdiDocument = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)
        self.int_header=InterchangeHeader()
        self.int_header.isa01.content="00"
        self.int_header.isa02.content="          "
        self.int_header.isa03.content="00"
        self.int_header.isa04.content="          "
        self.int_header.isa05.content="12"
        self.int_header.isa06.content="8005551234AA   "
        self.int_header.isa07.content="12"
        self.int_header.isa08.content="8005555678BB   "
        self.int_header.isa09.content="131022"
        self.int_header.isa10.content="1400"
        self.int_header.isa11.content="U"
        self.int_header.isa12.content="00401"
        self.int_header.isa13.content="000003821"
        self.int_header.isa14.content="0"
        self.int_header.isa15.content="P"
        self.int_header.isa16.content=">"

    def field_count_string(self, field="", length="", found=0, expected=0):
        """Utility method to build the return string"""
        return "Field " + field + " is too " + length + ". Found " + str(found) + " characters, expected " + str(
            expected) + " characters."

    def test_valid_file(self):
        """Test the positive case"""
        report = self.simpleEdiDocument.validate()
        self.assertTrue(report.is_document_valid())

    def test_isa_01_validation_segment_too_short(self):
        """Test the isa01 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa01.content="0"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA01")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA01", "short", 1, 2))

    def test_isa_01_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa01.content="000"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA01")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA01", "long", 3, 2))

    def test_isa_02_validation_segment_too_short(self):
        """Test the isa01 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa02.content="         "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA02")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA02", "short", 9, 10))

    def test_isa_02_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa02.content="           "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA02")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA02", "long", 11, 10))

    def test_isa_03_validation_segment_too_short(self):
        """Test the isa03 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa03.content="0"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA03")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA03", "short", 1, 2))

    def test_isa_03_validation_segment_too_long(self):
        """Test the isa03 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa03.content="000"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA03")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA03", "long", 3, 2))

    def test_isa_04_validation_segment_too_short(self):
        """Test the isa04 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa04.content="         "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA04")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA04", "short", 9, 10))

    def test_isa_04_validation_segment_too_long(self):
        """Test the isa04 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa04.content="           "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA04")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA04", "long", 11, 10))

    def test_isa_05_validation_segment_too_short(self):
        """Test the isa05 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa05.content="1"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA05")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA05", "short", 1, 2))

    def test_isa_05_validation_segment_too_long(self):
        """Test the isa05 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa05.content="120"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA05")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA05", "long", 3, 2))

    def test_isa_06_validation_segment_too_short(self):
        """Test the isa06 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa06.content="8005551234AA  "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA06")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA06", "short", 14, 15))

    def test_isa_06_validation_segment_too_long(self):
        """Test the isa06 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa06.content=" 8005551234AA   "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA06")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA06", "long", 16, 15))

    def test_isa_07_validation_segment_too_short(self):
        """Test the isa07 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa07.content="1"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA07")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA07", "short", 1, 2))

    def test_isa_07_validation_segment_too_long(self):
        """Test the isa07 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa07.content="120"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA07")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA07", "long", 3, 2))

    def test_isa_08_validation_segment_too_short(self):
        """Test the isa08 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa08.content="8005555678BB  "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA08")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA08", "short", 14, 15))

    def test_isa_08_validation_segment_too_long(self):
        """Test the isa08 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa08.content="8005555678BB    "
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA08")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA08", "long", 16, 15))

    def test_isa_09_validation_segment_too_short(self):
        """Test the isa09 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa09.content="31022"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA09")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA09", "short", 5, 6))

    def test_isa_09_validation_segment_too_long(self):
        """Test the isa09 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa09.content="0131022"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA09")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA09", "long", 7, 6))

    def test_isa_10_validation_segment_too_short(self):
        """Test the isa10 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa10.content="400"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA10")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA10", "short", 3, 4))

    def test_isa_10_validation_segment_too_long(self):
        """Test the isa10 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa10.content="01400"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA10")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA10", "long", 5, 4))

    def test_isa_11_validation_segment_too_short(self):
        """Test the isa11 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa11.content=""
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA11")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA11", "short", 0, 1))

    def test_isa_11_validation_segment_too_long(self):
        """Test the isa11 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa11.content="U0"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA11")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA11", "long", 2, 1))


    def test_isa_12_validation_segment_too_short(self):
        """Test the isa12 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa12.content="0401"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA12")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA12", "short", 4, 5))

    def test_isa_12_validation_segment_too_long(self):
        """Test the isa12 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa12.content="000401"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA12")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA12", "long", 6, 5))

    def test_isa_13_validation_segment_too_short(self):
        """Test the isa13 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa13.content="00003821"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA13")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA13", "short", 8, 9))

    def test_isa_13_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa13.content="0000003821"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA13")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA13", "long", 10, 9))

    def test_isa_14_validation_segment_too_short(self):
        """Test the isa14 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa14.content=""
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA14")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA14", "short", 0, 1))

    def test_isa_14_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa14.content="12"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA14")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA14", "long", 2, 1))


    def test_isa_15_validation_segment_too_short(self):
        """Test the isa15 segment is too short"""
        header = copy.copy(self.int_header)
        header.isa15.content=""
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA15")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA15", "short", 0, 1))

    def test_isa_15_validation_segment_too_long(self):
        """Test the isa15 segment is too long"""
        header = copy.copy(self.int_header)
        header.isa15.content="0P"
        report = ValidationReport()
        header.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual(report.error_list[0].segment.name, "ISA15")
        self.assertEqual(report.error_list[0].msg, self.field_count_string("ISA15", "long", 2, 1))


    def test_isa_16_validation_segment_too_short(self):
        """Test the isa01 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*~"
        self.assertRaises(SegmentTerminatorNotFoundError, self.parser.parse_document, testDocument)


    def test_isa_16_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~0"
        document = self.parser.parse_document(testDocument)
        self.assertEqual(">", document.interchange.header.isa16.content)


if __name__ == '__main__':# pragma: no cover
    unittest.main()