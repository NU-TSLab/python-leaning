from ultralytics import YOLO
import cv2

MODEL_PATH = r"C:/python-leaning/Machine_Learning/runs/exp_cpu_strong4/weights/best.pt"
CLASS_NAME = "speed_sign"                
CONF_THR = 0.45
IOU_THR  = 0.5

def expand_box(xyxy, w, h, ratio=0.10):
    x1,y1,x2,y2 = map(int, xyxy)
    bw, bh = x2-x1, y2-y1
    x1 = max(0, int(x1 - bw*ratio)); y1 = max(0, int(y1 - bh*ratio))
    x2 = min(w-1, int(x2 + bw*ratio)); y2 = min(h-1, int(y2 + bh*ratio))
    return x1,y1,x2,y2

def main():
    model = YOLO(MODEL_PATH)
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        h, w = frame.shape[:2]

        results = model(frame, conf=CONF_THR, iou=IOU_THR, imgsz=640, verbose=False)[0]

        for box in results.boxes:
            cls = int(box.cls[0].item())
            name = results.names.get(cls, str(cls))
            if name != CLASS_NAME:
                continue
            x1,y1,x2,y2 = expand_box(box.xyxy[0].cpu().numpy(), w, h, 0.10)
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.putText(frame, "KORE!", (x1, max(0,y1-6)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)

        cv2.imshow("speed-sign-detect", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

