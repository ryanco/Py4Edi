import unittest
from FixtureReader import FixtureReader
from EdiValidator import Validator

class TestFixtureReader(unittest.TestCase):

    def test_read_simple_edi_file(self):
        document = FixtureReader().read_edi_document('fixtures/General/Simple.edi')
        self.assertTrue(Validator().is_valid_document(document))

    def test_file_not_found(self):
        self.assertRaises(IOError, FixtureReader().read_edi_document, "fixtures/General/NoFile.edi")