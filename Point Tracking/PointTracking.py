import cv2
import math
import numpy as np


#read in video
cap = cv2.VideoCapture('Laser pointer_Trim.mp4')

#find fps and calculate time between each frame
fps = cap.get(cv2.CAP_PROP_FPS)
f2fTime = 1/fps

#consider the size of powder bed, interpolate actual distance from pixel
_, Frame = cap.read()
height,width,_ = Frame.shape
bedXLength = 1280
bedYLength = 7200


cXPre = 0
cYPre = 0
while(1):
    _, currentFrame = cap.read()
    if currentFrame is None:
        break
    capGray = cv2.cvtColor(currentFrame,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(capGray,200,255,0)
    M = cv2.moments(thresh)
    if M["m00"] != 0:
         cXCurr = int(M["m10"] / M["m00"])
         cYCurr = int(M["m01"] / M["m00"])
    else:
         cXCurr, cYCurr = 0, 0
    distance = math.sqrt((cXCurr - cXPre)^2 + (cYCurr - cYPre)^2)
    velocity = distance/f2fTime
    print(velocity)

cap.release()


