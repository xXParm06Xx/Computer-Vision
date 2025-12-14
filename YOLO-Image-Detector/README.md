# 👾 YOLO Image Detector

A simple Python script that automatically detects objects in images using YOLOv8. Just drop your images in a folder and run the script—no configuration needed.

## 📌 What It Does

* Detects objects in all images inside the `images/` folder
* Supports common formats: `.jpg`, `.png`, `.jpeg`, `.bmp`, `.webp`
* Uses pretrained YOLOv8 weights (no custom training required)
* This weights are downloaded automatically in `weights/` folder
* Runs batch inference on multiple images at once
* Displays detection results with bounding boxes and labels
* Works out of the box—model weights download automatically on first run

## 📁 Project Structure

```
YOLO-Image-Detector/
├── main.py
├── requirements.txt
├── weights/
    └── yolov8n.pt (downloaded automatically when program is run)
├── README.md
└── images/
    ├── image1.jpg
    ├── image2.png
    └── ... here you can add images
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/xXParm06Xx/YOLO-Image-Detector.git
cd YOLO-Image-Detector
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
numpy==1.26.4
opencv-python==4.9.0.80
Pillow==10.2.0
ultralytics==8.3.27
torch==2.2.2
torchvision==0.17.2
matplotlib==3.8.4
tqdm==4.66.2
PyYAML==6.0.1
requests==2.31.0
scipy==1.11.4
psutil==5.9.8
seaborn==0.13.2
pandas==2.2.2
```

## 🚀 How to Run

Make sure you're in the project root directory, then run:

```bash
python main.py
```

The script will:
1. Look for images in the `images/` folder
2. Run object detection on each image
3. Display results one by one (press any key to move to the next image)
4. Close all windows when done

## 📷 How to Add Images

1. Create an `images/` folder in the project root (if it doesn't exist)
2. Add your images to this folder
3. Run the script—it will automatically detect all valid images

No code changes needed. The script handles everything automatically.

## 💡 Purpose

This project is a practical example for learning:
* How to use pretrained YOLO models
* Batch image processing with Python
* Basic computer vision workflows with OpenCV

It's intended for practice and demonstration purposes.

## 🔮 Future Improvements

* Save detection results to an output folder instead of just displaying them
* Add command-line arguments for custom input/output paths
* Support video file detection
* Export detection results to JSON or CSV
* Add confidence threshold filtering
* Enable webcam live detection mode

## 📝 Notes

* The YOLOv8 model weights (`yolov8n.pt`) are **not included** in this repository
* They will be **downloaded automatically** by Ultralytics in the `weights/` folderon the first run
* The model file is around 6MB and will be cached locally
* Make sure you have an active internet connection for the first run