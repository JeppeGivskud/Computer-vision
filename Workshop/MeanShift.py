from tracemalloc import start
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from Functions import *


def meanShift(probability_map, start_point=[10, 15], radius=15):
    # Takes values inside circle and finds their relative position to the center

    # initialize a circular kernal
    # +1 is to make the diameter odd to have a clear center
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1), np.float32)
    # make the circle filled with 1's
    cv.circle(kernel, (radius, radius), radius, 1, -1)

    # Find points with value over 0
    Points = []
    for y in range(kernel.shape[0]):
        for x in range(kernel.shape[1]):
            if kernel[y, x] == 1:
                if probability_map[start_point[0] + y, start_point[1] + x] > 0:
                    Points.append([start_point[0] + y, start_point[1] + x])

    # Find the vectors from the middle of the circle
    adjusted_points = []
    for i in range(len(Points)):
        adjusted_points.append(
            [
                Points[i][0] - (start_point[0] + radius),
                Points[i][1] - (start_point[1] + radius),
            ]
        )

    # Split vectors into x and y for calculating average
    adjusted_pointsy = []
    adjusted_pointsx = []
    for i in range(len(adjusted_points)):
        adjusted_pointsy.append(adjusted_points[i][0])
        adjusted_pointsx.append(adjusted_points[i][1])

    # Calculate average change in y and x
    averagey = np.average(adjusted_pointsy)
    averagex = np.average(adjusted_pointsx)
    new_Location = round(averagey + start_point[0]), round(averagex + start_point[1])

    # Check if the new location is the same as the last (not good way to end loop)
    DoAnotherMeanShift = True
    if new_Location[0] == start_point[0] and new_Location[1] == start_point[1]:
        DoAnotherMeanShift = False
        print("ENDING")

    # The x and y locations are flipped for some reason
    new_Location = np.transpose(new_Location)

    return new_Location, DoAnotherMeanShift


if __name__ == "__main__":
    print("STARTING")

    video = cv.VideoCapture("Workshop/Orange.mov")
    template, template_hist = GenerateMask("Workshop/OrangeTemplate.png")

    # Get startposition
    ret, frame = video.read()

    Probabilitymap = ProbabilityMap(frame, template_hist)

    max_value = np.max(Probabilitymap)
    max_index = np.unravel_index(np.argmax(Probabilitymap), Probabilitymap.shape)

    startlocation = max_index
    MeanShiftRadius = 30

    print(startlocation)

    while True:
        ret, frame = video.read()
        Probabilitymap = ProbabilityMap(frame, template_hist)
        # cv.imshow("output", Probabilitymap)
        # cv.imshow("output2", frame)
        # cv.waitKey(0)

        DoMeanShift = True
        while DoMeanShift:
            startlocation, DoMeanShift = meanShift(
                Probabilitymap, startlocation, MeanShiftRadius
            )
        # cv.rectangle(
        #     frame,
        #     (startlocation[0] - MeanShiftRadius, startlocation[1] - MeanShiftRadius),
        #     (startlocation[0] + MeanShiftRadius, startlocation[1] + MeanShiftRadius),
        #     (0, 255, 0),
        #     2,
        # )
        cv.rectangle(
            frame,
            (startlocation[1], startlocation[0]),
            (
                startlocation[1] + MeanShiftRadius * 2,
                startlocation[0] + MeanShiftRadius * 2,
            ),
            (0, 255, 0),
            2,
        )

        cv.imshow("output", frame)
        cv.waitKey(0)
