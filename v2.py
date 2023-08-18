import cv2

threshold_value = 128
blur_value = 0

def update_threshold(x):
    global threshold_value
    threshold_value = x
def update_blur(x):
    global blur_value
    blur_value = x if x % 2 == 1 else x + 1  # Ensure blur kernel size is odd


def apply_filter(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply blur with the current blur value
    blurred = cv2.GaussianBlur(gray, (blur_value, blur_value), 0)
    
    # Apply thresholding with the current threshold value
    _, filtered_frame = cv2.threshold(blurred, threshold_value, 255, cv2.THRESH_BINARY)
    
    return filtered_frame

def main():
    frame = cv2.imread("test1.bmp")
    cv2.namedWindow('Filtered Frame')
    cv2.createTrackbar('Threshold', 'Filtered Frame', threshold_value, 255, update_threshold)
    cv2.createTrackbar('Blur', 'Filtered Frame', blur_value, 20, update_blur)
    
    while True:
        filtered_frame = apply_filter(frame)
        show_image = cv2.resize(filtered_frame, (720, 540))
        cv2.imshow('Filtered Frame', show_image)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture and destroy windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
