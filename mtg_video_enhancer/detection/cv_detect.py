""" Module to segment magic cards

This script can be execute or imported as a modul.
"""

import cv2 as cv
import numpy as np
import argparse


def load_image_with_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input", help="Path to input image.", default="../../images/cards.jpeg"
    )
    args = parser.parse_args()
    img = cv.imread(cv.samples.findFile(args.input))
    if img is None:
        print("Could not open or find the image:", args.input)
        exit(0)

    img_bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)

    return img_bgr


def load_image(url="../../images/cards.jpeg"):
    img = cv.imread(url)
    img_bgr = cv.cvtColor(img, cv.COLOR_RGB2BGR)

    return img_bgr


def watershed():

    return []


def fill(img):
    # https://www.learnopencv.com/filling-holes-in-an-image-using-opencv-python-c/
    kernel = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]], dtype=np.float32)
    imgLaplacian = cv.filter2D(img, cv.CV_32F, kernel)
    im_th = np.uint8(imgLaplacian)

    im_floodfill = im_th.copy()
    h, w = im_th.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv.floodFill(im_floodfill, mask, (0, 0), 255)
    im_floodfill_inv = cv.bitwise_not(im_floodfill)
    im_out = im_th | im_floodfill_inv

    return im_out


def contours_image(img):
    # https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
    # https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html

    ret, thresh = cv.threshold(img, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)

    return img


def canny_image(img):
    threshold = 30
    img = cv.Canny(img, threshold, threshold * 2)

    return img


def threshold_binary_inverse(img):
    # https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html

    blur = cv.GaussianBlur(img, (5, 5), 0)
    _, bw = cv.threshold(blur, 127, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    return bw


def threshold_binary(img):
    # blur = cv.GaussianBlur(img, (5, 5), 0)
    _, bw = cv.threshold(img, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    return bw


def white_balance(img_bgr):
    """Does white balance on a image

    input:
        img_bgr: image with bgr-color
    return:
        image in bgr-color
    """

    bgr = list(cv.split(img_bgr))
    avg = list(map(lambda x: cv.mean(x)[0], bgr))
    k = sum(avg) / 3
    k_bgr = list(map(lambda x: k / x, avg))
    bgr = list(
        map(
            lambda x, kx: cv.addWeighted(src1=x, alpha=kx, src2=0, beta=0, gamma=0),
            bgr,
            k_bgr,
        )
    )
    balance_img = cv.merge(bgr)

    return balance_img


def main():
    img = load_image(url="../../images/cards.jpeg")


if __name__ == "__main__":
    main()
