import mediapipe as mp
import time
import cv2


class handDetector:
    def __init__(self, mode = False, max_Hands = 2, detectCon = 0.5, minconfi = 0.5):
        self.mode = mode
        self.max_Hands = max_Hands
        self.detectCon = detectCon
        self.minconfi = minconfi
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
    max_num_hands=self.max_Hands,
    min_detection_confidence=self.detectCon,
    min_tracking_confidence=self.minconfi
    )
        self.mpDrawing = mp.solutions.drawing_utils

        self.chnage_color_of_landmarks = self.mpDrawing.DrawingSpec(color = (2, 3, 4), thickness = 7)
        self.chnage_color_of_lines = self.mpDrawing.DrawingSpec(color = (212, 32, 231), thickness = 5)



    def detet_hands(self, img, draw = True):

        imgbGR = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = self.hands.process(imgbGR)
        # print(result.multi_hand_landmarks)

        if result.multi_hand_landmarks:
            for handlms in result.multi_hand_landmarks:
               if draw:
                    self.mpDrawing.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS, self.chnage_color_of_landmarks, self.chnage_color_of_lines)
        return img


def main():
    cap = cv2.VideoCapture(0)
    ctime = 0
    ptime = 0

    detecor = handDetector()
    while True:
        success, img = cap.read()
        img = detecor.detet_hands(img)
        cv2.imshow("asd", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()