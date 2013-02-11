import unittest
from EdiParser import Parser
from Obfuscator import Obfuscator
from Fixtures import FixtureFiles, FixtureReader

class TestObfuscator(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        self.obfuscator = Obfuscator()
        self.simpleEdiDocument = FixtureReader().read_edi_file(FixtureFiles.simple_edi_file)
        self.obfuscated_doc = self.obfuscator.obfuscate(self.simpleEdiDocument)

    def test_obfuscator_sender_ids(self):
        id_value = "8005551234AA   "
        self.assertEqual(id_value, self.obfuscated_doc.interchange.header.isa06.content)
        self.assertEqual(id_value, self.obfuscated_doc.interchange.groups[0].header.gs02.content)

    def test_obfuscator_receiver_ids(self):
        id_value = "8005555678BB   "
        self.assertEqual(id_value, self.obfuscated_doc.interchange.header.isa08.content)
        self.assertEqual(id_value, self.obfuscated_doc.interchange.groups[0].header.gs03.content)

    def test_obfuscator_control_ids(self):
        control_id = "123456789"
        self.assertEqual(control_id, self.obfuscated_doc.interchange.header.isa13.content)
        self.assertEqual(control_id, self.obfuscated_doc.interchange.trailer.iea02.content)
        self.assertEqual(control_id, self.obfuscated_doc.interchange.groups[0].header.gs06.content)
        self.assertEqual(control_id, self.obfuscated_doc.interchange.groups[0].trailer.ge02.content)

if __name__ == '__main__':# pragma: no cover
    unittest.main()
