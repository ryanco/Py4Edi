import unittest
from Fixtures import FixtureReader
from EdiValidator import Validator
from ParserErrors import InvalidFileTypeError

class TestFixtureReader(unittest.TestCase):

    def test_read_simple_edi_file(self):
        document = FixtureReader().read_edi_file('fixtures/General/Simple.edi')
        self.assertTrue(Validator().is_valid_document(document))

    def test_file_not_found(self):
        self.assertRaises(IOError, FixtureReader().read_edi_file,
            "fixtures/General/NoFile.edi")

    def test_non_edi_file(self):
        self.assertRaises(InvalidFileTypeError, FixtureReader().read_edi_file,
            "fixtures/validation_errors/xml.edi")

if __name__ == '__main__':# pragma: no cover
    unittest.main()