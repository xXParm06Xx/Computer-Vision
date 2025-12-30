# using yolo with videos

from ultralytics import YOLO
from pathlib import Path
import cv2
import cvzone
import math, time

# initialisation
model = YOLO("weights/yolov8n.pt")  # using yolov8n model

# retrieving classes
with open("yolo.txt", "r") as f:
    classNames = f.read().splitlines() 

def path():
    folder = Path("videos")
    files = folder.glob("*.*")

    vid_path = []
    valid_ext = [".mp4", ".mkv", ".avi", ".mov"]
    for file in files:
        if file.suffix.lower() in valid_ext:
            vid_path.append(file)
    return vid_path


def anim(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)


def detector(frame, results):
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            width, height = x2 - x1, y2 - y1
            bbox = int(x1), int(y1), int(width), int(height)
            cvzone.cornerRect(frame, bbox, l=10, t=2)
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            curr_class = classNames[cls]
            color = (
                (255, 0, 255) if conf > 0.6 else (0, 0, 255)
            )  # if confidence is greater logic
            cvzone.putTextRect(
                frame,
                f"{curr_class} {conf}",
                (max(0, x1), max(35, y1)),
                scale=0.8,
                thickness=2,
                font=cv2.FONT_HERSHEY_COMPLEX,
                offset=5,
                colorR=color,
            )


def fps(frame, prev_time):
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if curr_time != prev_time else 0
    prev_time = curr_time
    cv2.putText(
        frame, f"FPS: {fps}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2
    )
    return prev_time


def main():
    prev_time = time.time()
    anim("YOLO Video Detector is starting...\n")

    user_inp = input("Enter 1 for video detection or 2 for webcam detection: ")

    if user_inp == "1":
        videos = path()

        if len(videos) == 0:
            anim("No videos found in videos folder.")
            return

        cv2.namedWindow("Detector", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Detector", 640, 380)

        # LOOPING OVER ALL VIDEOS
        for video in videos:
            anim(f"\nPlaying video: {video.name}")
            cap = cv2.VideoCapture(str(video))

            while True:
                ret, frame = cap.read()
                if not ret:
                    anim(f"Finished: {video.name}")
                    break

                results = model(frame, imgsz=640, stream=True, conf=0.4, iou=0.4)
                detector(frame, results)

                prev_time = fps(frame, prev_time)

                cv2.imshow("Detector", frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    cap.release()
                    cv2.destroyAllWindows()
                    anim("User exited.")
                    return

            cap.release()
            time.sleep(1)

        anim("\nAll videos completed.")
        cv2.destroyAllWindows()

    elif user_inp == "2":
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)
        cv2.namedWindow("Detector", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Detector", 640, 480)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            results = model(frame, conf=0.4, iou=0.4)
            detector(frame, results)
            prev_time = fps(frame, prev_time)

            cv2.imshow("Detector", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
