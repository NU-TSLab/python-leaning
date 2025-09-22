import cv2
import numpy as np
import os
import glob

def perspective_skew(img, skew_type="right"):
    """
    正面画像を斜め視点に変換
    skew_type: "right", "left", "top", "bottom"
    """
    h, w = img.shape[:2]

    src_pts = np.float32([[0,0],[w,0],[0,h],[w,h]])

    if skew_type == "right":
        dst_pts = np.float32([[0,0],[w*0.8, h*0.1],[0, h],[w*0.9, h*0.9]])
    elif skew_type == "left":
        dst_pts = np.float32([[w*0.2, h*0.1],[w,0],[w*0.1,h*0.9],[w,h]])
    elif skew_type == "top":
        dst_pts = np.float32([[0,h*0.2],[w,h*0.1],[0,h],[w,h]])
    elif skew_type == "bottom":
        dst_pts = np.float32([[0,0],[w,0],[0,h*0.9],[w,h*0.8]])
    else:
        dst_pts = src_pts

    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(img, M, (w,h), borderValue=255)
    return warped

def generate_variations_from_folder(input_dir, output_dir="output", ksize=3):
    """
    回転・縦方向スキュー・斜め視点変換を組み合わせて
    テンプレートマッチング用画像を生成
    """
    os.makedirs(output_dir, exist_ok=True)
    files = glob.glob(os.path.join(input_dir, "*.png")) + glob.glob(os.path.join(input_dir, "*.jpg"))
    if not files:
        raise FileNotFoundError(f"{input_dir} に PNG/JPG ファイルが見つかりません。")

    angles = [-10, 0, 10]        # 回転
    scales = [1.0]
    skew_y_factors = [1.0, 1.25, 1.5, 1.75, 2.0]
    perspective_types = ["right", "left", "top", "bottom"]

    kernel_sharpen = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])

    total_count = 0
    for file_path in files:
        filename = os.path.splitext(os.path.basename(file_path))[0]
        img = cv2.imread(file_path)
        if img is None:
            print(f"読み込み失敗: {file_path}")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        count = 0

        for scale in scales:
            base_w = int(gray.shape[1] * scale)
            base_h = int(gray.shape[0] * scale)
            resized = cv2.resize(gray, (base_w, base_h), interpolation=cv2.INTER_LINEAR)

            for skew_y in skew_y_factors:
                skewed_h = int(resized.shape[0] * skew_y)
                skewed_w = resized.shape[1]
                skewed = cv2.resize(resized, (skewed_w, skewed_h), interpolation=cv2.INTER_LINEAR)

                for perspective_type in perspective_types:
                    warped = perspective_skew(skewed, skew_type=perspective_type)

                    extra_w = int(warped.shape[1] * 0.3)
                    extra_h = int(warped.shape[0] * 0.1)
                    canvas = np.ones((warped.shape[0]+extra_h, warped.shape[1]+extra_w), dtype=warped.dtype)*255
                    start_x = extra_w // 2
                    start_y = extra_h // 2
                    canvas[start_y:start_y+warped.shape[0], start_x:start_x+warped.shape[1]] = warped

                    for angle in angles:
                        center = ((canvas.shape[1])//2, (canvas.shape[0])//2)
                        M = cv2.getRotationMatrix2D(center, angle, 1.0)
                        rotated = cv2.warpAffine(canvas, M, (canvas.shape[1], canvas.shape[0]),
                                                 flags=cv2.INTER_LINEAR,
                                                 borderMode=cv2.BORDER_CONSTANT,
                                                 borderValue=255)
                        denoised = cv2.medianBlur(rotated, ksize)
                        sharpened = cv2.filter2D(denoised, -1, kernel_sharpen)

                        out_name = f"{filename}_ang{angle}_sky{skew_y}_persp{perspective_type}.png"
                        out_path = os.path.join(output_dir, out_name)
                        cv2.imwrite(out_path, sharpened)
                        count += 1
                        total_count += 1

        print(f"{filename}: {count} 枚生成")
    print(f"合計 {total_count} 枚を {output_dir} に保存しました。")

# 使用例
generate_variations_from_folder(
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_number_temprate_base",
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_number_temprate",
    ksize=3
)
