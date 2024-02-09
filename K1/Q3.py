import cv2 as cv
import sys

GED=cv.imread("K1/GOAT.png")

if GED is None:
    sys.exit("Could not read the image.")

if False:
    cv.imshow("Display window", GED)
    k = cv.waitKey(0)
    if k == ord("s"):
        cv.imwrite("GOAT.png", GED)
print(GED.shape)

if True:
    count=0
    for x in range(GED.shape[0]):
        for y in range(GED.shape[1]):
            print(GED[x][y])
            count=count+1
    print(count)

