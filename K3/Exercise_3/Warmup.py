import cv2 as cv
import numpy as np

input_image = cv.imread("Exercises\\Exercise_3\\aau-city-1.jpg")
output_image = input_image.copy()

############################################################
# Use cv2.cornerHarris to find corners and draw them with circles on output picture

# Your code here!
gray = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)


corner = cv.cornerHarris(gray, 2, 3, 0.04)
corner = cv.dilate(corner, None)

threshold = 0.5 * corner.max()

for y in range(corner.shape[0]):
    for x in range(corner.shape[1]):
        if corner[y, x] > threshold:
            output_image = cv.circle(output_image, (x, y), 10, (255, 0, 0))
############################################################

cv.imshow("output.png", output_image)
cv.waitKey(0)
