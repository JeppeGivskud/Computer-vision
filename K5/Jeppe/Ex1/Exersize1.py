import glob
import cv2
import numpy as np

# Exercise 1

# Use the biker.png template from Exercise materials to do mean shift
# tracking in the traffic video in Exercise materials.
# (Hint: use OpenCV's calcBackProject() function to produce a similarity image for mean shift
# - see this mean shift tutorial for more pointers)

# Note that for mean shift tracking you need to provide an initial tracking window
# manually, and the biker only shows up from frame 114, so wait until then to start tracking.

# What happens when the biker disappears over the horizon? Why?

# Importing
template = cv2.imread("Ex1/biker copy.png")
video_capture = cv2.VideoCapture("Ex1/slow_traffic_small.mp4")

# Initial tracking
## Calculate histogram of the template
template_hsv = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
template_hsv = cv2.calcHist([template_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
## Normalize histogram
cv2.normalize(template_hsv, template_hsv, 0, 255, cv2.NORM_MINMAX)

# loop from picture 114
video_capture.set(cv2.CAP_PROP_POS_FRAMES, 114)
ret, frame = video_capture.read()
# find initial position
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
## Calculate the back projection
propabilities = cv2.calcBackProject(
    [frame_hsv], [0, 1], template_hsv, [0, 180, 0, 256], 1
)
max_value = np.max(propabilities)
max_index = np.unravel_index(np.argmax(propabilities), propabilities.shape)

# Draw bounding box around the detected object
x = max_index[1]
y = max_index[0]
w = template.shape[1]  # Width of the template
h = template.shape[0]  # Height of the template

frame = cv2.rectangle(
    frame, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), (0, 255, 0), 2
)
cv2.imwrite("Ex1/output.png", frame)
# manually
ret, frame = video_capture.read()
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

tolerance = 20
subframe = frame_hsv[
    y - tolerance - h // 2 : y + tolerance + h // 2,
    x - tolerance - w // 2 : x + tolerance + w // 2,
]
# subframe = cv2.cvtColor(subframe, cv2.COLOR_HSV2BGR)

propabilities = cv2.calcBackProject(
    [subframe], [0, 1], template_hsv, [0, 180, 0, 256], 1
)
# cv2.imwrite("Ex1/output.png", propabilities)
canvas = np.zeros_like(frame_hsv)
canvas[
    y - tolerance - h // 2 : y + tolerance + h // 2,
    x - tolerance - w // 2 : x + tolerance + w // 2,
    2,
] = propabilities

max_value = np.max(propabilities)
max_index = np.unravel_index(np.argmax(propabilities), propabilities.shape)
# TODO: tilføj bounding box xy til billedet så det passer rigtigt
# Draw bounding box around the detected object
x = max_index[1]
y = max_index[0]
w = template.shape[1]  # Width of the template
h = template.shape[0]  # Height of the template

canvas = cv2.rectangle(
    canvas, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), (0, 255, 0), 2
)
cv2.imwrite("Ex1/output.png", canvas)

exit()
while True:
    ret, frame = video_capture.read()
    if not ret:
        break
    ## Find initial position of template
    # Convert the frame to HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Extract the subframe from the original picture
    subframe = frame_hsv[y : y + h, x : x + w]
    subframe = cv2.cvtColor(subframe, cv2.COLOR_HSV2BGR)

    # Calculate the back projection on subframe
    propabilities = cv2.calcBackProject(
        [subframe], [0, 1], template_hsv, [0, 180, 0, 256], 1
    )
    # Draw the probabilities frame on a black canvas
    canvas = np.zeros_like(frame_hsv)
    canvas[y : y + h, x : x + w, 0] = propabilities
    # cv2.imwrite("Ex1/output.png", subframe)

    # Find meanshift inside

    # ret, track_window = cv2.meanShift(dst, (x, y, w, h), term_crit)


### draw rectangle
## Find position in bounded area. maybe the biker.png shape
### draw rectangle

## if new positions are not found exit()

exit()
# Set the termination criteria for mean shift
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

# Initialize variables for tracking window
x, y, w, h = 300, 200, 100, 50  # Initial tracking window

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Calculate the back projection
    dst = cv2.calcBackProject([hsv], [0, 1], roi_hist, [0, 180, 0, 256], 1)

    # Apply meanshift to get the new location
    ret, track_window = cv2.meanShift(dst, (x, y, w, h), term_crit)

    # Draw the tracking window on the frame
    x, y, w, h = track_window
    img2 = cv2.rectangle(frame, (x, y), (x + w, y + h), 255, 2)
    cv2.imshow("img2", img2)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
