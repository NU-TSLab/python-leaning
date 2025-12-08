import cv2
import os
import glob
import csv
import numpy as np
from PIL import Image, ImageOps
import easyocr

# ==== 設定 ====
VALID_SIGNS = {"10", "20", "30", "40", "50", "60", "70", "80"}
OUTPUT_CSV = "ocr_wrong_matches.csv"
TEMPLATE_FOLDER = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_number_temprate"

reader = easyocr.Reader(['en'], gpu=True)


# ==== 画像読み込み ====
def load_image_exif_corrected(path, gray=False):
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    img_np = np.array(img)

    if gray:
        if img_np.ndim == 2:
            return img_np
        if img_np.shape[2] == 4:
            img_np = cv2.cvtColor(img_np, cv2.COLOR_RGBA2RGB)
        return cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    else:
        if img_np.ndim == 2:
            return cv2.cvtColor(img_np, cv2.COLOR_GRAY2BGR)
        if img_np.shape[2] == 4:
            return cv2.cvtColor(img_np, cv2.COLOR_RGBA2BGR)
        return cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)


# ==== 明るさ・コントラスト補正 ====
def adjust_brightness_contrast(img, contrast=1.2):
    mean = np.mean(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
    beta = 128 - mean
    return cv2.convertScaleAbs(img, alpha=contrast, beta=beta)


# ==== 赤円形検出 ====
def detect_red_circles(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 60, 20])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 60, 20])
    upper_red2 = np.array([180, 255, 255])
    mask = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.medianBlur(mask, 5)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    circles = []

    for cnt in contours:
        if len(cnt) < 5:
            continue
        area = cv2.contourArea(cnt)
        if area < 3200:
            continue
        ellipse = cv2.fitEllipse(cnt)
        (x, y), (MA, ma), _ = ellipse
        r = max(MA, ma) / 2
        x1 = max(int(x - r), 0)
        y1 = max(int(y - r), 0)
        x2 = min(int(x + r), img.shape[1])
        y2 = min(int(y + r), img.shape[0])
        region = img[y1:y2, x1:x2]
        circles.append(region)
    return circles


# ==== テンプレート読み込み ====
def load_templates(template_dir):
    templates = {}
    exts = ("*.png", "*.PNG", "*.jpg", "*.JPG", "*.jpeg", "*.JPEG")
    for ext in exts:
        for path in glob.glob(os.path.join(template_dir, ext)):
            img = load_image_exif_corrected(path, gray=True)
            if img is not None:
                templates[os.path.basename(path)] = img
    print(f"Loaded {len(templates)} templates")
    return templates


# ==== テンプレートマッチング ====
def match_digit(part, templates, side="left"):
    best_score = -1
    best_name = None
    for name, tmpl in templates.items():
        tmpl_resized = cv2.resize(tmpl, (part.shape[1], part.shape[0]))
        res = cv2.matchTemplate(part, tmpl_resized, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)
        if max_val > best_score:
            best_score = max_val
            best_name = name
    return best_name, best_score


def template_match_two_digits(region, templates):
    """テンプレートマッチングで全ての赤円から、Left/Rightの最高スコア組を採用"""
    img_gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    h, w = img_gray.shape[:2]
    mid = w // 2
    left = img_gray[:, :mid]
    right = img_gray[:, mid:]

    left_name, left_score = match_digit(left, templates, side="left")
    right_name, right_score = match_digit(right, templates, side="right")

    if left_name and right_name:
        result = f"{left_name[0]}{right_name[0]}"
        total_score = (left_score + right_score) / 2
        return result, total_score
    return None, -1


# ==== 全体処理 ====
def process_images(image_folder, templates):
    image_files = glob.glob(os.path.join(image_folder, "*.jpg"))
    total, correct = 0, 0
    wrong_data = []

    for img_path in image_files:
        total += 1
        orig = load_image_exif_corrected(img_path, gray=False)
        if orig is None:
            continue

        adjusted = adjust_brightness_contrast(orig)
        candidate_regions = detect_red_circles(adjusted)
        if not candidate_regions:
            print(f"{os.path.basename(img_path)}: 赤領域なし")
            continue

        best_prediction = None
        best_score = -1
        best_region = None

        # 各赤円についてスコア最大の結果を採用
        for region in candidate_regions:
            result, score = template_match_two_digits(region, templates)
            if score > best_score:
                best_score = score
                best_prediction = result
                best_region = region

        if best_prediction is None:
            print(f"{os.path.basename(img_path)}: 認識失敗")
            continue

        print(f"\n対象画像: {os.path.basename(img_path)}")
        print(f"推定結果: {best_prediction}（スコア={best_score:.3f}）")

        # --- 認識結果の確認表示 ---
        scale = 600 / best_region.shape[1]
        display_resized = cv2.resize(best_region, (0, 0), fx=scale, fy=scale)
        cv2.imshow("認識対象", display_resized)

        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == ord('y'):
                correct += 1
                break
            elif key == ord('n'):
                wrong_data.append([img_path, best_prediction])
                break
            elif key == 27:  # ESCキー
                print("処理を中断しました。")
                cv2.destroyAllWindows()
                return

        cv2.destroyAllWindows()

    # --- 結果のCSV出力 ---
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["対象画像", "推定結果"])
        writer.writerows(wrong_data)

    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"\n総画像数: {total}, 正解数: {correct}, 正答率: {accuracy:.2f}%")
    print(f"誤判定データは {OUTPUT_CSV} に保存されました。")


# ==== 実行 ====
if __name__ == "__main__":
    templates = load_templates(TEMPLATE_FOLDER)
    process_images(
        r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic_2",
        templates
    )
