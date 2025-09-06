import cv2
import easyocr
import glob
import csv
import os

# 画像ディレクトリ
DATA_DIR = "./sign_images"
# 結果ログ
LOG_FILE = "ocr_feedback.csv"

# OCRリーダー
reader = easyocr.Reader(['en'])

# 既存ログ読み込み（追記対応）
existing = set()
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            existing.add(row[0])

# データセット内の画像をループ
for img_path in glob.glob(os.path.join(DATA_DIR, "*.jpg")):
    if img_path in existing:
        continue  # 既に処理済みならスキップ

    img = cv2.imread(img_path)
    cv2.imshow("Sign", img)
    cv2.waitKey(10)  # 表示を更新

    # OCR推定
    results = reader.readtext(img, detail=0)
    prediction = results[0] if results else ""

    print(f"ファイル: {os.path.basename(img_path)}")
    print(f"推定結果: {prediction}")

    # 人間のYES/NO
    while True:
        user_input = input("結果が正しければ y / 間違いなら n: ").strip().lower()
        if user_input in ("y", "n"):
            break

    # ログに保存
    with open(LOG_FILE, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([img_path, prediction, "YES" if user_input == "y" else "NO"])

cv2.destroyAllWindows()
