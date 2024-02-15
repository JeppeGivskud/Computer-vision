import cv2

def Histogram(image):
    histogram=[]
    for i in range(0,255):
        histogram.append(0)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]): 
            value=image[y][x]-1
            histogram[value]+=1
    return histogram

def FindThreshold(image):
    sum=0
    for y in range(image.shape[0]):
        for x in range(image.shape[1]): 
            sum+=image[y][x]
    Threshold=sum/(image.shape[0]*image.shape[1])
    return int(Threshold)


def Threshold(inputImage,threshold):
    Image=inputImage.copy()

    for y in range(Image.shape[0]):
        for x in range(Image.shape[1]): 
            if Image[y][x]<threshold:
                Image[y][x]=0
            else:
                Image[y][x]=255
    return Image

def Flip(inputImage):
    Image=inputImage.copy()
    for y in range(Image.shape[0]):
        for x in range(Image.shape[1]):
            if Image[y][x] < 200:
                Image[y][x] = 255
            else:
                Image[y][x] = 0
    return Image


if __name__=="__main__":
    print("Running")
    image = cv2.imread("K2/Jeppe/Grassfire/Lady.png", flags=cv2.IMREAD_GRAYSCALE)

    threshold=FindThreshold(image)

    newimage=Threshold(image,threshold)
    newimage=Flip(newimage)
    image = cv2.imread("K2/Jeppe/Grassfire/Lady.png", flags=cv2.IMREAD_GRAYSCALE)


    cv2.imshow("Display window", image)
    cv2.imshow("Displaewy window", newimage)
    k = cv2.waitKey(0)
