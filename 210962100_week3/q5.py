import cv2

# Load the image
image_path = 'C:/Users/ugcse.PG-CP.000/PycharmProjects/pythonProject(210962100)/210962100_week3/resources/Lenna.png'
image = cv2.imread(image_path)

# Perform Canny edge detection
edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Display the original image and the detected edges
cv2.imshow('Original Image', image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
