import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image = cv2.imread("tests/cropped_screenshot_test.png")

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imwrite("gray_image.png", image)
custom_config = r"--oem 3 --psm 6 -l rus"
text = pytesseract.image_to_string(image, config=custom_config)

print("Extracted Text:")
print(text)
