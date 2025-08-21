import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]="0"
import cv2
import numpy as np
import time
WIDTH = 1920
HEIGHT = 1080
FPS = 60

threshold = 100

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

ret, img_thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow("Frame", img_thresh)
cv2.waitKey(0)

cv2.imwrite("1-5_OpenCV_th.jpeg", img_thresh)

cap.release()
cv2.destroyAllWindows()