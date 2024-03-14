import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


path = "Kast.mp4"
video = cv.VideoCapture(path)
template = cv.imread("Minion.png")
hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)
ret, frame = video.read()  # ret is a boolean checking if current it the last frame
cv.imwrite("output.png", frame)
