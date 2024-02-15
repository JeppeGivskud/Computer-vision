import cv2 as cv
import sys

def GreyScalePixel(pixel):
    rWeight=0.33
    gWeight=0.33
    bWeight=0.33
    return round(pixel[0]*rWeight+pixel[1]*gWeight+pixel[2]*bWeight)
           
def PointProcessing(image,manipulation):
    newImage=image
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            newImage[x][y] = manipulation(image[x][y])
    return newImage

def GreyScaleThisImage(Image):
    NewImage = PointProcessing(Image,GreyScalePixel)

    return NewImage

def findBounderies(Image):
    low=255
    high=0
    for x in range(Image.shape[0]):
        for y in range(Image.shape[1]):
            value=Image[x][y][0]
            if (value<=low):
                low=Image[x][y][0]
            if (value>=high):
                high=Image[x][y][0]
    return int(low),int(high)

def StrechPixel(value,lower,upper):
    b=-lower
    a=255/(upper+b)
    #print("OST")
    Value=value[0]
    newValue=round(a*(Value+b))
    return newValue

def StrechGreyImage(Image):
    GrayImage = GreyScaleThisImage(Image)
    StrechedImage=Image

    lower,upper=findBounderies(GrayImage)

    for x in range(GrayImage.shape[0]):
        for y in range(GrayImage.shape[1]):
            StrechedImage[x][y] = StrechPixel(GrayImage[x][y],lower,upper)
    return StrechedImage

def ActualLessContrast(inputImage,koefficient):
    Image=inputImage.copy()
    a=koefficient

    for y in range(Image.shape[0]):
        for x in range(Image.shape[1]):
            Image[y][x]=a*Image[y][x]

    return Image

def findActualGreyBounderies(Image):
    low=255
    high=0
    for y in range(Image.shape[0]):
        for x in range(Image.shape[1]):
            value=Image[y][x]
            if (value<=low):
                low=Image[y][x]
            if (value>=high):
                high=Image[y][x]
    return int(low),int(high)

def StrechActualPixel(Pixel,lower,upper):
    b=-lower
    a=255/(upper+b)

    Value=Pixel
    newValue=round(a*(Value+b))
    return newValue

def StrechActualGreyImage(Image):
    lower,upper=findActualGreyBounderies(Image)

    for y in range(Image.shape[0]):
        for x in range(Image.shape[1]):
            Image[y][x] = StrechActualPixel(Image[y][x],lower,upper)
    return Image

#Color images
def findColorBounderies(Image,nr):
    low=255
    high=0
    for x in range(Image.shape[0]):
        for y in range(Image.shape[1]):
            value=Image[x][y][nr]
            if (value<=low):
                low=Image[x][y][nr]
            if (value>=high):
                high=Image[x][y][nr]
    return int(low),int(high)

def StrechColorPixel(Pixel,number,lower,upper):
    Lower=lower[number]
    Upper=upper[number]
    b=-Lower
    a=255/(Upper+b)
    #print("OST")

    Value=Pixel[number]
    newValue=round(a*(Value+b))

    if (newValue>255):
        newValue=255
        print("OVER 255")

    if (newValue<0):
        newValue=0
        print("UNDER 0")
    return newValue

def FindEdges(Image):
    lowerR,upperR=findColorBounderies(Image,0)
    lowerG,upperG=findColorBounderies(Image,1)
    lowerB,upperB=findColorBounderies(Image,2)
    lower = [lowerR,lowerG,lowerB]
    upper = [upperR,upperG,upperB]
    print(f'lower:{lower}\n'
          f'upper:{upper}')
    return lower,upper

def StrechColorImage(Image):
    StrechedImage=Image
    lower,upper=FindEdges(Image)
    for x in range(Image.shape[0]):
        for y in range(Image.shape[1]):
            for i in range(Image.shape[2]):
                StrechedImage[x][y][i] = StrechColorPixel(Image[x][y],i,lower,upper)
#            StrechedImage[x][y][1] = StrechColorPixel(Image[x][y],1,lowerG,upperG)
 #           StrechedImage[x][y][2] = StrechColorPixel(Image[x][y],2,lowerB,upperB)
    FindEdges(StrechedImage)
    return StrechedImage

if __name__ == "__main__":

    GED=cv.imread("K1/GOAT2LowContrast copy.png")

    if GED is None:
        sys.exit("Could not read the image.")

    if False:
        cv.imshow("Display window", GED)
        k = cv.waitKey(0)
        if k == ord("s"):
            cv.imwrite("GOAT.png", GED)

    if False:
        count=0
        for x in range(GED.shape[0]):
            for y in range(GED.shape[1]):
                print(GED[x][y])
                count=count+1
        print(count)
    if False:
        NewGed = GreyScaleThisImage(GED)
        cv.imshow("Display window", NewGed)
        #k = cv.waitKey(0)
        #exit() 

    if False:
        NewGed = GreyScaleThisImage(GED)
        low,high=findBounderies(NewGed)
        print(low)
        print(high)

    if False:
        pixel= [102,150,150]
        newpixel=StrechPixel(pixel,100,150)
        print(newpixel)

    if False:
        NewGed = StrechGreyImage(GED)
        #NewGed2 = GreyScalePixel(GED)
        cv.imshow("STRECH window", NewGed)
        #cv.imshow("GREY window", NewGed2)
        k = cv.waitKey(0)

    if False:
        NewGed = StrechColorImage(GED)
        #NewGed2 = GreyScalePixel(GED)
        cv.imshow("STRECH window", NewGed)
        #cv.imshow("GREY window", NewGed2)
        k = cv.waitKey(0)
