# -*- coding: utf-8 -*-
# 例題4、2枚のカメラの画像の差分を表示させる
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2
import numpy as np
import time

# absdiff自作関数
def img_diff(img1, img2):
    diff = np.abs(np.array(img1,dtype='int32') - np.array(img2,dtype='int32'))
    return np.array(diff, dtype='uint8')

# hsv自作関数
def rgb_to_hsv(src):
    # BGR to RGB
    b, g, r = cv2.split(src.astype('float32') / 255.0)

    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)
    delta = cmax - cmin

    # Hue
    H = np.zeros_like(cmax)
    mask = delta != 0
    idx = (cmax == r) & mask
    H[idx] = (60 * ((g[idx] - b[idx]) / delta[idx]) + 360) % 360
    idx = (cmax == g) & mask
    H[idx] = (60 * ((b[idx] - r[idx]) / delta[idx]) + 120) % 360
    idx = (cmax == b) & mask
    H[idx] = (60 * ((r[idx] - g[idx]) / delta[idx]) + 240) % 360
    H = (H / 2).astype('uint8')  # 0-179 にスケール

    # Saturation
    S = np.zeros_like(cmax)
    S[cmax != 0] = (delta[cmax != 0] / cmax[cmax != 0]) * 255
    S = S.astype('uint8')

    # Value
    V = (cmax * 255).astype('uint8')

    hsv = cv2.merge([H, S, V])
    return hsv

def get_colorplane(frame):
    # HSVグレースケール変換
    # library
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # 自作関数
    gray = rgb_to_hsv()

    # RGBグレースケール変換 cv2.COLOR_BGR2GRAY
    # cv2.COLOR_BGR2GRAY 輝度変換してる下記式
    # 輝度信号Y = 0.299・R+0.587・G+0.114・B
    # library
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 自作関数
    
    return gray

# カメラ初期呼び出し
cap = cv2.VideoCapture(0)

if input("Press enter to start operations...") == 'q':
    # 最初の1フレームを背景画像に設定
    ret, bg = cap.read()
    bg_frame = get_colorplane(bg)

if input("Press enter to start operations...") == 'w':
    # フレームの取得
    ret, frame = cap.read()
    fr_frame = get_colorplane(frame)

    # 差分の絶対値を計算 例題4
    diff = cv2.absdiff(fr_frame, bg_frame)
    # 自作関数
    #diff = img_diff(fr_frame, bg_frame)

    # 画像を表示
    cv2.imshow("backgrand", bg)
    cv2.imshow("Frame", frame)
    cv2.imshow("gray", diff)

    cv2.waitKey(0)

# 画像の保存

# カメラのリリース
cap.release()
cv2.destroyAllWindows()
