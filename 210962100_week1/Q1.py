# Import the OpenCV library
import cv2

# Load an image from the provided file path ('resources\\test.jpg') in color mode (cv2.IMREAD_COLOR)
loaded_image = cv2.imread('resources\\test.jpg', cv2.IMREAD_COLOR)

# Display the loaded image in a window titled 'image'
cv2.imshow('Loaded Image', loaded_image)

# Wait until any key is pressed before continuing.
# This delay keeps the window open to prevent immediate closure.
# The program proceeds once a key is pressed.
cv2.waitKey(0)

# Close all OpenCV windows, including the 'Loaded Image' window.
cv2.destroyAllWindows()

# Save the loaded image as a new file ('resources\\test1.jpg') while preserving its content.
# This action creates a duplicate of the original image, saved as 'test1.jpg' in the 'resources' folder.
cv2.imwrite('resources\\test1.jpg', loaded_image)
