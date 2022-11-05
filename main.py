# from ctypes.wintypes import RGB
import cv2
import numpy as np
import mediapipe as mp
import pyautogui



cap = cv2.VideoCapture(0)
pyautogui.FAILSAFE=False
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils


while True:

    _, img = cap.read()# The image that we take here is the BGR image.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.flip(img, 1)
    image_height,image_width,_ = img.shape
    # Change image from bgr to rgb because hands.process takes rgb images
    RGBimage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(RGBimage)
    if result.multi_hand_landmarks:
       
        for handLMS in result.multi_hand_landmarks:
            # handLMS is the list of the laandmarks contining landmarks coordinates
            handLMS = handLMS.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            y,x = handLMS.y,handLMS.x
            
            y=handLMS.y*image_height
            x=handLMS.x*image_width
            pyautogui.moveTo(x,y,duration=0.25)

            
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
