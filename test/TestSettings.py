import unittest
from Settings import DefaultSettings, CurrentSettings


class TestSettings(unittest.TestCase):
    def test_default_settings(self):
        """Test the default settings"""
        self.assertEqual("*", DefaultSettings.element_separator)
        self.assertEqual("~", DefaultSettings.segment_terminator)
        self.assertEqual(">", DefaultSettings.sub_element_separator)
        self.assertEqual("00401", DefaultSettings.version)


    def test_current_settings(self):
        """Test the current settings are the defaults"""
        self.assertEqual(DefaultSettings.element_separator, CurrentSettings.element_separator)
        self.assertEqual(DefaultSettings.segment_terminator, CurrentSettings.segment_terminator)
        self.assertEqual(DefaultSettings.sub_element_separator, CurrentSettings.sub_element_separator)
        self.assertEqual(DefaultSettings.version, CurrentSettings.version)