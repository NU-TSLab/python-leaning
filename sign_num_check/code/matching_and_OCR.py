import cv2
import os
import glob
import csv
import numpy as np
from PIL import Image, ImageOps
import easyocr

# ==== 設定 ====
VALID_SIGNS = {"10","20","30","40","50","60","70","80"}
OUTPUT_CSV = "ocr_wrong_matches.csv"
TEMPLATE_FOLDER = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_number_temprate"

# OCRリーダー
reader = easyocr.Reader(['en'], gpu=True)   # GPU不要なら gpu=False

# テンプレート読み込み（1桁用）
templates = {}
for file_path in glob.glob(os.path.join(TEMPLATE_FOLDER, "*.jpg")):
    name = os.path.splitext(os.path.basename(file_path))[0]
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    templates[name] = img

# ==== 画像前処理 ====
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
        (x, y), (MA, ma), angle = ellipse
        r = max(MA, ma) / 2
        x1 = max(int(x - r), 0)
        y1 = max(int(y - r), 0)
        x2 = min(int(x + r), img.shape[1])
        y2 = min(int(y + r), img.shape[0])
        region = img[y1:y2, x1:x2]
        circles.append(region)
    return circles

# ==== OCR ====
def ocr_on_region(region):
    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    results = reader.readtext(gray, detail=0)
    filtered = [txt for txt in results if txt.isdigit() and txt in VALID_SIGNS]
    return " ".join(filtered)

# ==== テンプレートマッチング（2桁対応） ====
def template_match_two_digits(region, show_crop=True):
    """
    1桁テンプレートでスライディングマッチングを行い、2桁数字を判定
    デバッグ用に矩形・スコアを表示
    """
    gray = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape

    # 中心領域 縦3/7 × 横5/7
    cx, cy = w // 2, h // 2
    rh, rw = int(h * 5 / 7 / 2), int(w * 3 / 7 / 2)
    x1, y1 = cx - rw, cy - rh
    x2, y2 = cx + rw, cy + rh
    cropped = gray[y1:y2, x1:x2].copy()

    if show_crop:
        display = region.copy()
        cv2.rectangle(display, (x1, y1), (x2, y2), (0, 255, 0), 2)
        scale = 600 / display.shape[1]
        cv2.imshow("3x5/7 Crop Area", cv2.resize(display, (0, 0), fx=scale, fy=scale))

    threshold = 0.02
    detected_digits = []
    positions = []
    search_region = cropped.copy()

    while len(detected_digits) < 2:
        best_score = 0
        best_name = None
        best_pos = None

        for name, tmpl in templates.items():
            res = cv2.matchTemplate(search_region, tmpl, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > best_score:
                best_score = max_val
                best_name = name
                best_pos = max_loc

        if best_score < threshold:
            break

        detected_digits.append(best_name)
        positions.append((best_pos, best_name, best_score))

        # 見つけたテンプレートの右側から次を探索
        tmpl_w = templates[best_name].shape[1]
        x, y = best_pos
        search_region = search_region[:, x + tmpl_w:]

    # デバッグ表示：検出矩形とスコア
    if show_crop:
        debug_display = cropped.copy()
        debug_display = cv2.cvtColor(debug_display, cv2.COLOR_GRAY2BGR)
        offset_x = 0
        for pos, name, score in positions:
            px, py = pos
            w_t, h_t = templates[name].shape[1], templates[name].shape[0]
            top_left = (px + offset_x, py)
            bottom_right = (px + offset_x + w_t, py + h_t)
            cv2.rectangle(debug_display, top_left, bottom_right, (0, 255, 0), 2)
            cv2.putText(debug_display, f"{name}:{score:.2f}", (top_left[0], top_left[1]-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            offset_x += w_t
        cv2.imshow("Template Matching Debug", cv2.resize(debug_display, (0,0), fx=2, fy=2))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    if len(detected_digits) == 2:
        combined = "".join(detected_digits)
        if combined in VALID_SIGNS:
            return combined
    return None

# ==== 画像処理全体 ====
def process_images(image_folder):
    image_files = glob.glob(os.path.join(image_folder, "*.jpg"))
    total = 0
    correct = 0
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

        prediction = None
        used_region = None

        # OCRで判定
        for region in candidate_regions:
            text = ocr_on_region(region)
            if text:
                prediction = text
                used_region = region
                break

        # OCRで見つからなければテンプレートマッチング
        if prediction is None:
            for region in candidate_regions:
                text = template_match_two_digits(region, show_crop=True)
                if text:
                    prediction = text
                    used_region = region
                    break

        if prediction is None:
            print(f"{os.path.basename(img_path)}: 認識失敗")
            continue

        print(f"\n対象画像: {os.path.basename(img_path)}")
        print(f"推定結果: {prediction}")

        # 確認用表示
        scale = 600 / used_region.shape[1]
        display_resized = cv2.resize(used_region, (0, 0), fx=scale, fy=scale)
        cv2.imshow("Candidate", display_resized)

        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == ord('y'):
                correct += 1
                break
            elif key == ord('n'):
                wrong_data.append([img_path, prediction])
                break
            elif key == 27:
                print("処理を中断しました。")
                cv2.destroyAllWindows()
                return

        cv2.destroyAllWindows()

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["対象画像", "推定結果"])
        writer.writerows(wrong_data)

    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"\n総画像数: {total}, 正解数: {correct}, 正答率: {accuracy:.2f}%")
    print(f"誤判定データは {OUTPUT_CSV} に保存されました。")

# ==== 実行例 ====
process_images(
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic_2"
)
