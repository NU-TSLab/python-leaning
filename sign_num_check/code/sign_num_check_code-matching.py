import cv2
import os
import glob
import csv
from PIL import Image, ImageOps
import numpy as np

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

def detect_red_white_circle(img, min_radius=15, min_wh=30):
    """
    赤円＋白円候補を抽出（赤円半径上位3つを返す）
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

    # 赤円半径で降順ソート
    candidates.sort(key=lambda x: x[0], reverse=True)
    top3 = candidates[:3]

    # 上位3つの赤円候補すべてを返す
    return [c[2] for c in top3]

def multi_template_matching(image_folder, template_folder, output_csv="wrong_matches_alldata.csv"):
    # テンプレート読み込み
    template_files = glob.glob(os.path.join(template_folder, "*.png"))
    templates = []
    for t_path in template_files:
        t_img = load_image_exif_corrected(t_path, gray=True)
        if t_img is None:
            continue
        templates.append((t_path, t_img))
        print(f"テンプレート: {os.path.basename(t_path)} サイズ={t_img.shape}")

    # シャープ化フィルタ（エッジ強調用）
    kernel_sharpen = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])

    # 対象画像
    image_files = glob.glob(os.path.join(image_folder, "*.jpg"))
    wrong_data = []
    total = 0
    correct = 0

    for img_path in image_files:
        total += 1
        orig = load_image_exif_corrected(img_path, gray=False)
        if orig is None:
            continue

        adjusted = adjust_brightness_contrast(orig)
        candidate_regions = detect_red_white_circle(adjusted, min_radius=15, min_wh=30)
        if not candidate_regions:
            print(f"{os.path.basename(img_path)}: 赤円＋白円が検出されませんでした")
            continue

        best_score = -1
        best_template_name = None
        best_loc = None
        best_size = None
        best_region = None

        # 上位3つすべての赤円候補領域でテンプレートマッチング
        for idx, region in enumerate(candidate_regions):
            # --- エッジ強調 ---
            gray_region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)
            gray_region = cv2.filter2D(gray_region, -1, kernel_sharpen)

            rh, rw = gray_region.shape[:2]
            for t_path, template in templates:
                # テンプレートを候補領域サイズにリサイズ
                resized_template = cv2.resize(template, (rw, rh))
                th, tw = resized_template.shape[:2]

                result = cv2.matchTemplate(gray_region, resized_template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(result)

                print(f"候補 {idx+1}, テンプレート {os.path.basename(t_path)}, スコア={max_val:.4f}")

                if max_val > best_score:
                    best_score = max_val
                    best_template_name = os.path.basename(t_path)
                    best_loc = max_loc
                    best_size = (tw, th)
                    best_region = region

        if best_template_name is None:
            print(f"{os.path.basename(img_path)}: マッチング不可")
            continue

        print(f"\n対象画像: {os.path.basename(img_path)}")
        print(f"最良テンプレート: {best_template_name}, スコア: {best_score:.4f}")

        display_img = best_region.copy()
        top_left = best_loc
        bottom_right = (top_left[0]+best_size[0], top_left[1]+best_size[1])
        cv2.rectangle(display_img, top_left, bottom_right, (0,0,255), 2)

        scale = 600 / display_img.shape[1]
        display_resized = cv2.resize(display_img, (0,0), fx=scale, fy=scale)
        cv2.imshow("Matched Result", display_resized)

        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == ord('y'):
                correct += 1
                break
            elif key == ord('n'):
                wrong_data.append([img_path, best_template_name, f"{best_score:.4f}"])
                break
            elif key == 27:
                print("処理を中断しました。")
                cv2.destroyAllWindows()
                return

        cv2.destroyAllWindows()

    # CSV保存
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["対象画像", "選ばれたテンプレート", "スコア"])
        writer.writerows(wrong_data)

    accuracy = (correct / total) * 100 if total > 0 else 0
    print(f"\n総画像数: {total}, 正解数: {correct}, 正答率: {accuracy:.2f}%")
    print(f"誤判定データは {output_csv} に保存されました。")


# 使用例
multi_template_matching(
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic_2",
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_temprate"
)
