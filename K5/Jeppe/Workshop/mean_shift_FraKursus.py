import cv2 as cv
import numpy as np

path = "WalkKomprimeret.mov"
video = cv.VideoCapture(path)
template = cv.imread("Minion.png")
hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)

# make a mask of the template
template_mask = cv.inRange(hsv_template, (0, 0, 0), (255, 255, 255))
template_hist = cv.calcHist(
    [hsv_template], [0, 1], template_mask, [180, 256], [0, 180, 0, 256]
)
cv.normalize(template_hist, template_hist, 0, 255, cv.NORM_MINMAX)

# make track window
track_window = (125, 400, 70, 70)

# set termination criteria
termination_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

# define start time
current_frame = 0
start_frame = 114

while True:
    ret, frame = video.read()  # ret is a boolean checking if current it the last frame
    current_frame += 1
    if current_frame <= start_frame:
        continue
    if not ret:
        print("No frames grabbed! (End of video?)")
        break
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    probability = cv.calcBackProject(
        [frame_hsv], [0, 1], template_hist, [0, 180, 0, 256], 1
    )
    cv.normalize(probability, probability, 0, 255, cv.NORM_MINMAX)

    _, track_window = cv.meanShift(probability, track_window, termination_criteria)

    x, y, w, h = track_window
    frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
    cv.imshow("MeanShift", frame)
    # cv.imshow("MeanShift", probability)
    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break


"""
Without a starting point the bounding box is just sitting in the corner, and when the biker gets smaller in the horizon, the tracking breaks. This is because the mask no longer fits the biker very well, as it is scale dependant.
"""
