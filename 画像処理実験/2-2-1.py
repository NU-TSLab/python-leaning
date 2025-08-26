import cv2
import numpy as np

cap = cv2.VideoCapture(0)

ret, background = cap.read()

while True:
    ret, frame = cap.read()

    #背景差分
    diff = cv2.absdiff(background, frame)

    #グレースケール化
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    #マスク
    _, mask = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    mask_3ch = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    #論理和
    moving = cv2.bitwise_and(frame, mask_3ch)

    #表示
    cv2.imshow("moving", moving)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()



