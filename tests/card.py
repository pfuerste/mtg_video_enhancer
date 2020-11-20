# Brauchen wir diese Klasse? Hier bestimmt nicht.
class Card:
    def __init__(
        self, name, color, type, cmc, subtype, attack, toughness, loyality
    ):
        self.name = name
        self.color = color
        self.type = type
        self.cmc = cmc
        self.subtype = subtype
        self.attack = attack
        self.toughness = toughness
        self.loyality = loyality
