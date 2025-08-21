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

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

def bgr_to_gray(frame):
    gray_frame = 0.114 * frame[:, :, 0] + 0.587 * frame[:, :, 1] + 0.299 * frame[:, :, 2]
    return np.clip(gray_frame, 0, 255).astype(np.uint8)

def bgr_to_hsv(frame):
    hsv = [[[0 for k in range(3)] for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            b = float(frame[i, j, 0])
            g = float(frame[i, j, 1])
            r = float(frame[i, j, 2])
            ma = max(b, g, r)
            mi = min(b, g, r)
            d = ma - mi
            v = ma
            if ma == 0:
                s = 0
            else:
                s = d / ma
            if d == 0:
                h = 0
            elif ma == r:
                h = 60 * (((g - b) / d) % 6)
            elif ma == g:
                h = 60 * ((b - r) / d + 2)
            else:
                h = 60 * ((r - g) / d + 4)
            
            hsv[i][j][0] = min(179, max(0, round(h / 2)))
            hsv[i][j][1] = min(255, max(0, round(s * 255)))
            hsv[i][j][2] = round(v)
    
    return np.asarray(hsv, dtype=np.uint8)

def hsv_to_gray(hsv, use):
    gray_scale = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            if use == 'h':
                gray = float(hsv[i, j, 0]) * (255 / 179)
            elif use == 's':
                gray = hsv[i, j, 1]
            else:
                gray = hsv[i, j, 2]
            gray_scale[i][j] = round(gray)

    return np.asarray(gray_scale, dtype=np.uint8)

def absdiff(f1, f2):
    diff_frame = [[0 for j in range(width)] for i in range(height)]
    for i in range(height):
        for j in range(width):
            diff_frame[i][j] = abs(int(f1[i, j]) - int(f2[i, j]))

    return np.asarray(diff_frame, dtype=np.uint8)

ret, frame1 = cap.read()
cv2.imwrite("1-4_no_OpenCV_frame1.jpeg", frame1)
time.sleep(1)
ret, frame2 = cap.read()
cv2.imwrite("1-4_no_OpenCV_frame2.jpeg", frame2)

gray1_1 = bgr_to_gray(frame1)
gray1_2 = bgr_to_gray(frame2)
cv2.imwrite("1-4_no_OpenCV_gray1_1.jpeg", gray1_1)
cv2.imwrite("1-4_no_OpenCV_gray1_2.jpeg", gray1_2)
cv2.imwrite("1-4_no_OpenCV_diff_BGR2GRAY.jpeg", absdiff(gray1_1, gray1_2))

gray2_1 = hsv_to_gray(bgr_to_hsv(frame1), 'h')
gray2_2 = hsv_to_gray(bgr_to_hsv(frame2), 'h')
cv2.imwrite("1-4_no_OpenCV_gray2_1.jpeg", gray2_1)
cv2.imwrite("1-4_no_OpenCV_gray2_2.jpeg", gray2_2)
cv2.imwrite("1-4_no_OpenCV_diff_from_H.jpeg", absdiff(gray2_1, gray2_2))

gray3_1 = hsv_to_gray(bgr_to_hsv(frame1), 's')
gray3_2 = hsv_to_gray(bgr_to_hsv(frame2), 's')
cv2.imwrite("1-4_no_OpenCV_gray3_1.jpeg", gray3_1)
cv2.imwrite("1-4_no_OpenCV_gray3_2.jpeg", gray3_2)
cv2.imwrite("1-4_no_OpenCV_diff_from_S.jpeg", absdiff(gray3_1, gray3_2))

gray4_1 = hsv_to_gray(bgr_to_hsv(frame1), 'v')
gray4_2 = hsv_to_gray(bgr_to_hsv(frame2), 'v')
cv2.imwrite("1-4_no_OpenCV_gray4_1.jpeg", gray4_1)
cv2.imwrite("1-4_no_OpenCV_gray4_2.jpeg", gray4_2)
cv2.imwrite("1-4_no_OpenCV_diff_from_V.jpeg", absdiff(gray4_1, gray4_2))

cap.release()
cv2.destroyAllWindows()