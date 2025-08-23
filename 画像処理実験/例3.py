# -*- coding: utf-8 -*-
# 例題3　カメラの画像を取得してグレースケール変換した画像を表示させる

# 必要ライブラリのインポート
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np
import time

WIDTH  = 1920
HEIGHT = 1080
FPS    = 60

# カメラのキャプチャ
cap = cv2.VideoCapture(0)

# フォーマット・解像度・FPSの設定
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

# フレームの取得
ret, frame = cap.read()

# RGBグレースケール変換 cv2.COLOR_BGR2GRAY
# library
gray_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 画像を表示
cv2.imshow("frame", frame)
cv2.imshow("gray_1", gray_1)

time.sleep(1)

b, g, r = frame[..., 0], frame[..., 1], frame[..., 2]
gray_2 = (0.114 * b + 0.587 * g + 0.299 * r).astype(np.uint8)

cv2.imshow("gray_2", gray_2)

# 待機(0.03sec)
time.sleep(1)

# 画像の保存
result = cv2.imwrite("rei3.jpg", gray_1)
print("保存結果:", result)

result = cv2.imwrite("rei3jisaku.jpg", gray_2)
print("保存結果:", result)


# カメラのリリース
cap.release()
cv2.destroyAllWindows()