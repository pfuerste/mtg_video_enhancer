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


# TODO nicht nur auf ganzem Bild, auch kleinere
def add_reflection(card_img: np.array, refl_img: np.array):
    card_h, card_w = card_img.shape[:2]
    min_refl_size = 50
    upper_left = (
        np.random.randint(0, card_h - min_refl_size),
        np.random.randint(0, card_w - min_refl_size),
    )
    max_refl_size = np.subtract((card_h, card_w), upper_left)
    # resize need (w, h)
    refl_size = (
        np.random.randint(min_refl_size - 1, max_refl_size[1]),
        np.random.randint(min_refl_size - 1, max_refl_size[0]),
    )
    refl_img = cv.resize(src=refl_img, dsize=refl_size)

    h, w = refl_img.shape[:2]
    zeros = np.zeros(shape=card_img.shape, dtype=card_img.dtype)
    a = cv.getGaussianKernel(w, 50)
    b = cv.getGaussianKernel(h, 50)
    c = b * a.T
    d = c / c.max()
    zeros[
        upper_left[0] : upper_left[0] + h, upper_left[1] : upper_left[1] + w, 0
    ] = (refl_img[:, :, 0] * d)
    zeros[
        upper_left[0] : upper_left[0] + h, upper_left[1] : upper_left[1] + w, 1
    ] = (refl_img[:, :, 1] * d)
    zeros[
        upper_left[0] : upper_left[0] + h, upper_left[1] : upper_left[1] + w, 2
    ] = (refl_img[:, :, 2] * d)
   
    t = cv.add(card_img, zeros)
    cv.imwrite("vig2.jpg", t)
    return t


def create_img(bg_path: str, card_paths: list, annot_csv: str, out_dir: str):
    img = cv.imread(bg_path)
    refl_img = cv.imread(
        "/mnt/c/Users/phili/OneDrive/Bilder/Bewerbungsphoto.png"
    )
    h, w = img.shape[:2]

    for card in card_paths:
        # TODO: weiße Ecken abschneiden
        card_img = cv.imread(card)
        card_img = add_reflection(card_img, refl_img)

        mask = 255 * np.ones(card_img.shape, card_img.dtype)

        h_blend = int(card_img.shape[1] / 2)
        w_blend = int(card_img.shape[0] / 2)

        out_img = cv.seamlessClone(
            card_img, img, mask, (h_blend, w_blend), cv.NORMAL_CLONE
        )
    cv.imwrite(os.path.join(out_dir, "refl.jpg"), out_img)


if __name__ == "__main__":
    for i in range(100):
        bg_path = (
            "/mnt/c/Users/phili/OneDrive/Bilder/photo_2020-07-06_09-37-19.jpg"
        )
        card_paths = get_random_imgs(
            "/mnt/c/Users/phili/Documents/card_imgs/historic", 1
        )
        out_dir = "/mnt/c/Users/phili/_Documents/Projects/mtg_video_enhancer/synth_data"
        create_img(bg_path, card_paths, None, out_dir)
    # add_reflection([cv.imread(bg_path), cv.imread(card_paths[1])])
