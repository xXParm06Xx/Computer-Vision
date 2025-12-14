# YOLO Image Dectector (auto) 
# This is a script to detect objects in an image using YOLO 
# Uses pretrained YOLOv8 weights (no custom training)
# JUST FOR PRACTICE AND EXAMPLE

from ultralytics import YOLO
from pathlib import Path # for auto path fetching for images
import cv2

model = YOLO("weights/yolov8n.pt") # specifying the path for downloading the weights


folder = Path("Yolo-Images")
if not folder.exists():
    print("No 'images' folder found.")
    exit()

files = folder.glob("*") 

image_paths = []

valid_ext = [".jpg", ".png", ".jpeg", ".bmp", ".webp"]
for file in files:
    if file.suffix.lower() in valid_ext:
        image_paths.append(file)

if not image_paths:
    print("No valid images found in the 'images' folder.")
    exit()

image_paths.sort()

try:
    results = model(image_paths)
except Exception as e:
    print(e)

# looping through results
for i, res in enumerate(results):
    img = res.plot()
    img = cv2.resize(img, (1000, 600))
    cv2.imshow(f"Result {i+1}", img) 
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
