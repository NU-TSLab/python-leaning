
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
count = -1

while (cap.isOpened()):    
    ret = 0
    while not ret:
        ret, frame = cap.read()
    cv2.imshow("Frame", frame)
    count += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        end = time.perf_counter()
        break

    if (count == 0):
        start = time.perf_counter()

cap.release()
print(f"実際のfps:{count / (end - start)}")
cv2.destroyAllWindows()
