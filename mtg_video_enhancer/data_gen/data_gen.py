import os
import numpy as np
import cv2 as cv


def get_random_imgs(img_dir: str, num: int) -> list:
    files = os.listdir(img_dir)
    files = np.random.choice(files, num, False)
    paths = [os.path.join(img_dir, file) for file in files]
    return paths


if __name__ == "__main__":
    print(get_random_imgs("/mnt/c/Users/phili/Documents/card_imgs/historic", 5))