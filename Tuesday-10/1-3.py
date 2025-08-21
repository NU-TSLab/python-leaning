import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]="0"
import cv2
import numpy as np
import time
print(cv2.__version__)
WIDTH = 1920
HEIGHT = 1080
FPS = 60

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)

ret, frame = cap.read()

gray_lib = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = 0.114*frame[:,:,0] + 0.587*frame[:,:,1] + 0.299*frame[:,:,2]

cv2.imshow("Frmae", frame)
cv2.imshow("gray_1", gray_lib)
cv2.imshow("gray_cal", gray)
time.sleep(0.03)

cv2.imwrite("1-3_frame.jpeg", frame)
cv2.imwrite("1-3_gray_lib.jpeg", gray_lib)
cv2.imwrite("1-3_gray_cal.jpeg", gray)

cap.release()
cv2.destroyAllWindows()