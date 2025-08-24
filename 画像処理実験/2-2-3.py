import cv2
import numpy as np

# カメラ起動
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # HSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 範囲を定義
    color_ranges = {
        "red":   [(0, 120, 70), (10, 255, 255), (170, 120, 70), (180, 255, 255)],
        "blue":  [(100, 100, 0), (140, 255, 255)]
    }

    total_count = 0

    for color, ranges in color_ranges.items():
        if color == "red":
            mask1 = cv2.inRange(hsv, ranges[0], ranges[1])
            mask2 = cv2.inRange(hsv, ranges[2], ranges[3])
            mask = mask1 | mask2
        else:
            mask = cv2.inRange(hsv, ranges[0], ranges[1])

        # ノイズ除去
        mask = cv2.medianBlur(mask, 5)

        # 輪郭検出
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # 輪郭描画
        draw_color = {
            "red": (0, 0, 255),
            "blue": (255, 0, 0)
        }[color]
        cv2.drawContours(frame, contours, -1, draw_color, 2)

        # 検出数カウント
        count = len(contours)

        # 色ごとの数を表示
        cv2.putText(frame, f"{color}: {count}", (10, 50 + 30*list(color_ranges.keys()).index(color)),cv2.FONT_HERSHEY_SIMPLEX, 0.8, draw_color, 2)

    # 表示
    cv2.imshow("color_count", frame)

    # 保存
    if cv2.waitKey(1) & 0xFF == ord('q'):
        result = cv2.imwrite("2-2color.jpg", frame)
        print("保存結果:", result)

    elif cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
