from typing import List
import random


CARD_SYMBOLS = ["♠", "♥", "♦", "♣"]
CARD_VALUE_MAP = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "A": 11,
    "J": 12,
    "Q": 13,
    "K": 14
}


class Card:

    def __init__(self, number: str, symbol: str) -> None:
        if number not in CARD_VALUE_MAP:
            raise ValueError("Invalid card number.")

        if symbol not in CARD_SYMBOLS:
            raise ValueError("Invalid card symbol.")

        self.__symbol = symbol
        self.__number = number

    def symbol(self)

    def __str__(self) -> str:
        # trebuie sa returneze string
        return f"<Card {self.__number}{self.__symbol}>"

    def __repr__(self) -> str:
        return self.__str__()

    def get_number(self) -> int:
        return CARD_VALUE_MAP[self.__number]

    def get_symbol(self) -> str:
        return self.__symbol

    def __eq__(self, other):
        # operator overloading
        # returneaza boolean
        # if self.number == other.number:
        #   return False
        return self.get_number() == other.get_number()

    def __lt__(self, other):
        return self.get_number() < other.get_number()

    def __le__(self, other):
        return self.get_number() <= other.get_number()

    def __gt__(self, other):
        return self.get_number() > other.get_number()

    def __ge__(self, other):
        return self.get_number() >= other.get_number()

    def __add__(self, other) -> int:
        return self.get_number() + other.get_number()
    
    # def __del__(self):
    #     """Destructor"""
    # print("Cartea a fost stearsa din memorie.")


class Deck:
    """
    When calling len() on this you will get the number of cards remained in deck.
    """

    def __init__(self) -> None:
        self.__cards = []
        for symbol in CARD_SYMBOLS:
            for number in CARD_VALUE_MAP:
                self.__cards.append(number, symbol)


    def __len__(self):
        # trebuie sa returneze int sau float
        return len(self.__cards)

    def get_cards(self, n) -> List[Card]:
        """Return n cards."""
        list1= []
        if n > len(self.__cards):
            raise ValueError("Not enough cards in deck")
        for i in range(n):
            list1.append(self.__cards.pop())
        return list1

    def shuffle(self):
        """Shuffles the deck"""
        return random.shuffle(self.__cards)
    

d1 = Deck()

# c1 = Card("2", CARD_SYMBOLS[0])
# c2 = Card("A", CARD_SYMBOLS[1])

# print(c1 == c2)
# # c1.__eq__(c2)


# print(f"Carti in pachet: {len(d1)}")

# print(d1.get_cards(10))

# print(f"Carti in pachet: {len(d1)}")

# print(d1.get_cards(2))
# d1.shuffle()
# print(d1.get_cards(2))