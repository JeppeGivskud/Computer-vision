from tracemalloc import start
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from mean_shift_FraKursus import *
from Functions import *


def meanShid(probability_map, window, start_point=[100, 100], radius=20):
    winx, winy, winw, winh = window
    winx, winy = start_point
    # initialize a circular kernal
    # +1 is to make the diameter odd to have a clear center
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1), np.float32)
    # make the circle filled with 1's
    cv.circle(kernel, (radius, radius), radius, 1, -1)
    Points = []
    for y in range(kernel.shape(0)):
        for x in range(kernel.shape(1)):
            if kernel(y, x) == 1:
                if probability_map(winy + y, winx + x) != 0:
                    Points.append([y, x])
    print(Points)

    return x, y


if __name__ == "__name__":
    video, template, template_hist = GenerateMask("WalkKomprimeret.mov", "Minion.png")
    while True:
        ret, frame = (
            video.read()
        )  # ret is a boolean checking if current it the last frame
        current_frame += 1
        if current_frame <= start_frame:
            continue
        if not ret:
            print("No frames grabbed! (End of video?)")
            break
        Probabilitymap = ProbabilityMap(frame, template_hist)
        meanShid(Probabilitymap)
