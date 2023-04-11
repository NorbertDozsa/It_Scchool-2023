from deck import Card, Deck

d1 = Deck()
d1.shuffle()
x_cards = d1.get_cards(2)

for i in x_cards:
    print(f"({i.get_number()}{i.get_symbol()}")