import cv2 as cv
from Q4 import*

if __name__ == "__main__":
    Input=cv.imread("K1/Jeppe/ConstrastTHIS.png")
    cv.imshow("Original input", Input)

    LessContrast = LessContrast(Input)
    cv.imshow("Less Contrast", LessContrast)

    MoreContrast = StrechColorImage(Input)
    cv.imshow("More Contrast", MoreContrast)
    k = cv.waitKey(0)