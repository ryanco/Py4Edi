import unittest
from Element import Element

class TestElement(unittest.TestCase):

    def test_empty_element_to_string(self):
        """Test rendering an optional empty element as a string"""
        element=Element(required=False)
        self.assertEqual("", str(element))

    def test_required_element_to_string(self):
        """Test rendering a required element as a string"""
        element=Element(required=True, content="TEST")
        self.assertEqual("TEST", str(element))

    def test_optional_element_to_string(self):
        """Test rendering an option element as a string"""
        element=Element(required=False, content="TEST")
        self.assertEqual("TEST", str(element))

    def test_is_valid_too_short(self):
        """Test an element that's content is too short"""
        element=Element(name="shorty", minLength=2, maxLength=4, content="1", required=True)
        self.assertFalse(element.validate()[0])
        self.assertEqual("Field shorty is too short. Found 1 characters, expected 2 characters.",
            element.validate()[1])

    def test_is_valid_too_long(self):
        """Test an element that's content is too long"""
        element=Element(name="longer", minLength=2, maxLength=4, content="12345", required=True)
        self.assertFalse(element.validate()[0])
        self.assertEqual("Field longer is too long. Found 5 characters, expected 4 characters.",
            element.validate()[1])

    def test_validate(self):
        """Test an element that's content is too long"""
        element=Element(name="just right", minLength=2, maxLength=4, content="123", required=True)
        self.assertTrue(element.validate()[0])

if __name__ == '__main__':# pragma: no cover
    unittest.main()