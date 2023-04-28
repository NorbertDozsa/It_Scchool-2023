from New_deck import Card,Deck

d1= Deck()
d1_iter = iter(d1)

def septica(deck: Deck):
    for card in deck:
        if card.get_value() >= 7:
            yield card

septica_cards = septica(d1)

print(next(septica_cards))