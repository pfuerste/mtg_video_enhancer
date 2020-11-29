import os
import numpy as np
import cv2 as cv
from numpy.core.defchararray import endswith


def get_random_imgs(img_dir: str, num: int) -> list:
    files = [file for file in os.listdir(img_dir) if file.endswith(".jpg")]
    try:
        files = np.random.choice(files, num, False)
    except ValueError:
        pass
    paths = [os.path.join(img_dir, file) for file in files]
    return paths


if __name__ == "__main__":
    print(get_random_imgs("/mnt/c/Users/phili/Documents/card_imgs/historic", 999999999))