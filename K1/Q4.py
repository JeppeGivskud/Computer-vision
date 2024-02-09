import cv2 as cv
import sys

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

if False:
    NewGed = GreyScaleThisImage(GED)
    cv.imshow("Display window", NewGed)
    #k = cv.waitKey(0)
    #exit() 

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

if False:
    NewGed = GreyScaleThisImage(GED)
    low,high=findBounderies(NewGed)
    print(low)
    print(high)

def StrechPixel(value,lower,upper):
    b=-lower
    a=255/(upper+b)
    #print("OST")
    Value=value[0]
    newValue=round(a*(Value+b))
    return newValue

if False:
    pixel= [102,150,150]
    newpixel=StrechPixel(pixel,100,150)
    print(newpixel)

def StrechGreyImage(Image):
    GrayImage = GreyScaleThisImage(Image)
    StrechedImage=Image

    lower,upper=findBounderies(GrayImage)

    for x in range(GrayImage.shape[0]):
        for y in range(GrayImage.shape[1]):
            StrechedImage[x][y] = StrechPixel(GrayImage[x][y],lower,upper)
    return StrechedImage

if False:
    NewGed = StrechGreyImage(GED)
    #NewGed2 = GreyScalePixel(GED)
    cv.imshow("STRECH window", NewGed)
    #cv.imshow("GREY window", NewGed2)
    k = cv.waitKey(0)

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
    b=-lower
    a=255/(upper+b)
    #print("OST")

    Value=Pixel[number]
    newValue=round(a*(Value+b))
    return newValue

def StrechColorImage(Image):
    StrechedImage=Image

    lowerR,upperR=findColorBounderies(Image,0)
    lowerG,upperG=findColorBounderies(Image,1)
    lowerB,upperB=findColorBounderies(Image,2)
    
    print(f'LowerR: {lowerR}, UpperR: {upperR}\n'
          f'LowerG: {lowerG}, UpperG: {upperG}\n'
          f'LowerB: {lowerB}, UpperR: {upperB}\n')
    
    for x in range(Image.shape[0]):
        for y in range(Image.shape[1]):
            StrechedImage[x][y][0] = StrechColorPixel(Image[x][y],0,lowerR,upperR)
            StrechedImage[x][y][1] = StrechColorPixel(Image[x][y],1,lowerG,upperG)
            StrechedImage[x][y][2] = StrechColorPixel(Image[x][y],2,lowerB,upperB)

    return StrechedImage

if False:
    NewGed = StrechColorImage(GED)
    #NewGed2 = GreyScalePixel(GED)
    cv.imshow("STRECH window", NewGed)
    #cv.imshow("GREY window", NewGed2)
    k = cv.waitKey(0)