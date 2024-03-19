from tracemalloc import start
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from Functions import *


def meanShid(probability_map, start_point=[16, 16], radius=4):
    winx, winy = start_point
    # initialize a circular kernal
    # +1 is to make the diameter odd to have a clear center
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1), np.float32)
    # make the circle filled with 1's
    cv.circle(kernel, (radius, radius), radius, 1, -1)
    print(kernel)
    Points = []
    for y in range(radius):
        for x in range(radius):
            if kernel[y, x] == 1:
                if probability_map[winy + y, winx + x] != 0:
                    Points.append([winy + y, winx + x])
    print("Points before adjustment:", Points)

    adjusted_points = []
    for i in range(len(Points)):
        adjusted_points.append(
            [Points[i][0] - start_point[0], Points[i][1] - start_point[1]]
        )
    print("Points after adjustment:", adjusted_points)

    adjusted_pointsX = []
    adjusted_pointsY = []
    for Pixel in adjusted_points:
        adjusted_pointsX.append(Pixel[1])
        adjusted_pointsY.append(Pixel[0])
    print(adjusted_pointsX)
    print(adjusted_pointsY)
    averagex = np.sum(adjusted_pointsX) / len(adjusted_pointsX)
    averagey = np.sum(adjusted_pointsY) / len(adjusted_pointsY)
    print(averagex, averagey)
    return Points


if __name__ == "__main__":
    print("STARTING")
    video, template, template_hist = GenerateMask(
        "Workshop/WalkKomprimeret.mov", "Workshop/Minion.png"
    )
    # start_frame=144
    # current_frame = 0
    Probabilitymap = cv.imread("Workshop/Frame 1.png")
    Probabilitymap = cv.cvtColor(Probabilitymap, cv.COLOR_BGR2GRAY)

    meanShid(Probabilitymap)

    exit()
    while True:
        ret, frame = (
            video.read()
        )  # ret is a boolean checking if current it the last frame
        # current_frame += 1
        # if current_frame <= start_frame:
        #     continue
        # if not ret:
        #     print("No frames grabbed! (End of video?)")
        #     break
        # Probabilitymap = ProbabilityMap(frame, template_hist)
        # meanShid(Probabilitymap)
