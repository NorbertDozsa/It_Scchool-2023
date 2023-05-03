from unittest import TestCase
from src.lib.atm import ATM


class TestConstructor(TestCase):

    def test_attributes_values(self):

        atm = ATM()

        self.assertFalse(atm.__service_mode)
        self.assertEqual(atm.__retry_counter, 0)
        self.assertEqual(atm.__pin, "8464903")
        
    def test_fill(self):

        atm = ATM()

        self.assert