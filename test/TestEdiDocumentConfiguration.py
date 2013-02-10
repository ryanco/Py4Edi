import unittest
from Configuration import EdiDocumentConfiguration

class TestEdiDocumentConfiguration(unittest.TestCase):

    def test_create_default_configuration(self):
        config=EdiDocumentConfiguration(EdiDocumentConfiguration.version,
            EdiDocumentConfiguration.element_separator, EdiDocumentConfiguration.segment_terminator,
            EdiDocumentConfiguration.sub_element_separator)
        self.assertEqual("00401", config.version)
        self.assertEqual("*", config.element_separator)
        self.assertEqual("~", config.segment_terminator)
        self.assertEqual(">", config.sub_element_separator)

if __name__ == '__main__':
    unittest.main()
