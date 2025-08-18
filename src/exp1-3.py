import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np
import time

WIDTH = 800
HEIGHT = 600
FPS = 60

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

ret, frame = cap.read()

gray_lib = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# 関数を使わない
# 単純平均法(Avarage Method)
gray_ave = np.mean(frame, axis=2).astype(np.uint8)

# 最大値・最小値法(Desaturation)
gray_desaturation = ((np.max(frame, axis=2) + np.min(frame, axis=2)) / 2).astype(np.uint8)

cv2.imshow("Flame", frame)
cv2.imshow("gray_1", gray_lib)
cv2.imshow("gray_ave", gray_ave)
cv2.imshow("gray_desaturation", gray_desaturation)

cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()