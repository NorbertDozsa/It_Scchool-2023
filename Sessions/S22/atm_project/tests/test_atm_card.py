from unittest import TestCase
from src.lib.atm import Card
from datetime import datetime

class TestConstructor(TestCase):

    def test_attributes_values(self):
        """Test that the attributes are generated correctly."""
        card = Card("test", "0837")

        self.assertIsInstance(card.number, str)
        self.assertEqual(len(card.number), 8)
        self.assertIsInstance(card.expire_date, datetime)
        

        


class TestGetBalance(TestCase):
    