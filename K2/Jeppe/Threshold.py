import cv2
def Threshold(image,threshold):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]): 
            if image[y][x]<threshold:
                image[y][x]=0
            else:
                image[y][x]=255
    return image

def Flip(image):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]): 
            if (image[y][x]==0): 
                image[y][x]=255
            else : 
                image[y][x]=0
    return image

if __name__=="__main__":
    print("Running")
    image = cv2.imread("K2/Jeppe/Grassfire/Lady.png", flags=cv2.IMREAD_GRAYSCALE)
    newimage=Threshold(image,150)
    newimage=Flip(newimage)
    image = cv2.imread("K2/Jeppe/Grassfire/Lady.png", flags=cv2.IMREAD_GRAYSCALE)

    cv2.imshow("Display window", image)
    cv2.imshow("Displaewy window", newimage)
    k = cv2.waitKey(0)
