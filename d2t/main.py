import PIL
import pyautogui
import keyboard
import pytesseract
import cv2
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
crop_box = (550, 600, 1400, 800)


def take_screenshot() -> PIL.Image:
    screenshot = pyautogui.screenshot()
    cropped_image = screenshot.crop(crop_box)
    return cropped_image


def extract_text(image: PIL.Image) -> str:
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    cv2.imwrite("gray_image.png", image)
    custom_config = r"--oem 3 --psm 6 -l rus"
    text = pytesseract.image_to_string(image, config=custom_config)
    return text


def main():
    image = take_screenshot()
    text = extract_text(image)
    print(text)


if __name__ == "__main__":
    keyboard.add_hotkey("ctrl+shift+s", main)
    print("Press Ctrl + Shift + S to take a cropped screenshot...")
    keyboard.wait("esc")  # Wait until ESC is pressed
