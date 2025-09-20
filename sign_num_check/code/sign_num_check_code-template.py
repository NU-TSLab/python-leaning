import cv2
import numpy as np
import os
import glob

def generate_variations_from_folder(input_dir, output_dir="output", ksize=3):
    """
    指定フォルダ内のPNG/JPG画像に対して、回転・拡大縮小・縦方向の傾斜を行い、
    グレースケール化＋MedianBlur＋エッジ強調でノイズ除去した画像を保存する。
    """

    # 出力先ディレクトリ作成
    os.makedirs(output_dir, exist_ok=True)

    # フォルダ内のPNG/JPGファイル一覧取得
    files = glob.glob(os.path.join(input_dir, "*.png")) + glob.glob(os.path.join(input_dir, "*.jpg"))
    if not files:
        raise FileNotFoundError(f"{input_dir} に PNG/JPG ファイルが見つかりません。")

    # 回転角度、倍率、縦方向の傾斜の組み合わせ
    angles = [-20, 0, 20]        # 回転
    scales = [1.0]               # 拡大縮小
    skew_y_factors = [1.0, 1.25, 1.5, 2.0, 2.5]  # 縦方向の傾斜
    skew_x = 1.0  # 横方向は固定

    # シャープ化フィルタ
    kernel_sharpen = np.array([[0, -1, 0],
                               [-1, 5, -1],
                               [0, -1, 0]])

    total_count = 0
    for file_path in files:
        filename = os.path.splitext(os.path.basename(file_path))[0]

        # 画像読み込み
        img = cv2.imread(file_path)
        if img is None:
            print(f"読み込み失敗: {file_path}")
            continue

        # グレースケール化
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        count = 0
        for scale in scales:
            # 基本リサイズ
            base_w = int(gray.shape[1] * scale)
            base_h = int(gray.shape[0] * scale)
            resized = cv2.resize(gray, (base_w, base_h), interpolation=cv2.INTER_LINEAR)

            for skew_y in skew_y_factors:
                # 縦方向の傾斜
                skewed_h = int(resized.shape[0] * skew_y)
                skewed_w = resized.shape[1]  # 横方向は固定
                skewed = cv2.resize(resized, (skewed_w, skewed_h), interpolation=cv2.INTER_LINEAR)

                center = (skewed_w // 2, skewed_h // 2)
                for angle in angles:
                    # 回転
                    M = cv2.getRotationMatrix2D(center, angle, 1.0)
                    rotated = cv2.warpAffine(skewed, M, (skewed_w, skewed_h), flags=cv2.INTER_LINEAR)

                    # ノイズ除去
                    denoised = cv2.medianBlur(rotated, ksize)

                    # --- エッジ強調（シャープ化） ---
                    sharpened = cv2.filter2D(denoised, -1, kernel_sharpen)

                    # 保存
                    out_name = f"{filename}_ang{angle}_scale{scale}_sky{skew_y}.png"
                    out_path = os.path.join(output_dir, out_name)
                    cv2.imwrite(out_path, sharpened)

                    count += 1
                    total_count += 1

        print(f"{filename}: {count} 枚生成")

    print(f"合計 {total_count} 枚を {output_dir} に保存しました。")


# 使用例
generate_variations_from_folder(
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching",
    r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_temprate",
    ksize=3
)
