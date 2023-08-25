# Import the OpenCV library
import cv2

# Load an image from the specified file path ('resources\\test.jpg') in color mode (1 indicates cv2.IMREAD_COLOR)
image = cv2.imread('resources\\test.jpg', 1)

# Display the loaded image in a window titled 'test'
cv2.imshow('test', image)

# Print the dimensions of the image (rows, columns, and channels)
# For a colored image, the dimensions are represented as (height, width, channels). Channels indicate the color components (3 for RGB).
print("Image dimensions: Height:", image.shape[0], ", Width:", image.shape[1], ", Channels:", image.shape[2])

# Extract the color values (BGR) of a specific pixel in the image (row: 100, column: 100)
blue_value, green_value, red_value = image[100, 100]

# Print the RGB values of the pixel at (100, 100) in the image
print("RGB Values")
print("Red:", red_value, "\nGreen:", green_value, "\nBlue:", blue_value)

# Note: OpenCV uses BGR color order by default, where 'blue_value' refers to the blue value, 'green_value' to green,
# and 'red_value' to red at that specific pixel location.
