import cv2
import numpy as np

def CheckSurroundings(image,position_to_burn,deck):
    y=position_to_burn[0]
    x=position_to_burn[1]
    #print("check neighbors of: ",y,",",x)

    four=y-1,x
    three=y,x-1
    two=y+1,x
    one=y,x+1

    #print(f'Four: {four}, Three: {three}, Two: {two}, One: {one}')

    if (image[four]==255): 
        deck.append(four) 
        #print(f'4 is {image[four]} and has been added')
    if (image[three]==255): 
        deck.append(three) 
        #print(f'3 is {image[three]} and has been added')
    if (image[two]==255): 
        deck.append(two) 
        #print(f'2 is {image[two]} and has been added')
    if (image[one]==255): 
        deck.append(one) 
        #print(f'1 is {image[one]} and has been added')

    return deck


def Grassfire(image):
    #Load image
    #array of objects
    #go through image x,y
        #If pixel = 255
            #deck=[]
            #while  deck is not empty
                #newdeck,objectCoordinates=Burn(toppixel)
                #deck.append
                #objectarray.append=objectcoordinates
            #append pixel to array in position 0
                #pixel = 0
                # check if surrounding pixels are object.
                # append each surrounding pixel to deck
            #if deck is not empty take top stack and run burn procedure
    
    Objects=[]
    #print(f'{image.shape[1],image.shape[0]}')

    for y in range(image.shape[0]):
        for x in range (image.shape[1]):                
                #print(f'{y,x} is {image[y,x]}')

                deck=[]
                if image[y,x]==255:
                    count=0
                    deck.append([y,x])

                    objectPixels=[]
                    while (len(deck)>0):
                        #burn
                        position_to_burn = deck[len(deck)-1]
                        image[position_to_burn[0]][position_to_burn[1]]=0;
                        #print(f'Position {position_to_burn} is burnt and the image has value {image[position_to_burn[0],position_to_burn[1]]}')

                        objectPixels.append(position_to_burn)
                        #print(f'Pixel {position_to_burn} has been appened to objectpixels: {objectPixels}')

                        #print(f'The deck {deck} is popped {deck.pop(len(deck)-1)} and is now {deck}')

                        #deck.pop(len(deck)-1)

                        deck=CheckSurroundings(image,position_to_burn,deck)
                        #print(f'The neighboring cells are checked and these were found {deck}')
                        #print()

                    #print("deck is empty ",deck)
                    #print("count is: ",count)
                    #exit()
                    Objects.append(objectPixels)
                    #exit()

                    #Checksurroundings(coordinate)
                        #checks the coordiante surroundings and appends the deck with the surrounding if it is bad.
    for i in range(len(Objects)):
        print(f'Nr {i} has size {len(Objects[i])} is: {Objects[i]}')   
                #print(deck)
    return Objects

def Extendimage(image):
    output_image = np.zeros((image.shape[0]+2, image.shape[1]+2), dtype=image.dtype)
    #print(output_image)
    for y in range(output_image.shape[0]-1):
        for x in range (output_image.shape[1]-1):
            if y>0 and y<output_image.shape[0] and x>0 and x<output_image.shape[1]:
                output_image[y,x]=image[y-1,x-1]
    return output_image

if __name__ == "__main__":
    print("Running")
    image = cv2.imread("K2/Jeppe/Grassfire/Lady.png", flags=cv2.IMREAD_GRAYSCALE)
    image=Extendimage(image)
    print(image)
    Objects=Grassfire(image)

    image = cv2.imread("K2/Jeppe/Grassfire/step2.png", flags=cv2.IMREAD_GRAYSCALE)
    image=Extendimage(image)
    print(image)
