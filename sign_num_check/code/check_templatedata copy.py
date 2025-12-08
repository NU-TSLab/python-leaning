import cv2
import numpy as np
import os
import glob
from PIL import Image, ImageOps

# ==== 設定 ====
INPUT_DIR = "python-leaning\\sign_num_check\\pattern_matching"        # 入力画像フォルダ
TEMPLATE_DIR = "python-leaning\\sign_num_check\\pattern_matching_number_temprate" # テンプレート画像フォルダ


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


# ==== 楕円補正 ====
def correct_ellipse_to_circle(img_gray, ellipse):
    """
    楕円領域を円形に補正する
    ellipse: (center, axes, angle)
        center: (x, y)
        axes: (major_axis_length, minor_axis_length)
        angle: 回転角（OpenCVのellipseフィット形式）
    """
    (cx, cy), (major, minor), angle = ellipse

    # 出力サイズを長軸長に合わせる
    size = int(max(major, minor))
    if size <= 0:
        return None

    # 楕円を水平にするよう回転補正
    M_rot = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)
    img_rot = cv2.warpAffine(img_gray, M_rot, (img_gray.shape[1], img_gray.shape[0]))

    # 回転後の楕円領域を矩形で切り出す
    x1 = int(cx - major / 2)
    y1 = int(cy - minor / 2)
    x2 = int(cx + major / 2)
    y2 = int(cy + minor / 2)

    # 範囲チェック
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(img_gray.shape[1], x2)
    y2 = min(img_gray.shape[0], y2)

    rect_roi = img_rot[y1:y2, x1:x2]
    if rect_roi.size == 0:
        return None

    # 縦横比を補正して正円に
    corrected = cv2.resize(rect_roi, (size, size))
    return corrected


def detect_and_correct_ellipse(img_gray):
    """
    楕円領域を検出して正円補正を行う。
    戻り値: 補正後のグレースケール画像 or None
    """
    # 2値化
    _, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # 輪郭検出
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        print("楕円検出失敗（輪郭なし）")
        return None

    # 最大面積の輪郭を使用（標識などを想定）
    c = max(contours, key=cv2.contourArea)
    if len(c) < 5:
        print("楕円近似不可（点が少なすぎる）")
        return None

    ellipse = cv2.fitEllipse(c)
    corrected = correct_ellipse_to_circle(img_gray, ellipse)
    return corrected


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

    for path in input_files:
        img_gray = load_image_exif_corrected(path, gray=True)
        print(f"\nProcessing {os.path.basename(path)}")

        # ==== 楕円補正 ====
        corrected = detect_and_correct_ellipse(img_gray)
        if corrected is None:
            print("楕円補正に失敗しました。スキップします。")
            continue

        # ==== 補正結果を表示 ====
        cv2.imshow("Original", img_gray)
        cv2.imshow("Corrected (Circle)", corrected)
        print("補正結果を確認してください。何かキーを押すと次へ進みます。")
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # ==== マッチング処理 ====
        h, w = corrected.shape[:2]
        region = (w // 4, h // 4, w // 2, h // 2)

        (l_name, l_score), (r_name, r_score) = match_templates_in_region(corrected, region, templates)

        if l_name is None or r_name is None:
            print(f"{os.path.basename(path)}: 認識失敗")
            continue

        result = f"{l_name[0]}{r_name[0]}"
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
