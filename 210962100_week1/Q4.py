# Import the OpenCV library with the alias 'cv'
import cv2 as cv

# Import the NumPy library with the alias 'np'
import numpy as np

# Define a color using BGR format (Blue, Green, Red)
color = (120, 120, 120)

# Define two points 'p0' and 'p1' to specify the rectangle's corners
# 'p0' represents the top-left corner (x=200, y=10)
# 'p1' represents the bottom-right corner (x=400, y=90)
p0 = 200, 10
p1 = 400, 90

# Create an image (numpy array) filled with zeros (black) with dimensions 400x1000 and 3 color channels (BGR)
# The data type 'np.uint8' signifies unsigned 8-bit integers (range: 0 to 255)
img = np.zeros((400, 1000, 3), np.uint8)

# Draw a rectangle on the 'img' using the defined points 'p0' and 'p1', along with the specified color and thickness=2
# The color (120, 120, 120) signifies gray due to equal BGR values.
cv.rectangle(img, p0, p1, color, 2)

# Display the 'img' in a window titled 'Rectangle'
cv.imshow('Rectangle', img)

# Wait until any key is pressed before proceeding.
# This delay keeps the window open, preventing immediate closure.
# The program will continue execution upon a key press.
cv.waitKey(0)

# Close all OpenCV windows, specifically the 'Rectangle' window.
cv.destroyAllWindows()
