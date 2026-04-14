import cv2

img = cv2.imread("images/input.jpg")

if img is None:
    print("Image not found! Check path")
    exit()

cv2.imwrite("images/output.jpg", img)

print("Image saved successfully")