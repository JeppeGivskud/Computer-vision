#from COMPUTER-VISION.K2.Jeppe.Grassfire.Grassfire import Extendimage
import random
from Threshold import*
import sys
sys.path.insert(0, '/Users/jeppegivskud/Documents/Programmering/VSCODE/Computer-vision/K2/Jeppe/Grassfire')
from Grassfire import*
#from K2.Jeppe.Grassfire.Grassfire import*

def drawNewPicture(picture,Objects):
    for object in Objects:
        color=random(0,255)
        print(color)
        for pixel in object:
            picture[pixel[0]][pixel[1]]=color
    return picture


if __name__ == "__main__":
    print("Running")
    image = cv2.imread("K2/Jeppe/Grassfire/Lady.png", flags=cv2.IMREAD_GRAYSCALE)
    image=Threshold(image,150)
    image=Extendimage(image)
    Objects=Grassfire(image)
    image=drawNewPicture(image,Objects)

    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    print("Done")
