import unittest
import copy
from TransactionSet import TransactionSet
from Reports import ValidationReport


class TestTransactionSetValidation(unittest.TestCase):
    def setUp(self):
        self.transaction_set = TransactionSet()
        #header
        self.transaction_set.header.st01.content = "810"
        self.transaction_set.header.st02.content = "000000001"
        #body
        self.transaction_set.transaction_body = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #trailer
        self.transaction_set.trailer.se01.content = "10"
        self.transaction_set.trailer.se02.content = "000000001"


    def test_mismatch_control_id(self):
        transaction = copy.copy(self.transaction_set)
        transaction.header.st02.content = "000000004"
        report = ValidationReport()
        transaction.validate(report)
        self.assertFalse(report.is_document_valid())
        self.assertEqual("The Transaction Set Control Number in ST02 does not match Transaction Set Control Number in SE02",
                         report.error_list[0].msg)


if __name__ == '__main__':
    unittest.main()
