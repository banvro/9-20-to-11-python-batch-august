import mediapipe as mp
import time
import cv2


class MyHandDectorModule:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, minDectioncon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minDectioncon = minDectioncon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDrawing = mp.solutions.drawing_utils
        self.chnage_color_of_landmarks = self.mpDrawing.DrawingSpec(color = (2, 3, 4), thickness = 7)
        self.chnage_color_of_lines = self.mpDrawing.DrawingSpec(color = (212, 32, 231), thickness = 5)


    def HandDetector(self, img, draw = True):
        imgbGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(imgbGR)
        # print(result.multi_hand_landmarks)
        ctime = 0
        ptime = 0

        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
                if draw:
                    self.mpDrawing.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS, self.chnage_color_of_landmarks, self.chnage_color_of_lines)

        ctime = time.time()
        fcm = 1 / (ctime - ptime)
        ptime = ctime

        cv2.putText(img, f"fcm : {fcm}", (0, 40), cv2.FONT_HERSHEY_PLAIN, 3, (231, 231, 123), 5)

    

def main():
    cap = cv2.VideoCapture(0)
    detector = MyHandDectorModule()
    while True:
        success, img = cap.read()
        detector.HandDetector(img)
        cv2.imshow("Hand Recognizer", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()