import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]="0"
import cv2
import numpy as np
import time
WIDTH = 1920
HEIGHT = 1080
FPS = 60

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

ret, frame = cap.read()
cv2.imwrite("1-4_OpenCV_frame1.jpeg", frame)
gray1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


ret, frame = cap.read()
cv2.imwrite("1-4_OpenCV_frame2.jpeg", frame)
gray2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

diff = cv2.absdiff(gray1, gray2)

cv2.imshow("Frame", diff)
cv2.waitKey(0)

cv2.imwrite("1-4_OpenCV_diff.jpeg", diff)

cap.release()
cv2.destroyAllWindows()