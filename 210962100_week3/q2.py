import cv2
import numpy as np

# Load the image
image_path = 'C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject(210962100)/210962100_week3/resources/Lenna.png'
image = cv2.imread(image_path)

# Compute the gradient in the x and y directions using Sobel filters
gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
cv2.imshow('title',gradient_x)
cv2.imshow('title1',gradient_y)

# Compute the magnitude and direction of the gradient
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)
gradient_direction = np.arctan2(gradient_y, gradient_x)

# Normalize the gradients for visualization
gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

# Display the original image and the gradient magnitude
cv2.imshow('Original Image', image)
cv2.imshow('Gradient Magnitude', gradient_magnitude_normalized)
cv2.waitKey(0)
cv2.destroyAllWindows()