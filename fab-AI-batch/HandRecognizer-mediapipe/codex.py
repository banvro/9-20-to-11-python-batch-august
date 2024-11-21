import mediapipe as mp
import MyHandRecognizerModulewithCordenates
import cv2
import time 
import os

wcam = 640
hcam = 480

cap = cv2.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)


folderpath = "FingerImages"
myList = os.listdir(folderpath)
# print(myList)
overlayList = []

for imagepath in myList:
    img = cv2.imread(f"{folderpath}/{imagepath}")
    overlayList.append(img)

while True:
    success, img = cap.read()
    h, w, c = overlayList[0].shape
    img[0:h, 0:w] = overlayList[0]

    cv2.imshow("c", img)
    cv2.waitKey(1)