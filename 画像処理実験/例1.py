# coding: utf-8
# 例題1 カメラの画像を取得する
import os
os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
# opencvライブラリのインポート
import cv2

WIDTH = 800
HEIGHT = 600
FPS = 60

def decode_fourcc(v):
    v = int(v)
    return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

# カメラのキャプチャ
cap = cv2.VideoCapture(0)

# フォーマット・解像度・FPSの設定
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

# フォーマット・解像度・FPSの取得
fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps    = cap.get(cv2.CAP_PROP_FPS)

# フレームの取得
ret, frame = cap.read()

# 画像を表示
cv2.imshow("Frame", frame)
cv2.waitKey(5000)

# 画像の保存及び結果確認
result = cv2.imwrite("rei1.jpg", frame)
print("保存結果:", result)

print(f"カメラ設定: {fourcc}, {width}x{height}, {fps}fps")

#カメラのリリース
cap.release()

# ファイルサイズの比較
print("取り込んだ画像:", frame.nbytes, "bytes")
filesize = os.path.getsize("rei1.jpg")
print("出力した画像:", filesize, "bytes")





#解像度変更
WIDTH = 1200
HEIGHT = 900
FPS = 60

# カメラのキャプチャ
cap = cv2.VideoCapture(0)

# フォーマット・解像度・FPSの設定
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

# フォーマット・解像度・FPSの取得
fourcc = decode_fourcc(cap.get(cv2.CAP_PROP_FOURCC))
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps    = cap.get(cv2.CAP_PROP_FPS)

# フレームの取得
ret, frame = cap.read()

# 画像を表示
cv2.imshow("Frame", frame)
cv2.waitKey(5000)

# 画像の保存及び結果確認
result = cv2.imwrite("rei1kai.jpg", frame)
print("保存結果:", result)


#カメラのリリース
cap.release()
cv2.destroyAllWindows()

print(f"カメラ設定: {fourcc}, {width}x{height}, {fps}fps")

# ファイルサイズの比較
print("取り込んだ画像(解像度変更):", frame.nbytes, "bytes")
filesize = os.path.getsize("rei1kai.jpg")
print("出力した画像(解像度変更):", filesize, "bytes")