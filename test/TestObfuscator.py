import unittest
from EdiDocument import EdiDocument
from EdiParser import Parser
from Obfuscator import Obfuscator

class TestObfuscator(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        self.obfuscator = Obfuscator()
        simpleFile = open('fixtures/General/Simple.edi', 'r')
        self.simpleEdiText = simpleFile.read()
        self.simpleEdiDocument = self.parser.parse_document(document_text=self.simpleEdiText)
        self.obfuscated_doc = self.obfuscator.obfuscate(self.simpleEdiDocument)
        simpleFile.close()

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
