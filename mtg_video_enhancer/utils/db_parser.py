import json


def get_keys(json_path: str) -> list:
    file = open(json_path, "r")
    j = json.load(file)
    cards = [card.keys() for card in j]
    all_keys = list()
    for keys in cards:
        for key in keys:
            if key not in all_keys:
                all_keys.append(key)
    return all_keys


def get_faulty_keys(json_path: str) -> list:
    all_keys = set(get_keys(json_path))
    faulty_keys = list()
    file = open(json_path, "r")
    j = json.load(file)
    cards = [card.keys() for card in j]
    for i, card in enumerate(cards):
        diff = all_keys - set(card)
        for d in diff:
            if d not in faulty_keys:
                faulty_keys.append(d)
    return faulty_keys


# Seems all cards do not have all data.
def get_faulty_cards(json_path: str) -> list:
    all_keys = set(get_keys(json_path))
    faulty_cards = list()
    file = open(json_path, "r")
    j = json.load(file)
    cards = [card for card in j]
    for i, card in enumerate(cards):
        diff = all_keys - set(card.keys())
        print(diff)
        if diff is not None:
            faulty_cards.append(i)
    return faulty_cards


def sort_by_keys():
    pass


def download_card_imgs():
    pass


if __name__ == "__main__":
    keys = get_faulty_cards("/mnt/c/Users/phili/_Documents/Projects/mtg_video_enhancer/oracle-cards-20201122100602.json")
    print(keys)
