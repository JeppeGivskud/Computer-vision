import random
from Threshold import*

import sys
sys.path.insert(0, '/Users/jeppegivskud/Documents/Programmering/VSCODE/Computer-vision/K2/Jeppe/Grassfire')
from Grassfire import*

sys.path.insert(0, '/Users/jeppegivskud/Documents/Programmering/VSCODE/Computer-vision/K1/Jeppe')
from Jeppe import*

def drawNewPicture(picture,Objects):
    for object in Objects:
        color=random.randint(0, 255)
        print(color)
        for pixel in object:
            picture[pixel[0]][pixel[1]]=color
    return picture


if __name__ == "__main__":
    print("Running")
    image = cv2.imread("K2/Jeppe/Grassfire/Turkeys.png", flags=cv2.IMREAD_GRAYSCALE)
    image=StrechActualGreyImage(image)
    image=Threshold(image,110)
    image=Flip(image)
    image=Extendimage(image)
    Objects=Grassfire(image)
    image=drawNewPicture(image,Objects)

    cv2.imshow("Display window", image)
    k = cv2.waitKey(0)
    print("Done")
