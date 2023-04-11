import random


s1= "♠"
s2 = "♥"
s3 = "♦"
s4 = "♣"

from typing import List

CARD_SYMBOL = ["♠", "♥", "♦", "♣"]
CARD_VALUE_MAP = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "A" : 11,
    "J" : 12,
    "Q" : 13,
    "K" : 14
    
}

class Card:

    def __init__(self, number: str, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number")
        if symbol not in CARD_SYMBOL:
            raise ValueError("Invalid card symbol.")

        self.__symbol = symbol
        self.__number = number
    
    def __str__(self) -> str:
        return f"{self.__number}{self.__symbol}"
    
    def __repr__(self) -> str:
        return self.__str__()

    def get_number(self) -> int:
        return CARD_VALUE_MAP[self.__number]
    
    def get_symbol(self) -> str:
        return self.__symbol

    def __eq__(self, other):
        # if self.number == other.number:
        #     if self.symbol == other.symbol:
        #         return True
        # else:
        #     return False
        return self.get_number() == other.get_number() 
    # and self.__symbol == other.get_symbol()
    
     #  __lt__ <
    # __le__ <=
    # __gt__ >
    # __ge__ >=
    def __lt__(self, other):
        return self.get_number() < other.get_number()
    
    def __le__(self, other):
        return self.get_number() <= other.get_number()
    
    def __gt__(self, other):
        return self.get_number > other.get_number()
    
    def __ge__(self, other):
        return self.get_number() >= other.get_number()
    
    def __add__(self, other) -> int:
        return self.get_number() + other.get_number()


class Deck:
    """
    When calling len() on this you will get the number of cards remained in deck.
    """
    def __init__(self,) -> None:
        self.__cards = []

    def __len__(self):
        return len(self.__cards)
    
    def get_cards(self, n):






c1 = Card("2", CARD_SYMBOL[0])
c2 = Card("A", CARD_SYMBOL[1])

print(c1 == c2)
print(c1 != c2)
print(c1 < c2)
print(c1 <= c2)
print(c1 >= c2)
print(c1 > c2)
print(c1 + c2)


c1.get_symbol()
