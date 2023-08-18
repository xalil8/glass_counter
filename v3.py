import cv2

# Global variables to store filter threshold, blur, and morphological operation values
threshold_value = 128
blur_value = 0
dilation_kernel_value = 3
erosion_kernel_value = 3
opening_kernel_value = 3

# Callback function for threshold slider
def update_threshold(x):
    global threshold_value
    threshold_value = x

# Callback function for blur slider
def update_blur(x):
    global blur_value
    blur_value = x if x % 2 == 1 else x + 1  # Ensure blur kernel size is odd

# Callback function for dilation kernel slider
def update_dilation_kernel(x):
    global dilation_kernel_value
    dilation_kernel_value = x if x % 2 == 1 else x + 1  # Ensure kernel size is odd

# Callback function for erosion kernel slider
def update_erosion_kernel(x):
    global erosion_kernel_value
    erosion_kernel_value = x if x % 2 == 1 else x + 1  # Ensure kernel size is odd

# Callback function for opening kernel slider
def update_opening_kernel(x):
    global opening_kernel_value
    opening_kernel_value = x if x % 2 == 1 else x + 1  # Ensure kernel size is odd

def apply_filter(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply blur with the current blur value
    blurred = cv2.GaussianBlur(gray, (blur_value, blur_value), 0)
    
    # Apply dilation
    dilation_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (dilation_kernel_value, dilation_kernel_value))
    dilated = cv2.dilate(blurred, dilation_kernel, iterations=1)
    
    # Apply erosion
    erosion_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (erosion_kernel_value, erosion_kernel_value))
    eroded = cv2.erode(dilated, erosion_kernel, iterations=1)
    
    # Apply opening
    opening_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (opening_kernel_value, opening_kernel_value))
    opened = cv2.morphologyEx(eroded, cv2.MORPH_OPEN, opening_kernel)
    
    # Apply thresholding with the current threshold value
    _, filtered_frame = cv2.threshold(opened, threshold_value, 255, cv2.THRESH_BINARY)
    
    return filtered_frame

def main():
    frame = cv2.imread("test1.bmp")
    cv2.namedWindow('Filtered Frame')
    
    # Create trackbars for various operations
    cv2.createTrackbar('Threshold', 'Filtered Frame', threshold_value, 255, update_threshold)
    cv2.createTrackbar('Blur', 'Filtered Frame', blur_value, 20, update_blur)
    cv2.createTrackbar('Dilation Kernel', 'Filtered Frame', dilation_kernel_value, 20, update_dilation_kernel)
    cv2.createTrackbar('Erosion Kernel', 'Filtered Frame', erosion_kernel_value, 20, update_erosion_kernel)
    cv2.createTrackbar('Opening Kernel', 'Filtered Frame', opening_kernel_value, 20, update_opening_kernel)
    
    while True:
        filtered_frame = apply_filter(frame)
        
        # Find contours in the filtered image
        contours, _ = cv2.findContours(filtered_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Find the largest contour
        largest_contour = max(contours, key=cv2.contourArea, default=None)
        
        # Draw the largest contour with red lines on the filtered image
        contour_image = filtered_frame.copy()
        cv2.drawContours(contour_image, [largest_contour], -1, (0, 0, 255), 2)
        
        show_image = cv2.resize(contour_image, (720, 540))
        cv2.imshow('Filtered Frame', show_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Print trackbar values after the loop
    print("Threshold:", threshold_value)
    print("Blur:", blur_value)
    print("Dilation Kernel:", dilation_kernel_value)
    print("Erosion Kernel:", erosion_kernel_value)
    print("Opening Kernel:", opening_kernel_value)
    
    # Release the video capture and destroy windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
