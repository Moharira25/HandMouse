from handTrackingModule import handDetector
import pyautogui
import time
import cv2
import numpy as np
def main():
    # Get the camera width and height (if needed, you can set this explicitly)
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cam_height, cam_width, _ = frame.shape

    detector = handDetector()
    last_press_time = 0
    click_count = 0
    prev_y = 0
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            if detector.is_pressing(lmList):
                current_time = time.time()
                if current_time - last_press_time < 1:
                    click_count += 1
                else:
                    click_count = 1

                if click_count == 2:
                    pyautogui.doubleClick()
                    click_count = 0
                else:
                    pyautogui.click()

                last_press_time = current_time

            #code for scrolling.
            x12, y12 = lmList[12][1], lmList[12][2]
            x8, y8 = lmList[8][1], lmList[8][2]
            scroll_distance = np.sqrt((x12 - x8) ** 2 + (y12 - y8) ** 2)
            print(scroll_distance)
            if scroll_distance < 30:

                pyautogui.scroll(y12 - prev_y)

            prev_y = y12

            x, y = lmList[4][1], lmList[4][2]
            # Inverted screen coordinates to move the mouse correctly
            screen_x = int(pyautogui.size()[0] - (x * pyautogui.size()[0] / img.shape[1]))
            screen_y = int(y * pyautogui.size()[1] / img.shape[0])

            pyautogui.moveTo(screen_x, screen_y, duration=0.1)





if __name__ == '__main__':
    main()