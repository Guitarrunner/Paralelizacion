import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import imagehash
import pandas as pd
import numpy as np
import json
import base64
import requests
import threading
 
 
#pruebas 
dir = './'
global imgIn
global mockIn

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
 

def alphaAnalysis(case):

    img = f'{dir}/test/test.jpeg'
    mock= f'{dir}/test/mock.jpeg'

     # creating thread
    t1 = threading.Thread(target=calcImg, args=(case,img,1))
    t2 = threading.Thread(target=calcImg, args=(case,mock,2))
 
    t1.start()
    t2.start()
 
    t1.join()
    t2.join()
    

    match case:
        case 1:
            cs = []
            c1, c2 = 0, 0
            i = 0
            while i<len(imgIn) and i<len(mockIn):
                c1+=(imgIn[i]-mockIn[i])**2
                i+= 1
            c1 = c1**(1 / 2)
            cs += [c1[0]]
            ind = cs.index(min(cs))
            print(ind)
            print("La comparació de imágenes resulto en "+str(ind)+"\n")
        case 2:
            compHash = imgIn - mockIn
            print("La comparació de imágenes resulto en "+str(compHash)+"\n")
        case 3:
            print("Opción 3\n")
        case 4:
            print("Opción 4\n")
        case _:
            print("Opción no valida\n")

    return 0


if __name__ =="__main__":
   
    print(alphaAnalysis(1))
    print("Done!\n")

