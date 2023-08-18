import cv2
import numpy as np

# Load image
img = cv2.imread('test1.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

# Threshold to get just the signature (INVERTED)
_, thresh_gray = cv2.threshold(gray, thresh=100, maxval=255, type=cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(thresh_gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Find object with the biggest bounding box
mx = (0, 0, 0, 0)  # biggest bounding box so far
mx_area = 0
for cont in contours:
    x, y, w, h = cv2.boundingRect(cont)
    area = w * h
    if area > mx_area:
        mx = x, y, w, h
        mx_area = area
x, y, w, h = mx

# Draw bounding rectangle on the image
cv2.rectangle(img, (x, y), (x+w, y+h), (200, 0, 0), 2)

# Display the image with the bounding rectangle
cv2.imshow('Image with Bounding Rectangle', thresh_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
