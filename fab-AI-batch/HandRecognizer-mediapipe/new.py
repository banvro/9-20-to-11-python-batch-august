import cv2
import mediapipe as mp
import time

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

change_color_of_landmark = mpDraw.DrawingSpec(color = (255, 0, 255), thickness = 8, circle_radius = 3)
change_landmark_connections = mpDraw.DrawingSpec(color = (232, 342, 122), thickness = 4, circle_radius =  2)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handlms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS, change_color_of_landmark, change_landmark_connections)

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    cv2.imshow("capture", img)
    if cv2.waitKey(20) & 0xFF == ord("x"):
        break