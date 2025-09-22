import cv2
import numpy as np
import glob
import os
from PIL import Image, ImageOps
import csv

def load_image_exif_corrected(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def resize_for_display(img, max_size=600):
    h, w = img.shape[:2]
    scale = min(max_size / max(h, w), 1.0)
    if scale < 1.0:
        img = cv2.resize(img, (int(w * scale), int(h * scale)))
    return img

def detect_red_sign_candidates(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 60, 0])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 60, 0])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    red_mask = cv2.medianBlur(red_mask, 5)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    ellipses = []

    for cnt in contours:
        if len(cnt) < 5:
            continue
        area = cv2.contourArea(cnt)
        if area < 3200:
            continue

        ellipse = cv2.fitEllipse(cnt)
        ellipses.append(ellipse)

        (x, y), (MA, ma), angle = ellipse
        r = max(MA, ma) / 2
        x1 = max(int(x - r), 0)
        y1 = max(int(y - r), 0)
        x2 = min(int(x + r), img.shape[1])
        y2 = min(int(y + r), img.shape[0])

        candidate = img[y1:y2, x1:x2]
        candidates.append(candidate)

    return candidates, ellipses

# --- メイン処理 ---
image_folder = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic"
csv_path = "red_sign_labels.csv"
os.makedirs(image_folder, exist_ok=True)

image_files = glob.glob(f"{image_folder}/*.jpg")
results = []

for img_path in image_files:
    img = load_image_exif_corrected(img_path)
    display_img = resize_for_display(img)

    _, ellipses = detect_red_sign_candidates(img)

    # 検出結果を表示
    vis = display_img.copy()
    scale_x = vis.shape[1] / img.shape[1]
    scale_y = vis.shape[0] / img.shape[0]
    for ellipse in ellipses:
        (x, y), (MA, ma), angle = ellipse
        cv2.ellipse(
            vis,
            (int(x * scale_x), int(y * scale_y)),
            (int(MA * scale_x / 2), int(ma * scale_y / 2)),
            angle,
            0, 360,
            (0, 255, 0), 2
        )

    cv2.imshow("Detected Candidates", vis)

    # キーボード入力でラベル付け
    key = cv2.waitKey(0)
    if key in (ord('y'), ord('Y')):
        results.append((os.path.basename(img_path), 'y'))
    else:
        results.append((os.path.basename(img_path), 'n'))

cv2.destroyAllWindows()

# CSVに保存
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["filename", "label"])
    writer.writerows(results)

# 正答率計算
y_count = sum(1 for _, label in results if label == 'y')
accuracy = y_count / len(results) if results else 0
print(f"正答率: {accuracy:.2%} ({y_count}/{len(results)})")
