# Import the cv2 library
import cv2
import numpy as np 
# Read the image you want connected components of
img = cv2.imread('test1.bmp',cv2.IMREAD_GRAYSCALE)
# Threshold it so it becomes binary

connectivity = 4  


num_labels, labelmap = cv2.connectedComponents(img,connectivity,cv2.CV_32S)

img = np.hstack((img,labelmap.astype(np.float32)/(num_labels-1)))
cv2.imshow("lets see",img)

cv2.waitKey(0)