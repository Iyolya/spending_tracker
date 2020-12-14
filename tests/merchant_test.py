import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):
    
    def setUp(self):

        self.merchant = Merchant("Overlook Hotel")
