import unittest
from Group import GroupTrailer
from Fixtures import FixtureFiles


class TestGESegmentParsing(unittest.TestCase):

    def setUp(self):
        self.simpleEdiDocument = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)

    def test_segment_type(self):
        """Test the segment type name from the class default."""
        self.assertEqual("GE", GroupTrailer().id.name)

    def test_segment_size(self):
        """Test the segment type size from the class default"""
        self.assertEqual(2, GroupTrailer().fieldCount)

    def test_number_of_included_groups(self):
        """Test the segment field from the instance"""
        self.assertEqual("0", self.simpleEdiDocument.interchange.groups[0].trailer.ge01.content)

    def test_interchange_control_number(self):
        """Test the segment field from the instance"""
        self.assertEqual("4321", self.simpleEdiDocument.interchange.groups[0].trailer.ge02.content)

if __name__ == '__main__':# pragma: no cover
    unittest.main()
