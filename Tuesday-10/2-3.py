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
red = frame[:, :, 2]
blue = frame[:, :, 0]
red = cv2.medianBlur(red, 3)
blue = cv2.medianBlur(blue, 3)

# 円検出
red_circles = cv2.HoughCircles(
    red,
    cv2.HOUGH_GRADIENT,
    dp=1,             # 解像度の逆数
    minDist=10,       # 円同士の最小距離（適宜調整）
    param1=150,       # Cannyエッジ検出の閾値
    param2=60,        # 円検出のしきい値（小さいと誤検出が増える）
    minRadius=0,      # 最小半径
    maxRadius=0    # 最大半径
)
blue_circles = cv2.HoughCircles(
    blue,
    cv2.HOUGH_GRADIENT,
    dp=1,             # 解像度の逆数
    minDist=10,       # 円同士の最小距離（適宜調整）
    param1=150,       # Cannyエッジ検出の閾値
    param2=60,        # 円検出のしきい値（小さいと誤検出が増える）
    minRadius=0,      # 最小半径
    maxRadius=0    # 最大半径
)
# 結果表示
if red_circles is not None:
    red_circles = np.uint16(np.around(red_circles))
    print("検出された赤い円の数:", red_circles.shape[1])

    for i in red_circles[0, :]:
        # 外円
        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # 中心
        cv2.circle(frame, (i[0], i[1]), 2, (0, 255, 0), 3)
else:
    print("赤い円は検出されませんでした")

if blue_circles is not None:
    blue_circles = np.uint16(np.around(blue_circles))
    print("検出された青い円の数:", blue_circles.shape[1])

    for i in blue_circles[0, :]:
        # 外円
        cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # 中心
        cv2.circle(frame, (i[0], i[1]), 2, (0, 255, 0), 3)
else:
    print("青い円は検出されませんでした")

cv2.imshow("Detected Circles", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()