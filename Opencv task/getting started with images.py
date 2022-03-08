import cv2 as cv
import sys
img = cv.imread("/home/swayam/opencv/samples/data/butterfly.jpg")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(10000)
if k == ord("s"):
    cv.imwrite("starry_night.png", img)