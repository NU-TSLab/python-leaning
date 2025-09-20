import cv2
import numpy as np
import glob
import os
from PIL import Image, ImageOps

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
    """
    赤色領域をマスクして標識候補を抽出する
    """
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # --- 夜間も考慮した赤色範囲 ---
    lower_red1 = np.array([0, 60, 20])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 60, 20])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)

    # ノイズ除去
    red_mask = cv2.medianBlur(red_mask, 5)

    # 輪郭検出
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    candidates = []
    ellipses = []

    for cnt in contours:
        if len(cnt) < 5:
            continue
        area = cv2.contourArea(cnt)
        if area < 6400:  # 小さいノイズは除去
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

    return candidates, ellipses, red_mask


# --- メイン処理 ---
image_folder = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic"
mask_save_folder = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic_template_mask"

os.makedirs(mask_save_folder, exist_ok=True)

image_files = glob.glob(f"{image_folder}/*.jpg")

for img_path in image_files:
    img = load_image_exif_corrected(img_path)
    display_img = resize_for_display(img)

    candidate_regions, ellipses, red_mask = detect_red_sign_candidates(img)

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
    cv2.waitKey(0)

    # マスクも表示
    mask_display = resize_for_display(red_mask)
    cv2.imshow("Red Mask", mask_display)
    cv2.waitKey(0)

    # マスク保存（二値化画像）
    base_name = os.path.splitext(os.path.basename(img_path))[0]
    save_path = os.path.join(mask_save_folder, f"{base_name}_mask.png")
    cv2.imwrite(save_path, red_mask)

cv2.destroyAllWindows()