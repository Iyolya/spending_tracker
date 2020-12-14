import unittest
from models.tag import Tag

class TestTag(unittest.TestCase):

    def setUp(self):

        self.tag = Tag("Holidays")\

    def test_tag_has_name(self):
        self.assertEqual("Holidays", self.tag.name)