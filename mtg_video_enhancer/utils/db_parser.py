import os
import json
from tqdm import tqdm
import urllib.request


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


# Return all card names which are in a format
def filter_by_format(json_path: str, keys: list) -> list:
    file = open(json_path, "r")
    j = json.load(file)
    cards = [card for card in j]
    filtered_cards = list()
    for card in cards:
        for key in keys:
            if key in [
                "standard",
                "future",
                "historic",
                "pioneer",
                "modern",
                "legacy",
                "pauper",
                "vintage",
                "penny",
                "commander",
                "brawl",
                "duel",
                "oldschool",
            ]:
                if card["legalities"][key] == "legal":
                    # if card not in filtered_cards:
                    filtered_cards.append(card)
    return filtered_cards


# Have a dict with only the desired keys
def filter_keys(card_list: list, keys: list) -> list:
    filtered_cards = list()
    for card in card_list:
        new_card = dict()
        valid_vals = 0
        for key in keys:
            if type(key) is not str:
                try:
                    new_card[key[0]] = card[key[0]][key[1]]
                    valid_vals += 1
                except KeyError:
                    continue
            else:
                try:
                    new_card[key] = card[key]
                    valid_vals += 1
                except KeyError:
                    continue
        # nested continues...
        if valid_vals == len(keys):
            filtered_cards.append(new_card)
    return filtered_cards


def download_card_imgs(names_and_urls: list, img_dir: str):
    if not os.path.isdir(img_dir):
        os.makedirs(img_dir)
    print(f"Starting download of {len(names_and_urls)} images to {img_dir}.")
    for card in tqdm(names_and_urls):
        name = card["name"]
        if "/" in name:
            name = name.replace("/", "_")
        if "//" in name:
            name = name.replace("//", "_")
        path = os.path.join(img_dir, name) + ".jpg"
        url = card["image_uris"]
        if not os.path.isfile(path):
            urllib.request.urlretrieve(url, path)
    print("Finished.")


if __name__ == "__main__":
    path = "/mnt/c/Users/phili/_Documents/Projects/mtg_video_enhancer/oracle-cards-20201122100602.json"
    img_dir = "/mnt/c/Users/phili/Documents/card_imgs/historic"

    modern_cards = filter_by_format(path, ["historic"])
    modern_names_urls = filter_keys(modern_cards, ["name", ["image_uris", "normal"]])
    download_card_imgs(modern_names_urls, img_dir)
