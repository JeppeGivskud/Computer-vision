import cv2
import numpy as np

input_image = cv2.imread("Warmup/traffic.png")
template = cv2.imread("Warmup/biker copy.png")

############################################################
# Compute the Histogram Backprojection for the template on
# the traffic image. Use it to draw a bounding box around
# the biker in the traffic image.
# Hint: Use the built-in cv2.calcBackProject.

# Convert images to HSV color space
hsvt = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

# Calculate histogram of the template
M = cv2.calcHist([hsvt], [0, 1], None, [180, 256], [0, 180, 0, 256])

# Normalize histogram
cv2.normalize(M, M, 0, 255, cv2.NORM_MINMAX)
# Calculate back projection
B = cv2.calcBackProject([hsv], [0, 1], M, [0, 180, 0, 256], 1)

max_value = np.max(B)
max_index = np.unravel_index(np.argmax(B), B.shape)

print("Maximum value:", max_value)
print("Location of maximum value (row, column):", max_index)

# Draw bounding box around the detected object
x = max_index[1]
y = max_index[0]
w = template.shape[1]  # Width of the template
h = template.shape[0]  # Height of the template

input_image = cv2.rectangle(
    input_image, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), (0, 255, 0), 2
)

############################################################
cv2.imwrite("Warmup/output.png", input_image)
