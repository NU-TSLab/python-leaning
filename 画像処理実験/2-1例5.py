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

gray_1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 画像を表示
cv2.imshow("gray_1", gray_1)
cv2.waitKey(1000)

# 2値化
threshold = 128
max = 255
retval, binary = cv2.threshold(gray_1, threshold, max, cv2.THRESH_BINARY)
cv2.imshow("binary1", binary)
cv2.waitKey(1000)

# 保存
result = cv2.imwrite("rei5.jpg", binary)
print("保存結果:", result)
print(f"画像サイズ: {binary.shape}")
print(f"取り込んだ画像:{binary.nbytes}bytes")
filesize = os.path.getsize("rei5.jpg")
print(f"出力した画像:{filesize}bytes")

time.sleep(1)


# グレースケール化
b, g, r = frame[..., 0], frame[..., 1], frame[..., 2]
gray_2 = (0.114 * b + 0.587 * g + 0.299 * r).astype(np.uint8)

# 画像表示
cv2.imshow("gray_2", gray_2)
cv2.waitKey(1000)

# 二値化
binary = np.where(gray_1 > threshold, max, 0).astype(np.uint8)

cv2.imshow("binary2", binary)
cv2.waitKey(1000)

# 保存
result = cv2.imwrite("rei5jisaku.jpg", binary)
print("保存結果:", result)
print(f"画像サイズ: {binary.shape}")
print(f"取り込んだ画像: {binary.nbytes} bytes")
filesize = os.path.getsize("rei5jisaku.jpg")
print(f"出力した画像: {filesize} bytes")


# カメラのリリース
cap.release()
cv2.destroyAllWindows()