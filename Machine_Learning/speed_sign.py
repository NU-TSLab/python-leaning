from ultralytics import YOLO
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

"""---------------YOLO---------------"""
MODEL_PATH = r"C:/python-leaning/Machine_Learning/runs/exp_cpu_strong4/weights/best.pt"
CLASS_NAME = "speed_sign"                
CONF_THR = 0.8
IOU_THR  = 0.5
IMG_SIZE = 640

"""---------------AKAZE Pattern Matching---------------"""
FIND_KEYPOINTS_THRESHOLD = 0.000001
OCTAVES = 5
OCTAVELAYERS = 6
MATCHING_THRESHOLD = 0.85

"""---------------Preparation---------------"""
GAMMA = 1.3
CLAHE = 3.5
SIGMOID_CENTER_1 = 140
SIGMOID_KONSTANT_1 = 0.35
SIGMOID_CENTER_2 = 95
SIGMOID_KONSTANT_2 = 0.35
ROI_SCALE = 256
SCALE_MAX = 999

"""---------------TextBox---------------"""
ACTUAL_VALUE_SCALE = 0.9
ACTUAL_VALUE_THICKNESS = 2
ACTUAL_VALUE_MARGIN = 6

OUTPUT_SPEED_SCALE = 2.0
OUTPUT_SPEED_THICKNESS = 3
OUTPUT_SPEED_MARGIN = 240

FONT = cv2.FONT_HERSHEY_SIMPLEX
GREEN = (0, 255, 0)

"""---------------Speed Judge---------------"""
JUDGE_FRAMES = 7
JUDGE_THRESHOLD = 4
DISPLAY_FRAMES = 7

CUT_FRAME = 1
MAX_FRAMES = 17000
TEMP_LABEL = [20, 30, 40, 50, 60, 70, 80, 90]
SOURCE_MODE = "video"  
VIDEO_PATH = r"C:/python-leaning/Machine_Learning/conv/IMG_0478.MOV"
global img2gamma, img2sigmoid_1, img2sigmoid_2

akaze = cv2.AKAZE_create(threshold=FIND_KEYPOINTS_THRESHOLD, nOctaves=OCTAVES, nOctaveLayers=OCTAVELAYERS)
bf = cv2.BFMatcher(cv2.NORM_HAMMING)

templates_img = {}
speed_label = {}
latest_judge_speed = [None for i in range(JUDGE_FRAMES)]

def frame_generator():
    """カメラまたは動画からフレームを逐次取得"""
    if SOURCE_MODE == "camera":
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        print("🎥 Webカメラモード開始")
    elif SOURCE_MODE == "video":
        cap = cv2.VideoCapture(VIDEO_PATH)
        if not cap.isOpened():
            raise RuntimeError("動画が開けませんでした。VIDEO_PATHを確認してください。")
        print(f"🎞 動画モード開始: {VIDEO_PATH}")
    else:
        raise ValueError("SOURCE_MODE は 'camera' または 'video' を指定してください。")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("🔚 フレーム取得終了")
            break
        yield frame

    cap.release()

def show_speed_graph(pltspeed=None):
    global speed_label

    plt.ion()
    plt.clf()

    bars = plt.bar(
        speed_label.keys(),
        speed_label.values(),
        color="limegreen",
        width=2.5,
        linewidth=1.0,
        edgecolor="black"
    )

    plt.ylim(0, JUDGE_FRAMES)
    plt.xlabel("Speed (km/h)")
    plt.ylabel("Vote Count")
    plt.title(f"Last {JUDGE_FRAMES}:")

    # --- 各棒の中に数値を表示 ---
    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width()/2,  # x位置（中央）
            height/2,                         # y位置（中央あたり）
            f"{int(height)}",                 # 表示する文字
            ha='center', va='center',
            fontsize=14, color="black", weight='bold'
        )

    if pltspeed is not None:
        plt.text(
            0.5, 0.92,                       # 軸比で位置指定（中央上）
            f"Output: {pltspeed} km/h",
            ha='center', va='center',
            transform=plt.gca().transAxes,
            fontsize=16, color="orange", weight='bold'
        )
    else:
        plt.text(
            0.5, 0.92,                       # 軸比で位置指定（中央上）
            f"Output: None",
            ha='center', va='center',
            transform=plt.gca().transAxes,
            fontsize=16, color="gray", weight='bold'
        )

    plt.tight_layout()
    plt.pause(0.001)

def expand_box(xyxy, w, h, ratio=0.10, p=1):
    x1,y1,x2,y2 = map(int, xyxy)
    bw, bh = int((x2-x1) * p), y2-y1
    x1 = max(0, int(x1 - bw*ratio)); y1 = max(0, int(y1 - bh*ratio))
    x2 = min(w-1, int(x2 + bw*ratio)); y2 = min(h-1, int(y2 + bh*ratio))
    return x1,y1,x2,y2

def remove_red(roi):
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0, 30, 30])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 30, 30])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 | mask2

    kernel = np.ones((3,3), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    roi_no_red = roi.copy()
    roi_no_red[mask > 0] = (255, 255, 255)

    return roi_no_red

def log_boost(gray, sigma=1.6, ksize=3, alpha=0.3):
    """
    gray: 8bit単一チャンネル
    sigma: 事前Gaussianのσ（ノイズ抑え）
    ksize: Laplacianのカーネル（3 or 5）
    alpha: 混ぜる強さ（0.2〜0.6でAB）
    """
    g = cv2.GaussianBlur(gray, (0, 0), sigmaX=sigma, sigmaY=sigma)
    lap = cv2.Laplacian(g, cv2.CV_16S, ksize=ksize)
    lap = cv2.convertScaleAbs(lap)                 # 0–255へ
    # 0中心に寄せて“輪郭だけ”を薄く加算
    lap = cv2.normalize(lap, None, 0, 255, cv2.NORM_MINMAX)
    out = cv2.addWeighted(gray, 1.0, lap, alpha, 0)
    return out

def gamma_preparation():
    global img2gamma
    img2gamma = np.zeros((256, 1),  dtype=np.uint8) 

    for i in range(256):
        img2gamma[i][0] = 255 * (float(i) / 255) ** (1.0 / GAMMA)

def sigmoid_preparation(center_1, k_1, center_2, k_2):
    global img2sigmoid_1, img2sigmoid_2
    x = np.arange(256)
    sigmoid = 1.0 / (1 + np.exp(-k_1 * (x - center_1)))
    img2sigmoid_1 = np.uint8(sigmoid * 255)
    sigmoid = 1.0 / (1 + np.exp(-k_2 * (x - center_2)))
    img2sigmoid_2 = np.uint8(sigmoid * 255)


def image_preparation(roi, th, mb = 3):
    h, w = roi.shape[:2]
    scale = ROI_SCALE / min(h, w)
    scale = min(SCALE_MAX, scale)
    interp = cv2.INTER_AREA if scale < 1.0 else cv2.INTER_CUBIC
    roi = cv2.resize(roi, (int(w*scale), int(h*scale)), interpolation=interp)
    w_scale = int(w * scale)
    #roi = roi[:, :w_scale // 2]

    #roi = remove_red(roi)

    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    gray = cv2.medianBlur(gray, mb)

    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    gray = cv2.LUT(gray, img2gamma)

    clahe = cv2.createCLAHE(CLAHE, (8, 8)); gray = clahe.apply(gray)

    gray = cv2.LUT(gray, img2sigmoid_1)

    #gray = cv2.LUT(gray, img2sigmoid_2)

    #gray = cv2.LUT(gray, img2gamma)

    #gray = cv2.GaussianBlur(gray, (0, 0), 0.8)

    #gray = log_boost(gray)

    #_, gray = cv2.threshold(gray, th, 255, cv2.THRESH_BINARY)

    return gray

def match_figure(kp_roi, des_roi, img_roi, templates, threshold, frame_c=0, box_c=0):
    best_label = None
    best_score = 0

    for label, (kp_t, des_t) in templates.items():
        if des_t is None or des_roi is None:
            continue

        bf_strict = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf_strict.match(des_t, des_roi)
        matches = [m for m in matches if m.distance < 60]
        matches = sorted(matches, key=lambda x: x.distance)

        print(f"[{label}] match数 = {len(matches)}")

        score = 0
        matches_mask = None

        if len(matches) >= 4:
            src_pts = np.float32([kp_t[m.queryIdx].pt for m in matches])
            dst_pts = np.float32([kp_roi[m.trainIdx].pt for m in matches])

            H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if mask is not None:
                matches_mask = mask.ravel().tolist()
                score = int(np.sum(matches_mask))

        if score > best_score:
            best_label = label
            best_score = score
        try:
            draw_params = dict(
                matchColor=(0,255,0),
                singlePointColor=None,
                matchesMask=matches_mask if matches_mask else None,
                flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
            )
            out = cv2.drawMatches(img_roi, kp_roi, templates_img[label], kp_t, matches, None, **draw_params)
            cv2.imwrite(f"C:/python-leaning/Machine_Learning/materials/ex/{frame_c}_{best_label}_{box_c}_strict.png", out)
        except Exception as e:
            print(f"⚠️ draw error: {e}")

        

    return best_label, best_score


def clean_dir(dir):
    for name in os.listdir(dir):
        p = os.path.join(dir, name)
        if os.path.isfile(p):
            os.remove(p)

def speed_judge(latest_speed):
    global latest_judge_speed, speed_label
    for label in TEMP_LABEL:
        speed_label[label] = 0
    for i in range(JUDGE_FRAMES-1):
        latest_judge_speed[JUDGE_FRAMES-i-1] = latest_judge_speed[JUDGE_FRAMES-i-2]
    latest_judge_speed[0] = latest_speed

    print(f"latest_judge_speed = {latest_judge_speed}")

    for i in range(JUDGE_FRAMES):
        if latest_judge_speed[i] == None:
            continue
        speed_label[latest_judge_speed[i]] += 1
    for label in TEMP_LABEL:
        if speed_label[label] >= JUDGE_THRESHOLD:
            return label
        
    return None

def main():
    model = YOLO(MODEL_PATH)
    clean_dir(r"C:/python-leaning/Machine_Learning/materials/ex")
    gamma_preparation()
    sigmoid_preparation(SIGMOID_CENTER_1, SIGMOID_KONSTANT_1, SIGMOID_CENTER_2, SIGMOID_KONSTANT_2)

    templates = {}
    for label in TEMP_LABEL:
        img = cv2.imread(f"C:/python-leaning/Machine_Learning/conv/figure/{label}.png")
        img = image_preparation(img, 90, 5)
        cv2.imwrite(f"C:/python-leaning/Machine_Learning/materials/ex/temp{label}.png", img)
        kp, des = akaze.detectAndCompute(img, None)
        out = cv2.drawKeypoints(img, kp, None, GREEN, 0)
        cv2.imwrite(f"C:/python-leaning/Machine_Learning/materials/ex/temp{label}_kp{len(kp)}.png", out)
        templates[label] = (kp, des)
        templates_img[label] = img
    
    frame_count = 0
    global latest_judge_speed
    judged_speed = None
    speed_temp = None
    none_count = 0
    frame = []
    for frame in frame_generator():
        h, w = frame.shape[:2]
        frame_count += 1
        if not frame_count % CUT_FRAME == 0:
            continue

        results = model(frame, conf=CONF_THR, iou=IOU_THR, imgsz=IMG_SIZE, verbose=False)[0]
        box_count = 0
        roi_exist = False
        for box in results.boxes:
            cls = int(box.cls[0].item())
            name = results.names.get(cls, str(cls))
            if name != CLASS_NAME:
                continue
            roi_exist = True
            box_count += 1
            x1,y1,x2,y2 = expand_box(box.xyxy[0].cpu().numpy(), w, h, -0.25, 0.80)

            roi = frame[y1:y2, x1:x2]
            roi = image_preparation(roi, 90, 5)
            if roi is not None and roi.size > 0:
                cv2.imshow("ROI", roi)
            kp, des = akaze.detectAndCompute(roi, None)
            match_label, score = match_figure(kp, des, roi, templates, MATCHING_THRESHOLD, frame_count, box_count)
            judged_speed = speed_judge(match_label)
            print(f"judged_speed = {judged_speed}")
            x1,y1,x2,y2 = expand_box(box.xyxy[0].cpu().numpy(), w, h, 0.10)
            cv2.rectangle(frame, (x1,y1), (x2,y2), GREEN, 2)
            print(f"score={score}")
            out = cv2.drawKeypoints(roi, kp, None, GREEN, 0)
            cv2.imwrite(f"C:/python-leaning/Machine_Learning/materials/ex/roi{frame_count}_label{match_label}_kp{len(kp)}.png", out)
            if match_label is not None and score >= 0:
                cv2.putText(frame, f"{match_label}km/h", (x1, max(0,y1-ACTUAL_VALUE_MARGIN)),
                            FONT, ACTUAL_VALUE_SCALE, GREEN, ACTUAL_VALUE_THICKNESS)
                print(f"{match_label}km/h")
        pltspeed = None
        if not roi_exist:
            judged_speed = None
            speed_judge(None)
        if judged_speed == None:
            none_count += 1
            if none_count <= DISPLAY_FRAMES:
                if speed_temp is not None:
                    pltspeed = speed_temp
                    text = f"{speed_temp}km/h"
                    (tw, th), baseline = cv2.getTextSize(text, FONT, OUTPUT_SPEED_SCALE, OUTPUT_SPEED_THICKNESS)
                    x = (w - tw) // 2
                    y = h - OUTPUT_SPEED_MARGIN
                    cv2.putText(frame, text, (x, y), FONT, OUTPUT_SPEED_SCALE, GREEN, 2, cv2.LINE_AA)
            else:
                speed_temp = None
        else:
            pltspeed = judged_speed
            text = f"{judged_speed}km/h"
            (tw, th), baseline = cv2.getTextSize(text, FONT, OUTPUT_SPEED_SCALE, OUTPUT_SPEED_THICKNESS)
            x = (w - tw) // 2
            y = h - OUTPUT_SPEED_MARGIN
            cv2.putText(frame, text, (x, y), FONT, OUTPUT_SPEED_SCALE, GREEN, 2, cv2.LINE_AA)
            speed_temp = judged_speed
            none_count = 0
        
        cv2.namedWindow("speed-sign-detect", cv2.WINDOW_NORMAL)
        cv2.imshow("speed-sign-detect", frame)
        cv2.resizeWindow("speed-sign-detect", 540, 960)

        show_speed_graph(pltspeed)

        if cv2.waitKey(1) & 0xFF == 27:
            break

        

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

