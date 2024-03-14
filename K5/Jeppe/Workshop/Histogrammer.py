import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

template = cv.imread("biker copy.png")
hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)

# make a mask of the template
template_hist_hue = cv.calcHist([hsv_template], [0], None, [180], [0, 180])
template_hist_satu = cv.calcHist([hsv_template], [1], None, [256], [0, 256])
# cv.normalize(template_hist_satu, template_hist_satu, 0, 255, cv.NORM_MINMAX)


def plotme(name, xlabel, ylabel, data, limits):
    plt.figure()
    plt.title(name)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(data)
    plt.xlim(limits)
    plt.show()


cv.imwrite("output.png", template)
print(template_hist_hue)
template_hist_hue = template_hist_hue * 2
print(template_hist_hue)

plotme("Histogram Hue", "Hue", "Frequency", template_hist_hue, [0, 360])

plotme("Histogram Saturation", "Saturation", "Frequency", template_hist_satu, [0, 255])
