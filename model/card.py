class Card:
    def __init__(
        self, name, color, type, cmc, supertype, subtype, attack, toughness, loyality
    ):
        self.name = name
        self.color = color
        self.type = type
        self.cmc = cmc
        self.supertype = supertype
        self.subtype = subtype
        self.attack = attack
        self.toughness = toughness
        self.loyality = loyality
