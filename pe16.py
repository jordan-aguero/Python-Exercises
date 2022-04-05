import numpy as np
import cv2 as cv

img = np.zeros((500,600,3), np.uint8)
# cv.circle(img,(80, 350), 50, (75, 75,255), -1)
# cv.circle(img,(520, 350), 50, (75, 75,255), -1)
cv.line(img,(0,90),(331,130),(255,0,0),5)
cv.line(img,(529,248),(1000,600),(255,0,0),5)
cv.line(img,(529,130),(600, 100),(255,0,0),5)
cv.rectangle(img,(330,250),(530,128),(255,0,0),-1)
cv.ellipse(img,(160, 170),(80,50), 15, 0, 180,(255,255,255),-1)
cv.ellipse(img,(160, 170),(20,50), 15, 0, 181,(0,0,250),-1)
cv.ellipse(img,(300, 370),(100,80),0, 0,180,(100, 100, 255),-1)
cv.putText(img,'JORDAN',(355, 200), cv.FONT_ITALIC, 1.3,(255,255,255),2,cv.LINE_4)

cv.imshow('display', img)
cv.waitKey(0)
cv.destrolAllWindows()