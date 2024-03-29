from tracemalloc import start
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def get_start_point(frame, probability_map, window):
    # check that the track window is inside the frame
    if (
        window[0] + window[2] <= frame.shape[1]
        and window[1] + window[3] <= frame.shape[0]
    ):
        max_value = 0
        max_coords = (0, 0)
        for y in range(window[1], window[1] + window[3]):
            for x in range(window[0], window[0] + window[2]):
                if probability_map[y, x] > max_value:
                    max_value = probability_map[y, x]
                    max_coords = (x, y)
        return max_coords
    else:
        return print("tracking window out of bounds")


def meanShid(probability_map, window, start_point, radius):
    winx, winy, winw, winh = window

    # initialize a circular kernal
    # +1 is to make the diameter odd to have a clear center
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1), np.float32)
    # make the circle filled with 1's
    cv.circle(kernel, (radius, radius), radius, 1, -1)
    Points = []
    for y in range(kernel.shape(0)):
        for x in range(kernel.shape(1)):
            if kernel(y, x) == 1:
                if probability(winy + y, winx + x) != 0:
                    Points.append([y, x])
    print(Points)

    return x, y


# Example code
def meanShift(probability_map, window, start_point, radius):
    x, y, w, h = window
    # initialize a circular kernel
    # +1 is to make the diameter odd to have a clear center
    kernel = np.zeros((2 * radius + 1, 2 * radius + 1), np.float32)
    # make the circle filled with 1's
    cv.circle(kernel, (radius, radius), radius, 1, -1)

    # calculate the initial center of the window
    center_x = start_point[0] - x
    center_y = start_point[1] - y

    # iterate until convergence
    while True:
        # calculate the average of the vectors within the window
        avg_x = np.mean(probability_map[y : y + h, x : x + w] * kernel)
        avg_y = np.mean(probability_map[y : y + h, x : x + w] * kernel)

        # calculate the new center of the window
        new_center_x = int(center_x + avg_x)
        new_center_y = int(center_y + avg_y)

        # calculate the new window coordinates
        new_x = max(0, new_center_x - w // 2)
        new_y = max(0, new_center_y - h // 2)
        new_w = min(w, probability_map.shape[1] - new_x)
        new_h = min(h, probability_map.shape[0] - new_y)

        # check for convergence
        if new_x == x and new_y == y and new_w == w and new_h == h:
            break

        # update the window coordinates and center
        x, y, w, h = new_x, new_y, new_w, new_h
        center_x, center_y = new_center_x, new_center_y

    return x, y


path = "Exercise_4\\slow_traffic_small.mp4"
video = cv.VideoCapture(path)
template = cv.imread("Exercises_5\\biker.png")
hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)

# make a mask of the template
template_mask = cv.inRange(hsv_template, (12, 50, 70), (100, 255, 255))
template_hist = cv.calcHist(
    [hsv_template], [0, 1], template_mask, [180, 256], [0, 180, 0, 256]
)
cv.normalize(template_hist, template_hist, 0, 255, cv.NORM_MINMAX)

# make track window
track_window = (592, 180, template.shape[1], template.shape[0])
x, y, w, h = track_window
print(track_window[0])
# set termination criteria
termination_criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1)

# define start time
current_frame = 0
start_frame = 114
start_point = 0

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
    cv.imwrite("probability_map.png", probability)

    if start_point == 0:
        startpoint = get_start_point(frame, probability, track_window)
    # x, y = meanShid(probability, track_window, startpoint, 10)
    # _, track_window = cv.meanShift(probability, track_window, termination_criteria)

    x, y = meanShift(probability, track_window, startpoint, 10)

    frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 1)
    cv.imshow("MeanShift", frame)
    k = cv.waitKey(30) & 0xFF
    if k == 27:
        break


"""
Without a starting point the bounding box is just sitting in the corner, and when the biker gets smaller in the horizon, the tracking breaks. This is because the mask no longer fits the biker very well, as it is scale dependant.
"""
