from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
import os
import base64

model = YOLO('yolov8n.pt')

def encode_image(img_array):
    _, buffer = cv2.imencode('.jpg', img_array)
    return base64.b64encode(buffer).decode('utf-8')

def analyze_image_bytes(image_bytes):
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    results = model(img)
    plotted_img = results[0].plot()
    return extract_classes(results), encode_image(plotted_img)

def analyze_video(video_bytes):
    detected_objects = set()
    best_frame_base64 = None
    first_frame_base64 = None 
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_bytes)
        temp_video_path = temp_video.name

    try:
        cap = cv2.VideoCapture(temp_video_path)
        frame_count = 0
        
        while cap.isOpened():
            success, frame = cap.read()
            if not success: break
            
            if frame_count == 0:
                first_frame_base64 = encode_image(model(frame)[0].plot())
            
            if frame_count % 30 == 0:
                results = model(frame)
                classes = extract_classes(results)
                detected_objects.update(classes)
                
                if len(classes) > 0 and best_frame_base64 is None:
                    best_frame_base64 = encode_image(results[0].plot())
                    
            frame_count += 1
        cap.release()
    finally:
        os.remove(temp_video_path)
        
    final_image = best_frame_base64 if best_frame_base64 else first_frame_base64
    return list(detected_objects), final_image

def extract_classes(results):
    found = []
    for r in results:
        for box in r.boxes:
            if float(box.conf[0]) > 0.25: 
                found.append(model.names[int(box.cls[0])])
    return found