import glob
import cv2 as cv
import numpy as np


path = glob.glob(
    "/Users/jakob/Documents/8. Semester/🤖 Computer Vision/OpenCV install/Lektion 4 Motion Analysis/UCSD_Anomaly_Dataset.v1p2/UCSDped1/Test/Test016/*.tif"
)
test16 = []
for img in path:
    n = cv.imread(img)
    test16.append(n)

for image in range(len(test16)):
    cv.imshow("yeet", test16[image])
    cv.waitKey(0)
