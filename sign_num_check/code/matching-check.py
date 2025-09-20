import cv2
import numpy as np
import glob
from PIL import Image, ImageOps

def load_image_exif_corrected(path):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

def detect_red_white_circle_top3(img, min_radius=15, min_wh=30):
    """
    赤円＋白円候補を抽出し、赤円半径が大きい順の上位3つを返す
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 赤色検出
    lower1 = np.array([0, 70, 50])
    upper1 = np.array([10, 255, 255])
    lower2 = np.array([170, 70, 50])
    upper2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower1, upper1)
    mask2 = cv2.inRange(hsv, lower2, upper2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    red_mask = cv2.medianBlur(red_mask, 5)

    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidates = []

    for cnt in contours:
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        if radius < min_radius:
            continue
        x, y, r = int(x), int(y), int(radius)
        x1 = max(x - r, 0)
        y1 = max(y - r, 0)
        x2 = min(x + r, img.shape[1])
        y2 = min(y + r, img.shape[0])
        if (x2 - x1) < min_wh or (y2 - y1) < min_wh:
            continue

        red_region = img[y1:y2, x1:x2]

        # 内側白円の存在確認
        hsv_region = cv2.cvtColor(red_region, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 180])
        upper_white = np.array([180, 40, 255])
        white_mask = cv2.inRange(hsv_region, lower_white, upper_white)
        white_ratio = cv2.countNonZero(white_mask) / (white_mask.shape[0] * white_mask.shape[1])

        candidates.append((r, white_ratio, red_region))

    if not candidates:
        return []

    # 赤円半径で降順ソートして上位3つを返す
    candidates.sort(key=lambda x: x[0], reverse=True)
    top3 = candidates[:3]
    return [c[2] for c in top3]  # 画像部分だけ返す

# --- テスト実行 ---
image_folder = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic_2"
image_files = glob.glob(f"{image_folder}/*.jpg")

for img_path in image_files:
    img = load_image_exif_corrected(img_path)
    candidate_regions = detect_red_white_circle_top3(img)
    if not candidate_regions:
        print(f"{img_path}: 赤円＋白円が検出されませんでした")
        continue

    for idx, region in enumerate(candidate_regions):
        cv2.imshow(f"{img_path} - Candidate {idx+1}", region)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

