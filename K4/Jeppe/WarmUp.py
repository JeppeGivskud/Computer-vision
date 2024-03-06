import glob
import cv2
import numpy as np


def load_images():
    background_images = [
        cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        for f in glob.glob("Assets/Warmup/BackgroundImages/*.tif")
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
    output_image = cv2.subtract(test_image, background)

    # output_image = np.abs(test_image - background).astype(np.uint8)

    cv2.imshow("background", background)
    cv2.imshow("input", test_image)
    cv2.imshow("output", output_image)
    cv2.waitKey(0)
    ############################################################
    # Return a mask for the people in test_image.png (see
    # desired_output.png for an example)
    # Compute the median of background_images and use the resulting
    # image as a base for doing background subtraction on test_image.

    # Your code here

    ############################################################

    cv2.imwrite("Assets/Warmup/output.png", output_image)
