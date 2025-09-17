import cv2
import numpy as np
import os
import glob

def generate_variations_from_folder(input_dir, output_dir="output", discard_bad=True):
    # 出力先ディレクトリ作成
    os.makedirs(output_dir, exist_ok=True)

    # フォルダ内のPNGファイル一覧取得
    files = glob.glob(os.path.join(input_dir, "*.jpg"))
    if not files:
        raise FileNotFoundError(f"{input_dir} に .jpg ファイルが見つかりません。")

    # 回転角度と倍率の組み合わせ
    angles = [-10, 0, 10]
    scales = [2.0, 1.0, 0.5]

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
            # 拡大縮小
            new_w = int(gray.shape[1] * scale)
            new_h = int(gray.shape[0] * scale)
            resized = cv2.resize(gray, (new_w, new_h), interpolation=cv2.INTER_LINEAR)

            h, w = resized.shape
            center = (w // 2, h // 2)

            for angle in angles:
                # 回転
                M = cv2.getRotationMatrix2D(center, angle, 1.0)  # scale=1.0（すでにリサイズ済み）
                rotated = cv2.warpAffine(resized, M, (w, h), flags=cv2.INTER_LINEAR)

                # --- ノイズ除去処理 ---
                blurred = cv2.GaussianBlur(rotated, (5, 5), 0)
                _, denoised = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

                # 品質チェック（真っ黒／真っ白すぎる画像は破棄）
                if discard_bad:
                    white_ratio = np.mean(denoised == 255)
                    if white_ratio < 0.05 or white_ratio > 0.95:
                        # 破棄
                        print(f"破棄: {filename} ang{angle} scale{scale} (白比率={white_ratio:.2f})")
                        continue

                # 保存パス
                out_name = f"{filename}_ang{angle}_scale{scale}.png"
                out_path = os.path.join(output_dir, out_name)
                cv2.imwrite(out_path, denoised)

                count += 1
                total_count += 1

        print(f"{filename}: {count} 枚生成 (破棄除く)")

    print(f"合計 {total_count} 枚を {output_dir} に保存しました。")


# 使用例
generate_variations_from_folder(r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching", r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pattern_matching_temprate")
