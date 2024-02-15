import random;
from Threshold import*
from Grassfire import Grassfire
from Modules import Q4


def drawNewPicture(picture,Objects):
    for object in Objects:
        color=random.randint(0, 255)
        print(color)
        for pixel in object:
            picture[pixel[0]][pixel[1]]=color
    return picture


if __name__ == "__main__":
    print("Running")
    image = cv2.imread("K2/Jeppe/Grassfire/KAT<3.png", flags=cv2.IMREAD_GRAYSCALE)
    image=Q4.StrechActualGreyImage(image)

    threshold=FindThreshold(image)
    image=Threshold(image,threshold+10)
    image=Flip(image)

    image=Grassfire.Extendimage(image)
    Objects=Grassfire.Grassfire(image)
    image=drawNewPicture(image,Objects)

    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    print("Done")
