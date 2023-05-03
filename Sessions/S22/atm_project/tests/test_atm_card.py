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
        self.assertIsInstance(card.security_code, int)
        self.assertTrue(100 <= card.security_code < 1000) 

class TestGetBalance(TestCase):
    
    def test_values(self):
        card = Card("test", "0837")

        self.assertEqual(card.get_balance(), 0)
        self.assertIsInstance(card.get_balance(), int)

class TestAddMoney(TestCase):

    def test_values(self):
        card = Card("test", "0837")
        card.add_money(10)

        self.assertEqual(card.get_balance(), 10)

class TestCheckPin(TestCase):

    def test_values(self):
        card = Card("test", "0837")
        
        self.assertTrue(card.check_pin("0837"))

class TestWithdraw(TestCase):

    def test_values(self):
        card = Card("test", "0837")
        card.add_money(10)
        card.withdraw(10)

        self.assertEqual(card.get_balance(), 0)