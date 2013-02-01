import unittest
from EdiDocument import EdiDocument
from EdiParser import Parser

class TestISASegmentParsing(unittest.TestCase):

    def setUp(self):
        simpleFile = open('fixtures/General/Simple.edi', 'r')
        self.simpleEdiText = simpleFile.read()
        parser = Parser()
        self.simpleEdiDocument = parser.parse_document(document_text=self.simpleEdiText)
        simpleFile.close()

    def test_segment_type(self):
        """Test the segment type name from the class default."""
        self.assertEqual("ISA", EdiDocument().interchange.header.id.name)

    def test_segment_separator(self):
        """Test the segment type name from the class default."""
        self.assertEqual("*", EdiDocument().element_separator)

    def test_segment_size(self):
        """Test the segment type size from the class default"""
        self.assertEqual(16, EdiDocument().interchange.header.fieldCount)

    def test_authorization_information_qualifier(self):
        """Test the segment field from the instance"""
        self.assertEqual("00", self.simpleEdiDocument.interchange.header.isa01.content)

    def test_authorization_information(self):
        """Test the segment field from the instance"""
        self.assertEqual("          ", self.simpleEdiDocument.interchange.header.isa02.content)

    def test_security_information_qualifier(self):
        """Test the segment field from the instance"""
        self.assertEqual("00", self.simpleEdiDocument.interchange.header.isa03.content)

    def test_security_information(self):
        """Test the segment field from the instance"""
        self.assertEqual("          ", self.simpleEdiDocument.interchange.header.isa04.content)

    def test_interchange_id_qualifier_sender(self):
        """Test the segment field from the instance"""
        self.assertEqual("12", self.simpleEdiDocument.interchange.header.isa05.content)

    def test_interchange_sender_id(self):
        """Test the segment field from the instance"""
        self.assertEqual("8005551234AA   ", self.simpleEdiDocument.interchange.header.isa06.content)

    def test_interchange_id_qualifier_receiver(self):
        """Test the segment field from the instance"""
        self.assertEqual("12", self.simpleEdiDocument.interchange.header.isa07.content)

    def test_interchange_receiver_id(self):
        """Test the segment field from the instance"""
        self.assertEqual("8005556789BB   ", self.simpleEdiDocument.interchange.header.isa08.content)

    def test_interchange_date(self):
        """Test the segment field from the instance"""
        self.assertEqual("130526", self.simpleEdiDocument.interchange.header.isa09.content)

    def test_interchange_time(self):
        """Test the segment field from the instance"""
        self.assertEqual("1615", self.simpleEdiDocument.interchange.header.isa10.content)

    def test_interchange_control_standard_id(self):
        """Test the segment field from the instance"""
        self.assertEqual("U", self.simpleEdiDocument.interchange.header.isa11.content)

    def test_interchange_control_version_number(self):
        """Test the segment field from the instance"""
        self.assertEqual("00401", self.simpleEdiDocument.interchange.header.isa12.content)

    def test_interchange_control_number(self):
        """Test the segment field from the instance"""
        self.assertEqual("000001234", self.simpleEdiDocument.interchange.header.isa13.content)

    def test_acknowledgement_requested_flag(self):
        """Test the segment field from the instance"""
        self.assertEqual("0", self.simpleEdiDocument.interchange.header.isa14.content)

    def test_test_indicator_flag(self):
        """Test the segment field from the instance"""
        self.assertEqual("P", self.simpleEdiDocument.interchange.header.isa15.content)

    def test_sub_element_separator(self):
        """Test the segment field from the instance"""
        self.assertEqual(">", self.simpleEdiDocument.interchange.header.isa16.content)

    def test_segment_terminator(self):
        """Test the segment field from the instance"""
        self.assertEqual("~", self.simpleEdiDocument.segment_terminator)