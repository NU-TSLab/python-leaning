# -*- coding: utf-8 -*-
# 例題4　2枚のカメラの画像の差分を表示させる

import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np
import time

# absdiff自作関数
def img_diff(img1, img2):
    return np.abs(np.array(img1, dtype='int32') - np.array(img2, dtype='int32')).astype('uint8')

# hsv自作関数
def rgb_to_hsv(src):
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    v = hsv[..., 2]
    return v


def get_OpenCV(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray

def get_rbg(frame):
    b, g, r = frame[..., 0], frame[..., 1], frame[..., 2]
    rbg = (0.114 * b + 0.587 * g + 0.299 * r).astype(np.uint8)
    return rbg

get_colorplane = {"hsv":rgb_to_hsv,"OpenCV":get_OpenCV,"rgb":get_rbg}


# カメラ初期設定
cap = cv2.VideoCapture(0)

for name, colorplane in get_colorplane.items():

    # 背景画像を取得して背景画像に設定
    if input("Press enter to start operations...") == "q":
        ret, bg = cap.read()
        bg_frame = colorplane(bg)

    # フレームの取得
    if input("Press enter to start operations...") == "w":
        ret, frame = cap.read()
        fr_frame = colorplane(frame)

    # 背景画像との差分を計算
    diff = cv2.absdiff(fr_frame, bg_frame)

    # 画像表示
    cv2.imshow("backgrand", bg_frame)
    cv2.imshow("frame", fr_frame)
    cv2.imshow("gray", diff)
    cv2.waitKey(1000)

    # 画像の保存
    result = cv2.imwrite(f"rei4_{name}_bg.jpg", bg)
    print("bg保存結果:", result)
    result = cv2.imwrite(f"rei4_{name}_frame.jpg", frame)
    print("frame保存結果:", result)
    result = cv2.imwrite(f"rei4_{name}_gray.jpg", diff)
    print("gray保存結果:", result)

# カメラのリリース
cap.release()
cv2.destroyAllWindows()