import os
import time
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"

import cv2

WIDTH = 1920
HEIGHT = 1080
FPS = 60

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

frame_count = 0
tmp = -1
end_time = time.perf_counter()
while (cap.isOpened()):
    ret, frame = cap.read()

    if tmp != int(frame):
        frame_count += 1

    cv2.imshow("Flame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(end_time / frame_count)
        break

cap.release()
cv2.destroyAllWindows()