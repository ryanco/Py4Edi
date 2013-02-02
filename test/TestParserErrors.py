import unittest
from Segment import Segment
from ParserErrors import InvalidFileTypeError

class TestParserErrors(unittest.TestCase):

    def test_invalid_file_type_error(self):
        """Test a invalid file type error"""
        message = "Test Message"
        exception = InvalidFileTypeError(segment=Segment(), msg=message)
        self.assertEqual(message, str(exception))