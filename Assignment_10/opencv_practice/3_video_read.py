import cv2
import os

video_path = os.path.join(os.path.dirname(__file__), "..", "videos", "input.mp4")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Cannot open video:", video_path)
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):

        break

cap.release()
cv2.destroyAllWindows()