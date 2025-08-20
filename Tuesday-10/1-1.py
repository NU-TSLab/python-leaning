import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"]="0"
import cv2
WIDTH = 800
HEIGHT = 600
FPS = 60

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"width:{width}, height:{height}, fps:{fps}")

ret, frame = cap.read()

cv2.imshow("Frame", frame)
cv2.waitKey(0)

if ret:
    cv2.imwrite("picture.jpeg", frame)

jpeg_size = os.path.getsize("picture.jpeg")
print(f"jpegのサイズ:{jpeg_size}byte，そのままの画像のサイズ:{int(width *  height * 3)}byte")
print(f"圧縮率:{((jpeg_size/(width *  height * 3)) * 100):.2f}%")
cap.release()
cv2.destroyAllWindows()
