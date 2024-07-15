import mediapipe as mp
import time
import cv2

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDrawing = mp.solutions.drawing_utils

chnage_color_of_landmarks = mpDrawing.DrawingSpec(color = (2, 3, 4), thickness = 7)
chnage_color_of_lines = mpDrawing.DrawingSpec(color = (212, 32, 231), thickness = 5)

cap = cv2.VideoCapture(0)

ctime = 0
ptime = 0

while True:
    success, img = cap.read()
    imgbGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgbGR)
    print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y*h)
                if id == 0:
                    cv2.circle(img, (cx, cy), 10, (222, 123, 232), cv2.FILLED )


            mpDrawing.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS, chnage_color_of_landmarks, chnage_color_of_lines)

    ctime = time.time()
    fcm = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, f"fcm : {fcm}", (0, 40), cv2.FONT_HERSHEY_PLAIN, 3, (231, 231, 123), 5)

    cv2.imshow("asd", img)

    if cv2.waitKey(12) & 0xff == ord("x"):
        break