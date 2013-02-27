import unittest
from EdiParser import Parser
from EdiValidator import Validator
from EdiValidationErrors import FieldValidationError
from ParserErrors import SegmentTerminatorNotFoundError
from Fixtures import FixtureFiles


class TestISASegmentValidator(unittest.TestCase):
    def setUp(self):
        self.parser = Parser()
        self.validator = Validator()
        self.simpleEdiDocument = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)

    def field_count_string(self, field="", length="", found=0, expected=0):
        """Utility method to build the return string"""
        return "Field " + field + " is too " + length + ". Found " + str(found) + " characters, expected " + str(
            expected) + " characters."

    def test_valid_file(self):
        """Test the positive case"""
        self.assertTrue(self.validator.is_valid_document(self.simpleEdiDocument))

    def test_isa_01_validation_segment_too_short(self):
        """Test the isa01 segment is too short"""
        testDocument = "ISA*0*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA01")
            self.assertEqual(error.msg, self.field_count_string("ISA01", "short", 1, 2))

    def test_isa_01_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        testDocument = "ISA*000*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA01")
            self.assertEqual(error.msg, self.field_count_string("ISA01", "long", 3, 2))

    def test_isa_02_validation_segment_too_short(self):
        """Test the isa01 segment is too short"""
        testDocument = "ISA*00*         *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA02")
            self.assertEqual(error.msg, self.field_count_string("ISA02", "short", 9, 10))

    def test_isa_02_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        testDocument = "ISA*00*           *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA02")
            self.assertEqual(error.msg, self.field_count_string("ISA02", "long", 11, 10))

    def test_isa_03_validation_segment_too_short(self):
        """Test the isa03 segment is too short"""
        testDocument = "ISA*00*          *0*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA03")
            self.assertEqual(error.msg, self.field_count_string("ISA03", "short", 1, 2))

    def test_isa_03_validation_segment_too_long(self):
        """Test the isa03 segment is too long"""
        testDocument = "ISA*00*          *000*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA03")
            self.assertEqual(error.msg, self.field_count_string("ISA03", "long", 3, 2))

    def test_isa_04_validation_segment_too_short(self):
        """Test the isa04 segment is too short"""
        testDocument = "ISA*00*          *00*         *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA04")
            self.assertEqual(error.msg, self.field_count_string("ISA04", "short", 9, 10))

    def test_isa_04_validation_segment_too_long(self):
        """Test the isa04 segment is too long"""
        testDocument = "ISA*00*          *00*           *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA04")
            self.assertEqual(error.msg, self.field_count_string("ISA04", "long", 11, 10))

    def test_isa_05_validation_segment_too_short(self):
        """Test the isa05 segment is too short"""
        testDocument = "ISA*00*          *00*          *1*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA05")
            self.assertEqual(error.msg, self.field_count_string("ISA05", "short", 1, 2))

    def test_isa_05_validation_segment_too_long(self):
        """Test the isa05 segment is too long"""
        testDocument = "ISA*00*          *00*          *120*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA05")
            self.assertEqual(error.msg, self.field_count_string("ISA05", "long", 3, 2))

    def test_isa_06_validation_segment_too_short(self):
        """Test the isa06 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*404347328     *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA06")
            self.assertEqual(error.msg, self.field_count_string("ISA06", "short", 14, 15))

    def test_isa_06_validation_segment_too_long(self):
        """Test the isa06 segment is too long"""
        testDocument = "ISA*00*          *00*          *12* 8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA06")
            self.assertEqual(error.msg, self.field_count_string("ISA06", "long", 16, 15))

    def test_isa_07_validation_segment_too_short(self):
        """Test the isa07 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *1*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA07")
            self.assertEqual(error.msg, self.field_count_string("ISA07", "short", 1, 2))

    def test_isa_07_validation_segment_too_long(self):
        """Test the isa07 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *120*8005555678BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA07")
            self.assertEqual(error.msg, self.field_count_string("ISA07", "long", 3, 2))

    def test_isa_08_validation_segment_too_short(self):
        """Test the isa08 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*800555567BB   *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA08")
            self.assertEqual(error.msg, self.field_count_string("ISA08", "short", 14, 15))

    def test_isa_08_validation_segment_too_long(self):
        """Test the isa08 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB    *131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA08")
            self.assertEqual(error.msg, self.field_count_string("ISA08", "long", 16, 15))

    def test_isa_09_validation_segment_too_short(self):
        """Test the isa09 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *21126*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA09")
            self.assertEqual(error.msg, self.field_count_string("ISA09", "short", 5, 6))

    def test_isa_09_validation_segment_too_long(self):
        """Test the isa09 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *0131022*1400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA09")
            self.assertEqual(error.msg, self.field_count_string("ISA09", "long", 7, 6))

    def test_isa_10_validation_segment_too_short(self):
        """Test the isa10 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*610*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA10")
            self.assertEqual(error.msg, self.field_count_string("ISA10", "short", 3, 4))

    def test_isa_10_validation_segment_too_long(self):
        """Test the isa10 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*01400*U*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA10")
            self.assertEqual(error.msg, self.field_count_string("ISA10", "long", 5, 4))

    def test_isa_11_validation_segment_too_short(self):
        """Test the isa11 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400**00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA11")
            self.assertEqual(error.msg, self.field_count_string("ISA11", "short", 0, 1))

    def test_isa_11_validation_segment_too_long(self):
        """Test the isa11 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U0*00401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA11")
            self.assertEqual(error.msg, self.field_count_string("ISA11", "long", 2, 1))

    def test_isa_12_validation_segment_too_short(self):
        """Test the isa12 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*0401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA12")
            self.assertEqual(error.msg, self.field_count_string("ISA12", "short", 4, 5))

    def test_isa_12_validation_segment_too_long(self):
        """Test the isa12 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*000401*000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA12")
            self.assertEqual(error.msg, self.field_count_string("ISA12", "long", 6, 5))

    def test_isa_13_validation_segment_too_short(self):
        """Test the isa13 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*00003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA13")
            self.assertEqual(error.msg, self.field_count_string("ISA13", "short", 8, 9))

    def test_isa_13_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*0000003821*0*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA13")
            self.assertEqual(error.msg, self.field_count_string("ISA13", "long", 10, 9))

    def test_isa_14_validation_segment_too_short(self):
        """Test the isa14 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821**P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA14")
            self.assertEqual(error.msg, self.field_count_string("ISA14", "short", 0, 1))

    def test_isa_14_validation_segment_too_long(self):
        """Test the isa01 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*00*P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA14")
            self.assertEqual(error.msg, self.field_count_string("ISA14", "long", 2, 1))


    def test_isa_15_validation_segment_too_short(self):
        """Test the isa15 segment is too short"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0**>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA15")
            self.assertEqual(error.msg, self.field_count_string("ISA15", "short", 0, 1))

    def test_isa_15_validation_segment_too_long(self):
        """Test the isa15 segment is too long"""
        testDocument = "ISA*00*          *00*          *12*8005551234AA   *12*8005555678BB   *131022*1400*U*00401*000003821*0*0P*>~"
        document = self.parser.parse_document(testDocument)
        self.assertRaises(FieldValidationError, self.validator.is_valid_document, document)
        try:
            self.validator.is_valid_document(document)
        except FieldValidationError as error:
            self.assertEqual(error.segment.name, "ISA15")
            self.assertEqual(error.msg, self.field_count_string("ISA15", "long", 2, 1))


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