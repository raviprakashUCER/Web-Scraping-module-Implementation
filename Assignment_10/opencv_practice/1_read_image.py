import cv2
import os

img_path = os.path.join(os.path.dirname(__file__), "..", "images", "input.jpg")

img = cv2.imread(img_path)

if img is None:
    print("❌ Image not found at:", img_path)
    exit()

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()