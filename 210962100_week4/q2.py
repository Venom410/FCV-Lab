import cv2
import numpy as np

# Path to the input image
image_path = 'resources/Table.jfif'

# Read the input image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detector to the grayscale image
edges = cv2.Canny(gray_image, 50, 150, apertureSize=3)

# Detect lines using the Hough Line Transform
# Parameters:
# - edges: The edge-detected image
# - 1: Distance resolution of the accumulator in pixels
# - np.pi / 180: Angle resolution of the accumulator in radians
# - threshold=100: Minimum number of votes (threshold) to consider a line
lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

# Create a copy of the original image to draw lines on
image_with_lines = image.copy()

# Draw the detected lines on the image
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image_with_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Display the original and processed images
cv2.imshow('Original Image', image)
cv2.imshow('Detected Lines', image_with_lines)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
