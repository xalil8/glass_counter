import cv2

# Global variable to store filter threshold value
threshold_value = 128

# Callback function for threshold slider
def update_threshold(x):
    global threshold_value
    threshold_value = x

def apply_filter(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding with the current threshold value
    _, filtered_frame = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    
    return filtered_frame


def main():


    frame = cv2.imread("test1.bmp")
    cv2.namedWindow('Filtered Frame')
    
    # Create a trackbar for threshold
    cv2.createTrackbar('Threshold', 'Filtered Frame', threshold_value, 255, update_threshold)
    
    while True:
        filtered_frame = apply_filter(frame)
        



        show_image = cv2.resize(filtered_frame,(720,540))
        cv2.imshow('Filtered Frame', show_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture and destroy windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
