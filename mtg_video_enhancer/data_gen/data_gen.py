import os
import numpy as np
import cv2 as cv
# from numpy.core.defchararray import endswith


def get_random_imgs(img_dir: str, num: int) -> list:
    files = [file for file in os.listdir(img_dir) if file.endswith(".jpg")]
    try:
        files = np.random.choice(files, num, False)
    except ValueError:
        pass
    paths = [os.path.join(img_dir, file) for file in files]
    return paths


# def write_gt(, annot_csv: str):

def create_img(bg_path: np.array, card_path: list,
               annot_csv: str, out_dir: str):
    img = cv.imread(bg_path)
    h, w = img.shape[:2]

    for card in card_path:
        card_img = cv.imread(card)
        mask = 255*np.ones(card_img.shape, card_img.dtype)
        
        #h_blend = np.random.randint(0, h)
        #w_blend = np.random.randint(0, w)
        h_blend = int(card_img.shape[1]/2)
        w_blend = int(card_img.shape[0]/2)
        
        out_img = cv.seamlessClone(card_img, img, mask,
                              (h_blend, w_blend), cv.NORMAL_CLONE)
    cv.imwrite(os.path.join(out_dir, "1.jpg"), out_img)


if __name__ == "__main__":
    bg_path = "/mnt/c/Users/phili/OneDrive/Bilder/photo_2020-07-06_09-37-19.jpg"
    card_paths = get_random_imgs("/mnt/c/Users/phili/Documents/card_imgs/historic", 1)
    out_dir = "/mnt/c/Users/phili/_Documents/Projects/mtg_video_enhancer/synth_data"
    create_img(bg_path, card_paths, None, out_dir)