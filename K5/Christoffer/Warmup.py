import glob
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

input_image = cv.imread("Exercises_5\\traffic.png")
hsv_input = cv.cvtColor(input_image, cv.COLOR_BGR2HSV)
template = cv.imread("Exercises_5\\biker.png")
hsv_template = cv.cvtColor(template, cv.COLOR_BGR2HSV)
output_image = input_image.copy()


############################################################
# Compute the Histogram Backprojection for the template on
# the traffic image. Use it to draw a bounding box around
# the biker in the traffic image.
# Hint: Use the built in calcBackProject.

# Your code here
template_mask = cv.inRange(hsv_template, (12, 50, 70), (100, 255, 255))

# cv.imshow("asdas", template_mask)
# cv.waitKey(0)

template_hist = cv.calcHist([hsv_template], [0, 1], template_mask, [180, 256], [0, 180, 0, 256])
cv.normalize(template_hist, template_hist, 0, 255, cv.NORM_MINMAX)

plt.figure()
plt.title("Histogram")
plt.xlabel("Hue")
plt.ylabel("Frequency")
plt.plot(template_hist[:, 0])
plt.xlim([0, 180])
plt.show()

probability = cv.calcBackProject([hsv_input], [0, 1], template_hist, [0, 180, 0, 256], 1)
most_likely = np.max(probability)
most_likely_index = np.unravel_index(np.argmax(probability), probability.shape)

x = most_likely_index[1]
y = most_likely_index[0]
w = template.shape[1]
h = template.shape[0]

cv.rectangle(output_image, (x - w // 2, y - h // 2), (x + w // 2, y + h // 2), (0, 255, 0), 2)
cv.imshow("asdasd", output_image)
cv.waitKey(0)

############################################################

# cv.imwrite("output.png", output_image)
