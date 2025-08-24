import cv2

# カメラを起動
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # グレースケール
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2値化
    _, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

    # 輪郭を検出
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 輪郭を描画
    cv2.drawContours(frame, contours, -1, (0, 0, 255), 2)

    # 輪郭の数
    count = len(contours)
    cv2.putText(frame, f"Count: {count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)

    # 表示
    cv2.imshow("Binary", binary)
    cv2.imshow("Original", frame)

    # 保存
    if cv2.waitKey(1) & 0xFF == ord('q'):
        result = cv2.imwrite("2-2black.jpg", binary)
        print("保存結果:", result)

    # 終了
    elif cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
