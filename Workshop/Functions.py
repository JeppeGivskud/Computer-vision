import cv2 as cv
import numpy as np


def GenerateMask(Videopath, templatepath):
    video = cv.VideoCapture(Videopath)
    template = cv.imread(templatepath)
    hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)

    # make a mask of the template
    template_mask = cv.inRange(hsv_template, (0, 0, 0), (255, 255, 255))
    template_hist = cv.calcHist(
        [hsv_template], [0, 1], template_mask, [180, 256], [0, 180, 0, 256]
    )
    cv.normalize(template_hist, template_hist, 0, 255, cv.NORM_MINMAX)
    return video, template, template_hist


def ProbabilityMap(frame, template_hist):
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    probability = cv.calcBackProject(
        [frame_hsv], [0, 1], template_hist, [0, 180, 0, 256], 1
    )
    cv.normalize(probability, probability, 0, 255, cv.NORM_MINMAX)
    return probability
