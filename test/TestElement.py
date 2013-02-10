import unittest
from Element import Element

class TestElement(unittest.TestCase):

    def test_empty_element_to_string(self):
        """Test rendering an optional empty element as a string"""
        element=Element()
        element.required=False
        self.assertEqual("", str(element))

if __name__ == '__main__':
    unittest.main()
