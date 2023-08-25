# Import the OpenCV library
import cv2

# Load an image from the specified file path ('resources\\test.jpg')
image = cv2.imread('resources\\test.jpg')

# Resize the image to a new size (720x480) using the cv2.resize function
resized_image = cv2.resize(image, (720, 480))

# Display the original image in a window titled 'Original Image'
cv2.imshow('Original Image', image)

# Display the resized image in a window titled 'Resized Image'
cv2.imshow('Resized Image', resized_image)

# Wait until any key is pressed before proceeding.
# This delay keeps the windows open, preventing immediate closure.
# The program continues when a key is pressed.
cv2.waitKey(0)

# Close all OpenCV windows, specifically the 'Original Image' and 'Resized Image' windows.
cv2.destroyAllWindows()
