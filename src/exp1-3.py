import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
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

gray_lib = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow("Flame", frame)
cv2.imshow("gray_1", gray_lib)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()