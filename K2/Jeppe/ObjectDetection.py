import random

from Threshold import*
from Grassfire import Grassfire
from Modules import Q4


if __name__ == "__main__":
    print("Running")
    inputImage = cv2.imread("K2/Jeppe/Grassfire/Turkeys.png", flags=cv2.IMREAD_GRAYSCALE)
    
    #Pre-processing
    lesscontrast=Q4.ActualLessContrast(inputImage,0.5)
    Stretched=Q4.StrechActualGreyImage(inputImage)
    
    threshold=FindThreshold(Stretched)
    Binary=Threshold(Stretched,threshold)
    BinaryFlipped = Flip(Binary)

    Extended=Grassfire.Extendimage(BinaryFlipped)
    Objects=Grassfire.Grassfire(Extended)
    Grassfired=drawNewPicture(Extended,Objects)


    cv2.imshow("inputImage", inputImage)
    cv2.imshow("Stretched", Stretched)
    cv2.imshow("Binary", Binary)
    cv2.imshow("BinaryFlipped", BinaryFlipped)
    cv2.imshow("Grassfired", Grassfired)
    k = cv2.waitKey(0)
    print("Done")
