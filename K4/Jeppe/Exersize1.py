import glob
import cv2
import numpy as np


def load_images():
    background_images = [
        cv2.imread(f, cv2.IMREAD_GRAYSCALE) for f in glob.glob("Assets/Test016/*.tif")
    ]

    test_image = cv2.imread("Assets/Warmup/test_image.png", cv2.IMREAD_GRAYSCALE)

    output_image = test_image.copy()

    return (
        background_images,
        test_image,
        output_image,
    )


def medianBackground(images):
    output_image = images.copy()
    output_image = np.median(output_image, axis=0).astype(np.uint8)
    print("medianing")
    return output_image


if __name__ == "__main__":
    background_images, test_image, output_image = load_images()
    background = test_image.copy()
    background = medianBackground(background_images)
    # output_image = cv2.subtract(test_image, background)

    i = 0
    while i < 100:
        test_image = background_images[i].copy()
        test_image = np.abs(test_image - background).astype(np.uint8)
        _, test_image = cv2.threshold(test_image, 50, 255, cv2.THRESH_BINARY)
        cv2.imshow("output", test_image)
        cv2.waitKey(0)

        i += 1
