from tracemalloc import start
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from Functions import *


def meanShid(probability_map, start_point=[10, 15], radius=15):
    # Takes values inside circle and finds their relative position to the center

    # initialize a circular kernal
    # +1 is to make the diameter odd to have a clear center
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1), np.float32)
    # make the circle filled with 1's
    cv.circle(kernel, (radius, radius), radius, 1, -1)

    Points = []
    for y in range(kernel.shape[0]):
        for x in range(kernel.shape[1]):
            if kernel[y, x] == 1:
                if probability_map[start_point[0] + y, start_point[1] + x] > 0:
                    Points.append([start_point[0] + y, start_point[1] + x])

    # print("Points before adjustment:", Points)
    adjusted_points = []
    for i in range(len(Points)):
        adjusted_points.append(
            [
                Points[i][0] - (start_point[0] + radius),
                Points[i][1] - (start_point[1] + radius),
            ]
        )
    adjusted_pointsy = []
    adjusted_pointsx = []
    # print("Points after adjustment:", adjusted_points)
    for i in range(len(adjusted_points)):
        adjusted_pointsy.append(adjusted_points[i][0])
        adjusted_pointsx.append(adjusted_points[i][1])

    averagey = np.average(adjusted_pointsy)
    averagex = np.average(adjusted_pointsx)

    # print("Adjustment: ", averagey, averagex)
    # print("Old location: ", start_point[0], start_point[1])
    # print("New location: ", averagey + start_point[0], averagex + start_point[1])
    new_Location = round(averagey + start_point[0]), round(averagex + start_point[1])
    # Color Original image
    copy = probability_map.copy()
    for pixel in Points:
        copy[pixel[0], pixel[1]] = 100
    cv.imshow("output", copy)
    cv.waitKey(1)

    end = False
    if new_Location[0] == start_point[0] and new_Location[1] == start_point[1]:
        end = True
        print("ENDING")

    return new_Location, end


if __name__ == "__main__":
    print("STARTING")
    video, template, template_hist = GenerateMask(
        "Workshop/WalkKomprimeret.mov", "Workshop/Minion.png"
    )
    # start_frame=144
    # current_frame = 0
    Probabilitymap = cv.imread("Workshop/Frame 3.png")
    Probabilitymap = cv.cvtColor(Probabilitymap, cv.COLOR_BGR2GRAY)
    cv.imshow("output", Probabilitymap)
    cv.waitKey(300)
    startlocation = [10, 10]

    end = False
    while not end:
        startlocation, end = meanShid(Probabilitymap, startlocation, 100)

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
