from card import Card


def test_constructor_sets_name():
    black_lotus = Card(
        name="Black Lotus",
        color="C",
        type="artifact",
        cmc=0,
        subtype=None,
        attack=None,
        toughness=None,
        loyality=None,
    )
    assert black_lotus.name == "Black Lotus"
    assert black_lotus.color == "C"
    assert black_lotus.type == "artifact"
    assert black_lotus.cmc == 0
    assert black_lotus.subtype == None
    assert black_lotus.attack == None
    assert black_lotus.toughness == None
    assert black_lotus.loyality == None
