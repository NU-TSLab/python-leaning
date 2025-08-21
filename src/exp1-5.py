# -*- coding: utf-8 -*-
# 内蔵グレースケール演算した画像後に二値化させる

# 必要ライブラリのインポート
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

WIDTH = 1920
HEIGHT = 1080
FPS = 60

# カメラのキャッチャ
cap = cv2.VideoCapture(0)

# フォーマット・解像度・FPSの設定
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

# 二値化のしきい値
threshold_half = 127
threshold_q1 = 63
threshold_q2 = 127 + 64

# フレームの取得
ret, frame = cap.read()

# 画像を表示
cv2.imshow("Frame", frame)

# RGBグレースケール変換 cv2.COLOR_BGR2GRAY
# library
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 自作で演算
# 二値化
# library
ret, img_thresh_half = cv2.threshold(gray, threshold_half, 255, cv2.THRESH_BINARY)
ret, img_thresh_q1 = cv2.threshold(gray, threshold_q1, 255, cv2.THRESH_BINARY)
ret, img_thresh_q2 = cv2.threshold(gray, threshold_q2, 255, cv2.THRESH_BINARY)
# 自作関数
gray[gray[:] != 0] = 255

# 画像を表示
cv2.imshow("digitize_half", img_thresh_half)
cv2.imshow("digitize_q1", img_thresh_q1)
cv2.imshow("digitize_q2", img_thresh_q2)
cv2.waitKey(0)

# カメラのリリース
cap.release()
cv2.destroyAllWindows()
