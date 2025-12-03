import cv2
import numpy as np

# Read image
image = cv2.imread('ss/zzee.jpg')

if image is None:
    print("Error: Could not read the image. Make sure the path is correct.")
else:
    hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    try:
        saturation_value = int(input('Enter saturation channel value to add (e.g., 50 for increase, -50 for decrease): '))

        # Split the HSV image into H, S, and V channels
        h, s, v = cv2.split(hsv_img)

        # Add the saturation value to the S channel
        # Use np.clip to keep the values in the 0-255 range
        s = np.clip(s.astype(np.int16) + saturation_value, 0, 255).astype(np.uint8)

        # Merge the channels back
        final_hsv = cv2.merge((h, s, v))

        # Convert the HSV image back to BGR
        saturated_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

        # Display the original and saturated images
        cv2.imshow('Original Image', image)
        cv2.imshow('Saturated Image', saturated_img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except ValueError:
        print("Invalid input. Please enter an integer.")
