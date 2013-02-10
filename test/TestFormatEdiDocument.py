import unittest
from EdiParser import Parser
from Fixtures import FixtureReader, FixtureFiles

class TestFormatEdiDocument(unittest.TestCase):

    def setUp(self):
        self.simple_edi_document = FixtureReader().read_edi_file(FixtureFiles.simple_edi_file)

    def test_isa_format_as_edi(self):
        good_isa_edi =\
        "ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>~"
        good_isa_document = Parser().parse_document(good_isa_edi)
        formatted_document = good_isa_document.format_as_edi()
        self.assertEqual(good_isa_edi, formatted_document)

    def test_isa_with_alternate_separators_format_as_edi(self):
        good_isa_edi =\
        "ISA|22|          |00|          |12|8005551234AA   |12|8005556789BB   |110408|1221|U|00401|000006617|0|P|>\n"
        good_isa_document = Parser().parse_document(good_isa_edi)
        formatted_document = good_isa_document.format_as_edi()
        self.assertEqual(good_isa_edi, formatted_document)

    def test_interchange_header_trailer_format_as_edi(self):
        interchange_edi=\
        "ISA*00*          *00*          *12*8005551234AA   *12*8005556789BB   *110408*1221*U*00401*000006617*0*P*>\nIEA*0*000006617\n"
        interchange_document = Parser().parse_document(interchange_edi)
        formatted_document = interchange_document.format_as_edi()
        self.assertEqual(interchange_edi, formatted_document)

    def test_simple_edi_document(self):
        simple_edi_document = FixtureReader().read_edi_file(FixtureFiles.simple_edi_file)
        formatted_document = simple_edi_document.format_as_edi()
        self.assertEqual(simple_edi_document.document_text, formatted_document)

    def test_multiple_groups_edi_document(self):
        multiple_edi_groups = FixtureReader().read_edi_file(FixtureFiles.multiple_groups_file)
        formatted_document = multiple_edi_groups.format_as_edi()
        self.assertEqual(multiple_edi_groups.document_text, formatted_document)

    def test_multiple_transactions_edi_document(self):
        multiple_transactions = FixtureReader().read_edi_file(FixtureFiles.single_group_multiple_transactions_file)
        formatted_document = multiple_transactions.format_as_edi()
        self.assertEqual(multiple_transactions.document_text, formatted_document)