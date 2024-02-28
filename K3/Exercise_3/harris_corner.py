from asyncio.windows_events import NULL
import cv2 as cv
import numpy as np

part1 = cv.imread("Exercises\\Exercise_3\\aau-city-1.jpg")
part2 = cv.imread("Exercises\\Exercise_3\\aau-city-2.jpg")

print(part1.shape)

part1_gray = np.float32(cv.cvtColor(part1, cv.COLOR_BGR2GRAY))
part2_gray = np.float32(cv.cvtColor(part2, cv.COLOR_BGR2GRAY))

part1_corner = cv.cornerHarris(part1_gray, 2, 3, 0.04)
part2_corner = cv.cornerHarris(part2_gray, 2, 3, 0.04)

# Dilate is nice to make the corner markings bigger
part1_corner = cv.dilate(part1_corner, None)
part2_corner = cv.dilate(part2_corner, None)

# Determine the threshold so that not every detected gets marked
# Set the color of each pixel where gradient value is greater than threshold to green
thresh1 = 0.5 * part1_corner.max()
part1[part1_corner > thresh1] = [0, 255, 0]
# np.where finds the coordinates where the green marks are for the corners
feature_location1 = np.where(part1_corner > thresh1)

test = []
for y in feature_location1[0]:
    if y > 0 and y < part1_gray.shape[0]:
        for x in feature_location1[1]:
            if x > 0 and x < part1_gray.shape[1]:
                bruh = part1_gray[y - 1 : y + 2, x - 1 : x + 2]

print(test)

"""
thresh2 = 0.03 * part2_corner.max()
part2[part2_corner > thresh2] = [0, 255, 0]
"""
cv.imshow("part1", part1)
cv.imshow("part2", part2)
cv.waitKey(0)
