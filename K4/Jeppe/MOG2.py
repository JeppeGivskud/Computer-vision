import glob
import cv2
import numpy as np


def load_images():
    background_images = [
        cv2.imread(f, cv2.IMREAD_GRAYSCALE) for f in glob.glob("Assets/Test016/*.tif")
    ]
    return background_images


if __name__ == "__main__":
    background_images = load_images()
    bg_subtractor = cv2.createBackgroundSubtractorMOG2()

    for i in range(200):
        img = background_images[i]
        fg_mask = bg_subtractor.apply(img)
        # Display the output image
        cv2.imshow("Output", fg_mask)
        cv2.waitKey(0)
