import cv2 as cv
import numpy as np


def GenerateMask(templatepath):
    template = cv.imread(templatepath)
    hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)

    # make a mask of the template
    template_mask = cv.inRange(hsv_template, (0, 0, 0), (255, 255, 255))
    template_hist = cv.calcHist(
        [hsv_template], [0, 1], template_mask, [180, 256], [0, 180, 0, 256]
    )
    cv.normalize(template_hist, template_hist, 0, 255, cv.NORM_MINMAX)
    return template, template_hist


def ProbabilityMap(frame, template_hist):
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    probabilitymap = cv.calcBackProject(
        [frame_hsv], [0, 1], template_hist, [0, 180, 0, 256], 1
    )

    cv.normalize(probabilitymap, probabilitymap, 0, 255, cv.NORM_MINMAX)
    return probabilitymap


def get_start_point(frame, probability_map, window):
    # check that the track window is inside the frame
    if (
        window[0] + window[2] <= frame.shape[1]
        and window[1] + window[3] <= frame.shape[0]
    ):
        max_value = 0
        max_coords = [0, 0]
        for y in range(window[1], window[1] + window[3]):
            for x in range(window[0], window[0] + window[2]):
                if probability_map[y, x] > max_value:
                    max_value = probability_map[y, x]
                    max_coords = [y, x]
        return max_coords
    else:
        return print("tracking window out of bounds")
