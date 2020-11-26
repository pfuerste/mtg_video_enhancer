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


def get_values(json_path: str, keys: list) -> dict:
    file = open(json_path, "r")
    j = json.load(file)
    cards = [card for card in j]
    keys_and_vals = dict.fromkeys(keys, list())
    for card in cards:
        for key in keys_and_vals.keys():
            if type(card[key]) is not dict:
                if card[key] not in keys_and_vals[key]:
                    keys_and_vals[key].append(card[key])
            else:
                keys_and_vals[key] = [[], []]
                for sub_key in card[key].keys():
                    if sub_key not in keys_and_vals[key][0]:
                        keys_and_vals[key][0].append(sub_key)
                    if card[key][sub_key] not in keys_and_vals[key][1]:
                        keys_and_vals[key][1].append(card[key][sub_key])
    return keys_and_vals


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
        if diff is not None:
            faulty_cards.append(i)
    return faulty_cards


def sort_by_keys():
    pass


def download_card_imgs():
    pass


if __name__ == "__main__":
    path = "/mnt/c/Users/phili/_Documents/Projects/mtg_video_enhancer/oracle-cards-20201122100602.json"
    keys = get_keys(path)
    vals = get_values(path, ["artist"])
    print(sorted(keys))
    print(vals)
