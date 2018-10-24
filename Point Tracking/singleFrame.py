import cv2
import numpy as np



picGray = cv2.imread('Centroid.png',0)
_,thresh = cv2.threshold(picGray,0,220,0)
M = cv2.moments(thresh)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])
cv2.circle(picGray, (cX, cY), 5, (255, 255, 255), -1)
cv2.imshow('fdsaf',picGray)
cv2.waitKey(0)
# while(1):
#     _, currentFrame = cap.read()
#     # convert BGR to HSV (for simpler array manipulation)
#     capHsv = cv2.cvtColor(currentFrame,cv2.COLOR_BGR2HSV)
#     # HSV value for white: Hue-0; Saturation-0; Value = 100%
#     currentMask = cv2.inRange(capHsv, lower_white, upper_white)

#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break