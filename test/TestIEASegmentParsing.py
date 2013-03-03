import unittest
from EdiDocument import EdiDocument
from Fixtures import FixtureFiles


class TestIEASegmentParsing(unittest.TestCase):
    def setUp(self):
        self.simpleEdiDocument = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)
        self.interchange_group_count_error_document = \
            FixtureFiles.documents.get(FixtureFiles.interchange_included_group_count_error_file)

    def test_segment_type(self):
        """Test the segment type name from the class default."""
        self.assertEqual("IEA", EdiDocument().interchange.trailer.id.name)

    def test_segment_size(self):
        """Test the segment type size from the class default"""
        self.assertEqual(2, EdiDocument().interchange.trailer.fieldCount)

    def test_number_of_included_groups(self):
        """Test the segment field from the instance"""
        self.assertEqual("1", self.simpleEdiDocument.interchange.trailer.iea01.content)

    def test_interchange_control_number(self):
        """Test the segment field from the instance"""
        self.assertEqual("000001234", self.simpleEdiDocument.interchange.trailer.iea02.content)

    def test_validate_segment_size_is_not_valid(self):
        """Test the validation of the segment size is not valid"""
        self.assertFalse(self.interchange_group_count_error_document.validate().is_document_valid())


if __name__ == '__main__':# pragma: no cover
    unittest.main()