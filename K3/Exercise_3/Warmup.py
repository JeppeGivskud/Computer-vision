import cv2 as cv
import numpy as np

input_image = cv.imread("Computer-vision\K3\Exercise_3\aau-city-1.jpg")
output_image = cv.imread("Computer-vision\K3\Exercise_3\aau-city-1.jpg")

############################################################
# Use cv2.cornerHarris to find corners and draw them with circles on output picture

# Your code here!
gray = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

corner = cv.cornerHarris(gray, 2, 3, 0.04)
corner = cv.dilate()

############################################################

cv.imwrite("output.png", output_image)
