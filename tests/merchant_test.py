import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):
    
    def setUp(self):

        self.merchant = Merchant("Overlook Hotel")

    def test_merchant_has_name(self):
        self.assertEqual("Overlook Hotel", self.merchant.name)
