import unittest
import copy
from EdiParser import Parser
from Obfuscator import Obfuscator
from Fixtures import FixtureFiles


class TestObfuscator(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        self.obfuscator = Obfuscator()
        simple_doc = FixtureFiles.documents.get(FixtureFiles.simple_edi_file)
        #don't modify the shared document based on the simple_edi_file, create a copy to modify.
        self.simpleEdiDocument = copy.deepcopy(simple_doc)
        self.obfuscated_doc = self.obfuscator.obfuscate(self.simpleEdiDocument)


    def test_obfuscator_sender_ids(self):
        id_value = "OBFUSCATE34AA  "
        self.assertEqual(id_value, self.obfuscated_doc.interchange.header.isa06.content)
        self.assertEqual(id_value, self.obfuscated_doc.interchange.groups[0].header.gs02.content)

    def test_obfuscator_receiver_ids(self):
        id_value = "OBFUSCATE78BB  "
        self.assertEqual(id_value, self.obfuscated_doc.interchange.header.isa08.content)
        self.assertEqual(id_value, self.obfuscated_doc.interchange.groups[0].header.gs03.content)

    def test_obfuscator_control_ids(self):
        control_id = "OBF456789"
        self.assertEqual(control_id, self.obfuscated_doc.interchange.header.isa13.content)
        self.assertEqual(control_id, self.obfuscated_doc.interchange.trailer.iea02.content)
        self.assertEqual(control_id, self.obfuscated_doc.interchange.groups[0].header.gs06.content)
        self.assertEqual(control_id, self.obfuscated_doc.interchange.groups[0].trailer.ge02.content)

if __name__ == '__main__':# pragma: no cover
    unittest.main()
