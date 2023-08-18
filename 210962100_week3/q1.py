import cv2
import numpy as np

# Load the image
image = cv2.imread('C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject(210962100)/210962100_week3/resources/Lenna.png')

# Apply Gaussian blur with smaller kernel and sigma
blurred = cv2.GaussianBlur(image, (3, 3), 1)

# Create a high-pass image
high_pass = cv2.subtract(image , blurred)

# Adjust the strength of sharpening (multiplication approach)
sharpened = cv2.add(image , high_pass)

# Display or save the result
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred)
cv2.imshow('Sharpened Image', sharpened/255)
cv2.waitKey(0)
cv2.destroyAllWindows()
