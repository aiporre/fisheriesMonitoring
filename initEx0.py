import cv2
import numpy as np

cam = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)  # matriz para filtar
while True:
    ret, frame = cam.read()
    mxRange = np.array([50, 255, 50])
    mnRange = np.array([0, 20, 0])
    mask = cv2.inRange(frame, mnRange, mxRange)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    suma = np.asarray(opening).reshape(-1).sum()
    print suma
    detect = suma > 1000000
    if detect:

        try:
            x, y, w, h = cv2.boundingRect(opening)
        except:
            print 'error while creating rectange'
            x = 10
            y = 10
            w = 5
            h = 5
        cv2.rectangle(frame, (x,y), (x+w,y+h),(0,255,0),3)
        cv2.circle(frame, (x + w/2, y + h/2), 5,(0,0,255), -1)
    cv2.imshow('filter', opening)
    # cv2.imshow('cam1', frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

