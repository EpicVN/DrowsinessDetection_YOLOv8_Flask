from ultralytics import YOLO
import cv2
import math

def video_detection(path_x):
    video_capture = path_x
    
    # Create a Webcam Object
    cap = cv2.VideoCapture(video_capture)
    
    model = YOLO("YOLO-Weights/best.pt").cuda()
    classNames = ["Buon_Ngu", "Tinh_Tao"]
    
    while True:
        success, img = cap.read()
        if not success:
            break
        else:
            results = model(img, stream=True)
            for r in results:
                boxes = r.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    print(x1, y1, x2, y2)
                    
                    # Get class information
                    conf = math.ceil((box.conf[0] * 100)) / 100
                    cls = int(box.cls[0])
                    class_name = classNames[cls]
                    
                    # Set color based on class
                    color = (0, 255, 0)  # default to green
                    if class_name == "Buon_Ngu":
                        color = (0, 0, 255)  # set to red for "Buon_Ngu"
                    
                    # Draw rectangle
                    cv2.rectangle(img, (x1, y1), (x2, y2), color, 3)
                    
                    # Draw filled rectangle for label
                    label = f'{class_name}{conf}'
                    t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                    c2 = x1 + t_size[0], y1 - t_size[1] - 3
                    cv2.rectangle(img, (x1, y1), c2, color, -1, cv2.LINE_AA)
                    
                    # Draw label text
                    cv2.putText(img, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=2, lineType=cv2.LINE_AA)

            yield img