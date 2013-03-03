import unittest
from Configuration import EdiDocumentConfiguration
from Settings import DefaultSettings

class TestEdiDocumentConfiguration(unittest.TestCase):
    def test_create_default_configuration(self):
        config = EdiDocumentConfiguration(DefaultSettings.version,
                                          DefaultSettings.element_separator,
                                          DefaultSettings.segment_terminator,
                                          DefaultSettings.sub_element_separator)
        self.assertEqual("00401", config.version)
        self.assertEqual("*", config.element_separator)
        self.assertEqual("~", config.segment_terminator)
        self.assertEqual(">", config.sub_element_separator)


if __name__ == '__main__':# pragma: no cover
    unittest.main()
