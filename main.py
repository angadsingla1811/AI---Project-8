#Resizing, rotating, brightening, and cropping an image using OpenCV in Python
import cv2

# Load the image
image = cv2.imread("image.jpg")

# 1. Rotate the image 90 degrees
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# 2. Brighten the image
brightened = cv2.convertScaleAbs(image, alpha=1.2, beta=50)

# 3. Crop a section of the image
cropped = image[50:300, 100:400]

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)
cv2.imshow("Brightened Image", brightened)
cv2.imshow("Cropped Image", cropped)

# Save the manipulated images
cv2.imwrite("rotated_image.jpg", rotated)
cv2.imwrite("brightened_image.jpg", brightened)
cv2.imwrite("cropped_image.jpg", cropped)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()