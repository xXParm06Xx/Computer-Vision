# 🎥 YOLO Video Detector

A powerful Python application that detects objects in real-time from videos and webcam feeds using YOLOv8. Just drop your videos in a folder or use your webcam—no configuration needed.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## 📌 What It Does

* Detects 80 different object classes in real-time from videos or webcam
* Supports common video formats: `.mp4`, `.mkv`, `.avi`, `.mov`
* Uses pretrained YOLOv8 weights (no custom training required)
* Weights are downloaded automatically in `weights/` folder
* Processes multiple videos in batch mode automatically
* Displays live FPS counter for performance monitoring
* Color-coded confidence levels (purple for high, red for moderate)
* Works out of the box—model weights download automatically on first run

## 📁 Project Structure

```
YOLO-Video-Detector/
├── main.py
├── requirements.txt
├── README.md
├── weights/
│   └── yolov8n.pt (downloaded automatically when program is run)
└── videos/
    ├── cars.mp4
    ├── bikes.mp4
    └── ... (place your videos here)
```

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/xXParm06Xx/YOLO-Image-Detector.git
cd YOLO-Video-Detector
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
ultralytics>=8.0.0
opencv-python>=4.8.0
cvzone>=1.6.1
numpy>=1.24.0
torch>=2.0.0
torchvision>=0.15.0
```

### 4. Create Required Folders

**Windows:**
```bash
mkdir videos
mkdir weights
```

**macOS/Linux:**
```bash
mkdir -p videos weights
```

## 🚀 How to Run

Make sure you're in the project root directory and your virtual environment is activated, then run:

```bash
python main.py
```

You'll see an interactive prompt:

```
YOLO Video Detector is starting...
Enter 1 for video detection or 2 for webcam detection:
```

### Option 1: Video Detection Mode
1. Place your video files in the `videos/` folder
2. Enter `1` when prompted
3. The detector will process all videos sequentially
4. Press `q` at any time to exit

### Option 2: Webcam Detection Mode
1. Ensure your webcam is connected and accessible
2. Enter `2` when prompted
3. Point your camera at objects to detect them in real-time
4. Press `q` to quit

## 📷 How to Add Videos

1. Create a `videos/` folder in the project root (if it doesn't exist)
2. Add your video files to this folder (`.mp4`, `.mkv`, `.avi`, `.mov`)
3. Run the script and select option `1`—it will automatically detect all valid videos

No code changes needed. The script handles everything automatically.

## 🎯 Detectable Objects (80 Classes)

The detector can identify objects including:

**People & Animals**: person, cat, dog, horse, bird, sheep, cow, elephant, bear, zebra, giraffe

**Vehicles**: car, bicycle, motorcycle, airplane, bus, train, truck, boat

**Indoor Objects**: chair, couch, bed, dining table, toilet, tv, laptop, mouse, keyboard, phone

**Kitchen Items**: bottle, wine glass, cup, fork, knife, spoon, bowl, banana, apple, orange

**And many more...** (80 total classes from COCO dataset)

## ⚙️ Configuration Options

You can customize detection parameters by modifying these values in `main.py`:

```python
# Confidence threshold (default: 0.4) - lower = more detections
results = model(frame, conf=0.4, iou=0.4)

# Image processing size (default: 640) - higher = more accurate but slower
results = model(frame, imgsz=640, stream=True)

# Color-coding threshold (default: 0.6)
color = (255, 0, 255) if conf > 0.6 else (0, 0, 255)
```

## 💡 Purpose

This project is a practical example for learning:
* How to use pretrained YOLO models for video processing
* Real-time object detection with OpenCV
* Batch video processing workflows
* Webcam integration for live detection
* Performance optimization with FPS tracking

It's intended for practice, demonstration, and educational purposes.

## 🔮 Future Improvements

* Save detection results as annotated video files
* Add command-line arguments for custom input/output paths
* Export detection statistics to JSON or CSV
* Add object tracking across frames
* Support for multiple camera sources
* Detection heatmap generation
* Custom object class filtering
* Save detection highlights/clips

## 🐛 Troubleshooting

**Issue**: "No videos found in videos folder"
* **Solution**: Ensure video files are in `videos/` directory with supported extensions

**Issue**: Webcam not detected
* **Solution**: Check if another app is using the camera. Close other apps and restart

**Issue**: Low FPS performance
* **Solution**: Reduce `imgsz` parameter or increase confidence threshold

**Issue**: ModuleNotFoundError
* **Solution**: Activate virtual environment and run `pip install -r requirements.txt`

## 📝 Notes

* The YOLOv8 model weights (`yolov8n.pt`) are **not included** in this repository
* They will be **downloaded automatically** by Ultralytics in the `weights/` folder on the first run
* The model file is around 6MB and will be cached locally
* Make sure you have an active internet connection for the first run
* For best performance, use a GPU-enabled system (CUDA support)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

## 📧 License

This project is licensed under the MIT License - feel free to use it for learning and personal projects.

## 🙏 Acknowledgments

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) - Object detection model
* [OpenCV](https://opencv.org/) - Computer vision library
* [cvzone](https://github.com/cvzone/cvzone) - Enhanced visualization tools

---

⭐ **If you found this project helpful, please give it a star!**

**Happy Detecting! 🎯**