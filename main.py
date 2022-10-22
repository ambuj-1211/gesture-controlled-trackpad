# from ctypes.wintypes import RGB
import cv2
import numpy as np
import mediapipe as mp
import pyautogui



cap = cv2.VideoCapture(0)

pyautogui.FAILSAFE=True
mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=3)
mpDraw = mp.solutions.drawing_utils


while True:

    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.flip(img, 1)
    image_height,image_width,_ = img.shape
    # Change image from bgr to rgb because hands.process takes rgb images
    RGBimage = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(RGBimage)
    if result.multi_hand_landmarks:
       
        for handLMS,face in result.multi_hand_landmarks,faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            face_frame = img.copy()
            cv2.rectangle(face_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            landmarks = predictor(gray, face)
            landmarks = face_utils.shape_to_np(landmarks)
            left_blink = blinked(landmarks[36], landmarks[37],
                             landmarks[38], landmarks[41], landmarks[40], landmarks[39])
            right_blink = blinked(landmarks[42], landmarks[43],
                              landmarks[44], landmarks[47], landmarks[46], landmarks[45])
            # handLMS is the list of the laandmarks contining landmarks coordinates
            handLMS = handLMS.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP]
            y,x = handLMS.y,handLMS.x
            pyautogui.moveTo(x,y,duration=0.25)
            if(left_blink == 1 or right_blink == 1):
                click+=1
            # y=handLMS.y*image_height
            # x=handLMS.x*image_width

            
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
