import cv2
import math
import numpy as np


# #read in video
cap = cv2.VideoCapture('Metal_SLS_Steady_Camera_Trim.mp4')

#find fps and calculate time between each frame
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
f2fTime = 1/fps

#consider the size of powder bed, interpolate actual distance from pixel
_, Frame = cap.read()
height,width,_ = Frame.shape

cXPre = 0
cYPre = 0
while(1):
    _, currentFrame = cap.read()
    if currentFrame is None:
        break
    capGray = cv2.cvtColor(currentFrame,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(capGray,250,255,0)
    M = cv2.moments(thresh)
    if M["m00"] != 0:
         cXCurr = int(M["m10"] / M["m00"])
         cYCurr = int(M["m01"] / M["m00"])
    else:
         cXCurr, cYCurr = 0, 0
    distance = math.sqrt(math.pow(cXCurr - cXPre,2) + math.pow(cYCurr - cYPre,2))
    velocity = distance/f2fTime
    print('x: ', cXCurr, 'y: ', cYCurr)
    print(velocity)
    cv2.circle(currentFrame, (cXCurr,cYCurr), 3, (0,255,0), 2)
    cv2.imshow('fdsf', currentFrame)
    cXPre = cXCurr
    cYPre = cYCurr
    cv2.waitKey(0)


cap.release()


