from .card import Card
from mtg_video_enhancer.classification.metrics import Metrics


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

    # So ausführlich müssen solche Basics imo nicht getestet werden.
    assert black_lotus.name == "Black Lotus"
    assert black_lotus.color == "C"
    assert black_lotus.type == "artifact"
    assert black_lotus.cmc == 0
    assert black_lotus.subtype is None
    assert black_lotus.attack is None
    assert black_lotus.toughness is None
    assert black_lotus.loyality is None


def test_lower_imports():
    Metrics()
