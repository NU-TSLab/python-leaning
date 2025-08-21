import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]="0"
import cv2
import time
print(cv2.__version__)
WIDTH = 1920
HEIGHT = 1080
FPS = 60

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

fps = cap.get(cv2.CAP_PROP_FPS)

count = 0

while (cap.isOpened()):
    ret = 0
    if not count == 0:
        latest_frame = frame

    while not ret:
        ret, frame = cap.read()

    if not count == 0:
        cv2.imshow("Diff", cv2.absdiff(latest_frame, frame))

    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()