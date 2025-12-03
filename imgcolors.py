import cv2

# import imutils

# Read image in grayscale
image = cv2.imread('ss/zzee.jpg', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError("Could not load image at path 'ss/zzee.jpg'")

cv2.imshow('Original (Grayscale)', image)

# Convert grayscale image to 3-channel BGR so we can manipulate color channels
gray_img = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.imshow('Gray as BGR', gray_img)

# Keep only the red channel (set blue and green to 0)
gray_img[:, :, 0] = 0  # Blue channel
gray_img[:, :, 1] = 0  # Green channel

cv2.imshow('Red Channel Only', gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()