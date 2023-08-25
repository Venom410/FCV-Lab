import cv2
import numpy as np

# Path to the image file
img_path = 'resources/Lenna.png'

# Read the image using OpenCV
image = cv2.imread(img_path)

# Convert the image from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the color range you want to segment
lower_color = np.array([0, 150, 150])  # Lower bound for hue, saturation, and value
upper_color = np.array([30, 255, 255])  # Upper bound for hue, saturation, and value

# Create a mask where pixels within the specified color range become white and others become black
color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

# Apply the color mask to the original image to obtain the segmented result
segmented_image = cv2.bitwise_and(image, image, mask=color_mask)

# Display the original image, the color mask, and the segmented result
cv2.imshow('Original Image', image)
cv2.imshow('Color Mask', color_mask)
cv2.imshow('Segmented Image', segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
