import unittest
from models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):

        self.transaction = Transaction("Holdiays", "Overlook Hotel", 600)