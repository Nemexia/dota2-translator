import pyautogui
import cv2
import numpy as np
import keyboard

# Define crop area (left, top, right, bottom)
crop_box = (550, 600, 1400, 800)  # Change these values as needed

def take_screenshot():
    screenshot = pyautogui.screenshot()  # Take a screenshot
    cropped_image = screenshot.crop(crop_box)  # Crop the screenshot
    cropped_image.save("cropped_screenshot.png")  # Save the image
    print("Screenshot saved as cropped_screenshot.png")

# Set hotkey (e.g., Ctrl + Shift + S)
keyboard.add_hotkey("ctrl+shift+s", take_screenshot)

print("Press Ctrl + Shift + S to take a cropped screenshot...")
keyboard.wait("esc")  # Keep script running until you press 'Esc'
