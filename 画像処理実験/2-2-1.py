import cv2
import numpy as np

# カメラを起動
cap = cv2.VideoCapture(0)

# フレーム取得
ret, frame1 = cap.read()

while True:
    # 次のフレームを取得
    ret, frame2 = cap.read()

    # 差分計算
    diff = cv2.absdiff(frame1, frame2)

    # 表示
    cv2.imshow("2", diff)

    #更新
    frame1 = frame2

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()