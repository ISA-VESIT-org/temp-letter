import cv2
import mediapipe 
import pyautogui

webcame = cv2.VideoCapture(0)
while True:
    _ , image = webcame.read()
    cv2.imshow("Hand Volume control", image)
    
    
