import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):

        self.transaction = Transaction("Holdiays", "Overlook Hotel", 1912)

    def test_transaction_has_tag(self):
        self.assertEqual("Holdiays", self.transaction.tag)

