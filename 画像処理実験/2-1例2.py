# -*- coding: utf-8 -*-
# 例題2　カメラの画像を取得して動画として表示させる
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
# opencvライブラリのインポート
import cv2

WIDTH = 1920
HEIGHT = 1080
FPS = 60

# カメラのキャプチャ
cap = cv2.VideoCapture(0)

# フォーマット・解像度・FPSの設定
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

while(cap.isOpened()):
    # フレームの取得
    ret, frame = cap.read()

    # 画像を表示
    cv2.imshow("Flame", frame)

    # qキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Actual resolution: {int(width)}x{int(height)}")
print("Actual FPS:", cap.get(cv2.CAP_PROP_FPS))

FPS = 15
WIDTH = 500
HEIGHT = 200

cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

while(cap.isOpened()):
    # フレームの取得
    ret, frame = cap.read()

    # 画像を表示
    cv2.imshow("Flame", frame)

    # qキーが押されたら途中終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"Actual resolution: {int(width)}x{int(height)}")
print("Actual FPS:", cap.get(cv2.CAP_PROP_FPS))

# カメラのリリース
cap.release()
cv2.destroyAllWindows()
