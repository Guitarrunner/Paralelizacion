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
        image = cv2.imread(t1)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])
        if flag: imgIn=histogram
        else: mockIn=histogram
        
        print("Opción 1\n")
    case 2:
        if flag: imgIn=imagehash.average_hash(Image.open(t1))
        else: mockIn=imagehash.average_hash(Image.open(t1))
        print("Opción 2\n")
    case 3:
        print("Opción 3\n")
    case 4:
        print("Opción 4\n")
    case _:
        print("Opción no valida\n")
 

def alphaAnalysis(case1,case2):

    img = f'{dir}/test/test.jpeg'
    mock= f'{dir}/test/mock.jpeg'

     # creating thread
    t1 = threading.Thread(target=calcImg, args=(case1,img,1))
    t2 = threading.Thread(target=calcImg, args=(case2,mock,2))
    startTime1 = time.time()
    t1.start()
    startTime2 = time.time()
    t2.start()
 
    t1.join()
    endTime1 = time.time()
    print("El tiempo de la primera encriptación fue de "+str(endTime1 - startTime1)+"s\n")
    t2.join()
    endTime2 = time.time()
    print("El tiempo de la primera encriptación fue de "+str(endTime2 - startTime2)+"s\n")

    return 0


if __name__ =="__main__":
   
    print(alphaAnalysis(1,2))
    print("Done!\n")

