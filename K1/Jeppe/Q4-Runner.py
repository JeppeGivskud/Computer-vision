import cv2 as cv
from Q4 import*

def LessContrast(Image):
    a=0.5
    b=100
    newImage=Image

    for x in range(Image.shape[0]):
        for y in range(Image.shape[1]):
            pixelr = a*(Image[x][y][0]+b)
            pixelg = a*(Image[x][y][1]+b)
            pixelb = a*(Image[x][y][2]+b)
            newImage[x][y][0]=pixelr
            newImage[x][y][1]=pixelg
            newImage[x][y][2]=pixelb
    return newImage

if __name__ == "__main__":
    Input=cv.imread("K1/Jeppe/ConstrastTHIS.png")
    cv.imshow("Original input", Input)

#    LessContrast = LessContrast(Input)
#    cv.imshow("Less Contrast", LessContrast)

    MoreContrast = StrechColorImage(Input)
    cv.imshow("More Contrast", MoreContrast)
    k = cv.waitKey(0)