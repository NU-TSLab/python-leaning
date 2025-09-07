import cv2, easyocr, glob, csv, os

DATA_DIR = r"C:\Users\csfu2\Documents\Python_git_study\python-leaning\sign_num_check\pic"
LOG_FILE = "ocr_feedback.csv"

reader = easyocr.Reader(['en'])

processed = set()
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            processed.add(row[0])

# jpg / png / jpeg を全部拾う
image_files = []
for ext in ("*.jpg", "*.JPG", "*.jpeg", "*.png"):
    image_files.extend(glob.glob(os.path.join(DATA_DIR, ext)))

print(f"見つかった画像ファイル数: {len(image_files)}")
if not image_files:
    print("画像が見つかりません。DATA_DIR のパスを再確認してください。")

for img_path in image_files:
    if img_path in processed:
        continue

    img = cv2.imread(img_path)
    if img is None:
        print(f"読み込み失敗: {img_path}")
        continue

    cv2.imshow("Sign", img)
    cv2.waitKey(10)

    results = reader.readtext(img, detail=0)
    prediction = results[0] if results else ""

    print(f"ファイル: {os.path.basename(img_path)}")
    print(f"OCR推定: {prediction}")

    while True:
        ans = input("正しければ y / 間違いなら n を入力: ").strip().lower()
        if ans in ("y", "n"):
            break

    with open(LOG_FILE, "a", newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([img_path, prediction, "YES" if ans == "y" else "NO"])

cv2.destroyAllWindows()
