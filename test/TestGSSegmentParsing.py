import unittest
from EdiDocument import EdiDocument
from Group import GroupHeader
from EdiParser import Parser

class TestGSSegmentParsing(unittest.TestCase):

    def setUp(self):
        simpleFile = open('fixtures/General/Simple.edi', 'r')
        self.simpleEdiText = simpleFile.read()
        parser = Parser()
        self.simpleEdiDocument = parser.parse_document(document_text=self.simpleEdiText)
        simpleFile.close()

    def test_segment_type(self):
        """Test the segment type name from the class default."""
        self.assertEqual("GS", GroupHeader().id.name)

    def test_segment_size(self):
        """Test the segment type size from the class default"""
        self.assertEqual(8, GroupHeader().fieldCount)

    def test_functional_id_code(self):
        """Test the GS01 segment"""
        self.assertEqual("IN", self.simpleEdiDocument.interchange.groups[0].header.gs01.content)

    def test_application_sender_code(self):
        """Test the GS02 segment"""
        self.assertEqual("8005551234A", self.simpleEdiDocument.interchange.groups[0].header.gs02.content)

    def test_application_receiver_code(self):
        """Test the GS03 segment"""
        self.assertEqual("8005556789B", self.simpleEdiDocument.interchange.groups[0].header.gs03.content)

    def test_group_date(self):
        """Test the GS04 segment"""
        self.assertEqual("20130526", self.simpleEdiDocument.interchange.groups[0].header.gs04.content)

    def test_group_time(self):
        """Test the GS05 segment"""
        self.assertEqual("1410", self.simpleEdiDocument.interchange.groups[0].header.gs05.content)

    def test_group_control_number(self):
        """Test the GS06 segment"""
        self.assertEqual("4321", self.simpleEdiDocument.interchange.groups[0].header.gs06.content)

    def test_responsible_agency_code(self):
        """Test the GS07 segment"""
        self.assertEqual("X", self.simpleEdiDocument.interchange.groups[0].header.gs07.content)

    def test_version_indicator_code(self):
        """Test the GS08 segment"""
        self.assertEqual("004010", self.simpleEdiDocument.interchange.groups[0].header.gs08.content)