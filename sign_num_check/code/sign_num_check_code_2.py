import os, glob, csv
import cv2
import numpy as np
import easyocr
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# ==== 設定 ====
DATA_DIR = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic_2"
LOG_FILE = "ocr_feedback_1_2.csv"

# 認識を許可する標識数字
VALID_SIGNS = {"10","20","30","40","50","60","70","80"}

reader = easyocr.Reader(['en'], gpu=True)   # GPU不要なら gpu=False

# ==== 既に処理したファイル ====
processed = set()
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            if row:
                processed.add(row[0])

# ==== 画像ファイル ====
image_files = []
for ext in ("*.jpg",):
    image_files.extend(glob.glob(os.path.join(DATA_DIR, ext)))

print(f"見つかった画像ファイル数: {len(image_files)}")
if not image_files:
    print("画像が見つかりません。DATA_DIR のパスを再確認してください。")

# ==== メインループ ====
for img_path in image_files:
    if img_path in processed:
        continue

    img = cv2.imread(img_path)
    if img is None:
        print(f"読み込み失敗: {img_path}")
        continue

    # -------- 明るさ・コントラスト補正 --------
    alpha, beta = 1.3, 30
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    # -------- 青色マスク --------
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90,  60,  50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # -------- ノイズ低減 --------
    # ガウシアンブラーで平滑化
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # モルフォロジー処理（小さな点ノイズ除去）
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)  # 穴埋め
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)   # 小さい点除去

    # 白黒反転
    preproc = cv2.bitwise_not(mask)

    # OCR
    results = reader.readtext(preproc, detail=0)

    # 許可された標識のみ残す
    filtered = [txt for txt in results if txt.isdigit() and txt in VALID_SIGNS]
    prediction = " ".join(filtered)

    # デバッグ用にマスク確認したい場合はコメントアウト解除
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 画像を既定ビューアで開く（Windows）
    try:
        os.startfile(img_path)
    except AttributeError:
        pass

    print(f"ファイル: {os.path.basename(img_path)}")
    print(f"OCR推定: {prediction if prediction else '(標識候補は検出されませんでした)'}")

    # フィードバック
    while True:
        ans = input("正しければ y / 間違いなら n を入力: ").strip().lower()
        if ans in ("y", "n"):
            break

    with open(LOG_FILE, "a", newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([img_path, prediction, "YES" if ans == "y" else "NO"])

print("全画像の確認が終了しました。")
