import cv2
import mediapipe as mp
import numpy as np


class handDetector():
    def __init__(self,
                 mode = False,
                 maxHands = 1,
                 detectionCon = 0.90,
                 trackCon = 0.85):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, 1, self.detectionCon, self.trackCon)


    def findHands(self, img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # Flip the image horizontally
        img = cv2.flip(img, 1)
        return img
    def findPosition(self, img, handNo=0):
        lmList = []
        if self.results.multi_hand_landmarks:

            myHand = self.results.multi_hand_landmarks[handNo]

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
        return lmList

    def is_pressing(self, lmList, threshold=15):
        """
        Check if landmark 8 is on top of landmark 4 (pressing action).
        Args:
        - lmList: List of landmarks with their coordinates.
        - threshold: Distance threshold to consider as pressing.

        Returns:
        - bool: True if pressing, False otherwise.
        """

        x8, y8 = lmList[8][1], lmList[8][2]
        x4, y4 = lmList[4][1], lmList[4][2]
        distance = np.sqrt((x8 - x4) ** 2 + (y8 - y4) ** 2)
        return distance < threshold





