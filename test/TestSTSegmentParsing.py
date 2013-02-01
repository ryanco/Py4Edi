import unittest
from EdiParser import Parser

class TestSTSegmentParsing(unittest.TestCase):

    def setUp(self):
        simpleFile = open('fixtures/General/MultipleTransactions.edi', 'r')
        self.simpleEdiText = simpleFile.read()
        parser = Parser()
        self.multiple_transaction_edi_document = parser.parse_document(document_text=self.simpleEdiText)
        simpleFile.close()

    def test_segment_type(self):
        """Test the segment type name from the class default."""
        self.assertEqual("ST", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[0].header.id.name)

    def test_transaction_one_id(self):
        """Test the first transaction's id"""
        self.assertEqual("000000001", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[0].header.st02.content)

    def test_transaction_two_id(self):
        """Test the first transaction's id"""
        self.assertEqual("000000002", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[1].header.st02.content)

    def test_transaction_three_id(self):
        """Test the first transaction's id"""
        self.assertEqual("000000003", self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets[2].header.st02.content)

    def test_transaction_count(self):
        """Test that the parser captures the correct number of transactions"""
        self.assertEqual(3, len(self.multiple_transaction_edi_document.interchange.groups[0].transaction_sets))
