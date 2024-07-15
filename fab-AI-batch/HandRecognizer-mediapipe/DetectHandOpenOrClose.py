import numpy as np
import mediapipe as mp
import cv2
import MyHandRecognizerModulewithCordenates

cap = cv2.VideoCapture(0)

hand = MyHandRecognizerModulewithCordenates.MyHandDectorModule()

while True:
    success, img = cap.read()
    hand.HandDetector(img)

    myHCO = hand.HandCordenates(img)
    
    if len(myHCO) != 0:
        if myHCO[8][2] < myHCO[6][2]:
            print("Hand Open")
        else:
            print("Hand Close")

    else:
        print("Hand Not Found")

    cv2.imshow("Check Hand Open Or Close", img)

    cv2.waitKey(1)