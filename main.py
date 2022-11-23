import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import imagehash
import json
import base64
import threading
import time

#pruebas 
dir = '.'
imgIn=""
mockIn=""

def calcImg(num,t1,flag):
   match num:
    case 1:
        print("Encriptación 1: Histograma cv2\n")
        image = cv2.imread(t1)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        if flag: imgIn=histogram
        else: mockIn=histogram
    case 2:
        print("Encriptación 2: Hash average hash\n")
        if flag: imgIn=imagehash.average_hash(Image.open(t1))
        else: mockIn=imagehash.average_hash(Image.open(t1))
    case 3:
        print("Encriptación 3: Histograma hard coded\n")
        img = Image.open(t1)
        pixels=[]
        for x in range(256):
            pixels.append(x)
        
        width,height=img.size
        counts=[]
        
        for i in pixels:
            temp=0
            for x in range(width):
                for y in range(height):
                    if (img.getpixel((x,y))==i):
                        temp=temp+1
            counts.append(temp)

        if flag: imgIn=pixels
        else: mockIn=pixels
    case 4:
        print("Encriptación 4: Hash whash\n")
        if flag: imgIn=imagehash.whash(Image.open(t1))
        else: mockIn=imagehash.whash(Image.open(t1))
    case _:
        print("Opción no valida\n")
 

def alphaAnalysis(case1,case2):

    img = f'{dir}/test/test.jpeg'
    mock= f'{dir}/test/mock.jpeg'

     # creating thread
    t1 = threading.Thread(target=calcImg, args=(case1,img,1))
    t2 = threading.Thread(target=calcImg, args=(case2,mock,2))
    totalStartTime = time.time()
    startTime1 = time.time()
    t1.start()
    startTime2 = time.time()
    t2.start()
 
    t1.join()
    endTime1 = time.time()
    print("El tiempo de la primera encriptación fue de "+str(endTime1 - startTime1)+"s\n")
    t2.join()
    endTime2 = time.time()
    totalEndTime = time.time()
    print("El tiempo de la segunda encriptación fue de "+str(endTime2 - startTime2)+"s\n")
    print("El tiempo de total de encriptación con hilos fue de "+str(totalEndTime - totalStartTime)+"s\n")

    totalStartTime = time.time()
    calcImg(1,img,1)
    calcImg(2,mock,2)
    totalEndTime = time.time()
    print("El tiempo de total de encriptación sin hilos fue de "+str(totalEndTime - totalStartTime)+"s\n")

    return 0


if __name__ =="__main__":
    case1 = input("Digite el primer método de encriptación (Del 1 al 4): \n")
    case2 = input("Digite el primer método de encriptación (Del 1 al 4): \n")
    alphaAnalysis(int(case1),int(case2))
    
    print("Done!\n")

