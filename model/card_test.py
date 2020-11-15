from card import Card

def test_constructor_sets_name():
    black_lotus = Card(name="Black Lotus")
    assert black_lotus.name == "Black Lotus"

