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

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def bgr_to_gray(frame):
    gray_frame = 0.114 * frame[:, :, 0] + 0.587 * frame[:, :, 1] + 0.299 * frame[:, :, 2]
    return np.clip(gray_frame, 0, 255).astype(np.uint8)

def frame_threshold(frame):
    thresh = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            if frame[i, j] >= threshold:
                thresh[i][j] = 255
            else:
                thresh[i][j] = 0

    return np.asarray(thresh, dtype=np.uint8)

ret, frame = cap.read()
gray = bgr_to_gray(frame)

img_thresh = frame_threshold(gray)

cv2.imshow("Frame", img_thresh)
cv2.waitKey(0)

cv2.imwrite("1-5_no_OpenCV_th.jpeg", img_thresh)

cap.release()
cv2.destroyAllWindows()