# -*- coding: utf-8 -*-
# カラー差分画像を動画で表示するプログラム

import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import cv2

WIDTH = 640
HEIGHT = 480
FPS = 30

# カメラのキャッチャ
cap = cv2.VideoCapture(0)

# フォーマット・解像度・FPSの設定
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

# 最初のフレームを取得
ret, prev_frame = cap.read()
if not ret:
    print("カメラが見つかりません")
    cap.release()
    exit()

while True:
    # 現在のフレームを取得
    ret, frame = cap.read()
    if not ret:
        break

    # 差分（カラーのまま計算）
    diff = cv2.absdiff(frame, prev_frame)

    # 結果を表示
    cv2.imshow("Current Frame", frame)
    cv2.imshow("Difference", diff)

    # 次のループ用に現在フレームを保存
    prev_frame = frame.copy()

    # 'q'で終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 終了処理
cap.release()
cv2.destroyAllWindows()
