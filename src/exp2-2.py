# -*- coding: utf-8 -*-
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2
import numpy as np

# カメラのキャッチャ
cap = cv2.VideoCapture(0)   # 0 は内蔵カメラ

if not cap.isOpened():
    print("カメラが開けませんでした")
    exit()

# 1枚撮影
ret, frame = cap.read()
cap.release()

if not ret:
    print("撮影に失敗しました")
    exit()

# グレースケール変換
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# 円検出
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1,             # 解像度の逆数
    minDist=20,       # 円同士の最小距離（適宜調整）
    param1=100,       # Cannyエッジ検出の閾値
    param2=30,        # 円検出のしきい値（小さいと誤検出が増える）
    minRadius=5,      # 最小半径
    maxRadius=100     # 最大半径
)

# 結果表示
if circles is not None:
    circles = np.uint16(np.around(circles))
    print("検出された円の数:", circles.shape[1])

    for i in circles[0, :]:
        # 外円
        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # 中心
        cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)
else:
    print("円は検出されませんでした")

cv2.imshow("Detected Circles", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
