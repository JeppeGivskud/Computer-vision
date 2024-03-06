import glob
import cv2
import numpy as np

background_images = [
    cv2.imread(f, cv2.IMREAD_GRAYSCALE)
    for f in glob.glob("Assets/Warmup/BackgroundImages/*.tif")
]

test_image = cv2.imread("Assets/Warmup/test_image.png", cv2.IMREAD_GRAYSCALE)
output_image = test_image.copy()


def medianBackground(images):

    print("medianing")


medianBackground(background_images)
############################################################
# Return a mask for the people in test_image.png (see
# desired_output.png for an example)
# Compute the median of background_images and use the resulting
# image as a base for doing background subtraction on test_image.

# Your code here

############################################################

cv2.imwrite("output.png", output_image)
