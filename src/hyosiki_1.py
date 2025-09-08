import cv2
import numpy as np
import os

# フルパスで指定
path = r"C:\Users\ykimt\Documents\8-5github\python-leaning-2\IMG_hyoshiki_all\IMG_hyoshiki3_b.jpeg"



# ファイル存在確認
if not os.path.exists(path):
    print("ファイルが存在しません:", path)
    exit()

# 画像を読み込み
img = cv2.imread(path)

# --- 読み込み失敗時の処理 ---
if img is None:
    print("読み込み失敗: None")
    exit()  # プログラムを終了

# BGRからHSVに変換
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 青色の範囲を指定 (調整可能)
lower_blue = np.array([100, 150, 0])   # H=100, S=150, V=0
upper_blue = np.array([140, 255, 255]) # H=140, S=255, V=255

# 青マスクを作成
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 青い部分を抽出
blue_only = cv2.bitwise_and(img, img, mask=mask)

# 結果を表示
cv2.imshow("Blue Mask", mask)       # 白黒のマスク画像
cv2.imshow("Blue Only", blue_only)  # 抽出した青部分

cv2.waitKey(0)
cv2.destroyAllWindows()