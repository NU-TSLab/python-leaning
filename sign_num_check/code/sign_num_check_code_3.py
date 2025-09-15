import cv2
import numpy as np
import os

def extract_sign_by_red(img, file, debug=False):
    """赤枠を利用して標識を抽出する"""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 赤色の範囲（調整可能）
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    # ノイズ除去（調整可能：カーネルサイズ）
    morph_kernel = np.ones((5,5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, morph_kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, morph_kernel)

    # 輪郭検出
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        print(f"赤枠検出失敗: {file}")
        return None

    c = max(contours, key=cv2.contourArea)
    if len(c) < 5:
        print(f"楕円フィット不可: {file}")
        return None

    # 楕円フィット
    ellipse = cv2.fitEllipse(c)
    (x, y), (MA, ma), angle = ellipse
    x1, y1 = int(x - MA/2), int(y - ma/2)
    x2, y2 = int(x + MA/2), int(y + ma/2)

    # 切り出し
    h_img, w_img = img.shape[:2]
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(w_img, x2), min(h_img, y2)
    cropped = img[y1:y2, x1:x2]

    # マスクで外を白塗り
    mask_cropped = np.zeros(cropped.shape[:2], dtype=np.uint8)
    shifted_c = c - [x1, y1]
    cv2.drawContours(mask_cropped, [shifted_c], -1, 255, -1)

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
    templ = np.full_like(gray, 255)
    templ[mask_cropped == 255] = gray[mask_cropped == 255]

    if debug:
        cv2.imshow("mask", mask)
        cv2.imshow("templ", templ)
        cv2.waitKey(0)

    return templ

def create_templates(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if not file.lower().endswith(".jpg"):
            continue

        path = os.path.join(input_dir, file)
        img = cv2.imread(path)
        if img is None:
            print(f"読み込み失敗: {path}")
            continue

        templ = extract_sign_by_red(img, file)
        if templ is not None:
            save_path = os.path.join(output_dir, file)
            cv2.imwrite(save_path, templ)
            print(f"保存完了: {save_path}")

if __name__ == "__main__":
    input_dir = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching"
    output_dir = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_temprate"
    create_templates(input_dir, output_dir)
