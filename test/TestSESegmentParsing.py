import unittest
from Fixtures import FixtureReader, FixtureFiles

class TestSTSegmentParsing(unittest.TestCase):

    def setUp(self):
        self.multiple_transaction_edi_document = \
        FixtureReader().read_edi_file(FixtureFiles.single_group_multiple_transactions_file)

    def test_segment_type(self):
        """Test the segment type name from the class default."""
        self.assertEqual("SE", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[0].trailer.id.name)

    def test_transaction_one_number_of_included_segments(self):
        """Test the first transaction's id"""
        self.assertEqual("2", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[0].trailer.se01.content)

    def test_transaction_two_number_of_included_segments(self):
        """Test the first transaction's id"""
        self.assertEqual("2", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[1].trailer.se01.content)

    def test_transaction_three_number_of_included_segments(self):
        """Test the first transaction's id"""
        self.assertEqual("2", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[2].trailer.se01.content)

    def test_transaction_one_control_number(self):
        """Test the first transaction's id"""
        self.assertEqual("000000001", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[0].trailer.se02.content)

    def test_transaction_two_control_number(self):
        """Test the first transaction's id"""
        self.assertEqual("000000002", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[1].trailer.se02.content)

    def test_transaction_three_number(self):
        """Test the first transaction's id"""
        self.assertEqual("000000003", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[2].trailer.se02.content)

    def test_transaction_count(self):
        """Test that the parser captures the correct number of transactions"""
        self.assertEqual(3, len(self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets))
