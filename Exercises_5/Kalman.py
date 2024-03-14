import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

debugMode = True


def calc_centroid(corners):
    x = sum(corners[:, 0] / len(corners[:, 0]))
    y = sum(corners[:, 1] / len(corners[:, 1]))
    return np.array([np.float32(x), np.float32(y)], np.float32)


# initialize video and template in hsv
path = "Exercise_4\\slow_traffic_small.mp4"
video = cv.VideoCapture(path)
template = cv.imread("Exercises_5\\biker.png")
hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)

# initialize Kalman filter
# first param is number of states, second is dimensions of measurement. 4 states is (x, y, x-speed, y-speed), 2 in measurements is x and y position
kalman = cv.KalmanFilter(4, 2)

# identity matrices for the state, transistion and covariance matrices
kalman.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], np.float32)

# this is the identity matrice with 1 on [0,2] and [1,3] to account for changes in the x and y directions (velocity)
kalman.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32)
# starting value for the noise covariance. 0.1 means that little noise is expected
kalman.processNoiseCov = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], np.float32) * 0.1

# this is the variable the measured position will be stored in
# measurement = np.zeros((2, 1), np.float32)

# this is the position the kalman filter expects the object to be in
prediction = np.zeros((4, 1), np.float32)

# make a mask of the template
template_mask = cv.inRange(hsv_template, (12, 50, 70), (100, 255, 255))
template_hist = cv.calcHist([hsv_template], [0, 1], template_mask, [180, 256], [0, 180, 0, 256])
cv.normalize(template_hist, template_hist, 0, 255, cv.NORM_MINMAX)

# make track window
track_window = (592, 180, template.shape[1], template.shape[0])

# set termination criteria
termination_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

# define start time
current_frame = 0
start_frame = 114

# Loop happends every frame of video (ends on end of video)
while True:
    ret, frame = video.read()  # ret is a boolean checking if current it the last frame
    current_frame += 1
    if current_frame <= start_frame:
        continue

    if not ret:
        print("No frames grabbed! (End of video?)")
        break
    frame_hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    probability = cv.calcBackProject([frame_hsv], [0, 1], template_hist, [0, 180, 0, 256], 1)
    cv.normalize(probability, probability, 0, 255, cv.NORM_MINMAX)

    # cam shift works better with varying scale
    ret, track_window = cv.CamShift(probability, track_window, termination_criteria)

    # take measurement of position as center of bounding box and update model
    corners = cv.boxPoints(ret)
    corners = np.int0(corners)
    measurement = calc_centroid(corners)
    kalman.correct(measurement)

    # predict next position
    prediction = kalman.predict()

    x, y, w, h = track_window
    frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)

    frame = cv.circle(frame, (int(prediction[0]), int(prediction[1])), 3, (0, 255, 0), -1)

    cv.imshow("MeanShift", frame)

    if debugMode:
        print("######### UPDATE #########")
        print(kalman.errorCovPost)
        time.sleep(1)

    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break
