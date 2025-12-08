import cv2
import numpy as np
import os
import glob
from PIL import Image, ImageOps

# ==== 設定 ====
INPUT_DIR = "python-leaning\sign_num_check\pattern_matching"        # 入力画像フォルダ
TEMPLATE_DIR = "python-leaning\sign_num_check\pattern_matching_number_temprate" # テンプレート画像フォルダ


# ==== 画像読み込み関数 ====
def load_image_exif_corrected(path, gray=False):
    """Exifを補正して画像を読み込む"""
    img = Image.open(path)
    img = ImageOps.exif_transpose(img)
    img_np = np.array(img)

    if gray:
        if img_np.ndim == 2:
            return img_np
        return cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    else:
        return cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)


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


# ==== マッチング処理 ====
def match_digit(part, templates, side="left"):
    best_score = -1
    best_name = None

    for name, tmpl in templates.items():
        # part と tmpl を同じ大きさにリサイズ
        tmpl_resized = cv2.resize(tmpl, (part.shape[1], part.shape[0]))

        res = cv2.matchTemplate(part, tmpl_resized, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(res)

        if max_val > best_score:
            best_score = max_val
            best_name = name

    print(f"{side} -> {best_name}, score={best_score:.3f}")
    return best_name, best_score


def match_templates_in_region(img_gray, region, templates):
    x, y, w, h = region
    roi = img_gray[y:y+h, x:x+w]

    mid = w // 2
    left = roi[:, :mid]
    right = roi[:, mid:]

    left_name, left_score = match_digit(left, templates, side="left")
    right_name, right_score = match_digit(right, templates, side="right")

    return (left_name, left_score), (right_name, right_score)


# ==== メイン処理 ====
if __name__ == "__main__":
    # テンプレート読み込み
    templates = load_templates(TEMPLATE_DIR)

    # 入力画像の読み込み
    input_files = []
    for ext in ("*.png", "*.PNG", "*.jpg", "*.JPG", "*.jpeg", "*.JPEG"):
        input_files.extend(glob.glob(os.path.join(INPUT_DIR, ext)))

    print(f"Found {len(input_files)} input images")

    total = 0
    correct = 0

    # 各画像に対してマッチング
    for path in input_files:
        img_gray = load_image_exif_corrected(path, gray=True)

        # ==== 矩形領域（仮置き）====
        # 実際のデータに合わせて修正してください
        h, w = img_gray.shape[:2]
        region = (w//4, h//4, w//2, h//2)  # 中央部分を仮に切り出す

        print(f"\nProcessing {os.path.basename(path)}")
        (l_name, l_score), (r_name, r_score) = match_templates_in_region(img_gray, region, templates)

        if l_name is None or r_name is None:
            print(f"{os.path.basename(path)}: 認識失敗")
            continue

        result = f"{l_name[0]}{r_name[0]}"  # ファイル名の先頭文字を数字とみなす例
        print(f"推定結果: {result}  （left={l_name}, right={r_name}）")

        # ==== 正誤判定 ====
        while True:
            ans = input("この結果は正しいですか？ (y/n): ").strip().lower()
            if ans in ("y", "n"):
                break
        total += 1
        if ans == "y":
            correct += 1

    # ==== 集計結果 ====
    if total > 0:
        accuracy = correct / total * 100
        print(f"\n正答率: {correct}/{total} = {accuracy:.2f}%")
    else:
        print("処理対象がありませんでした。")
