import cv2 as cv
import numpy as np

input_image = cv.imread("K3/Jeppe/Exercise materials-20240228/aau-city-1.jpg")
output_image = input_image.copy()

############################################################
# Use cv2.cornerHarris to find corners and draw them with circles on output picture

# Your code here!
grey = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)

corners = cv.cornerHarris(grey, blockSize=2, ksize=3, k=0.04)

# threshold = np.max(corners)  0.4

for y in range(grey.shape[0]):
    for x in range(grey.shape[1]):
        if corners[y, x] > 300:  # threshold:
            output_image = cv.circle(output_image, (x, y), 10, (0, 0, 255))


############################################################
if __name__ == "__main__":

    cv.imshow("Display window", input_image)
    cv.imshow("Display window2", output_image)

    k = cv.waitKey(0)
