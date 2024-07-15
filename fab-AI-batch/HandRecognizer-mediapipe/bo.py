import cv2 
import mediapipe as mp
import numpy as np
import time
import MyHandRecognizerModuleTest

cap = cv2.VideoCapture(0)
detector = MyHandRecognizerModuleTest.MyHandDectorModule()
while True:
    success, img = cap.read()
    
    imgx = detector.HandDetector(img)
    
    lmlst = detector.findPostion(img)

    # print(lmlst)
    if len(lmlst) != 0:
        if lmlst[8][2] < lmlst[6][2]:
            print("index finder open")
    else:
        print("no hand found")




    cv2.imshow("Asd", img)
    cv2.waitKey(1)