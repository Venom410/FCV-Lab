import cv2

# Read the image from the specified file path ('resources\\test.jpg')
image = cv2.imread('resources\\test.jpg')

# Get the center coordinates and angle of rotation
center = (image.shape[1] // 2, image.shape[0] // 2)  # (x, y) format
angle = 90  # Angle of rotation in degrees (positive for counter-clockwise)

# Get the rotation matrix using cv2.getRotationMatrix2D
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale=1.0)

# Perform the rotation using cv2.warpAffine
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Display the original and rotated images
cv2.imshow('Original Image', image)
cv2.imshow('Rotated Image', rotated_image)

# Wait until any key is pressed before proceeding.
# This delay keeps the windows open, preventing immediate closure.
# The program continues when a key is pressed.
cv2.waitKey(0)

# Close all OpenCV windows, specifically the 'Original Image' and 'Rotated Image' windows.
cv2.destroyAllWindows()
