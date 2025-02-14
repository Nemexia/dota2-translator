import pyautogui
import cv2
import numpy as np

screenshot = pyautogui.screenshot()
image = np.array(screenshot)  # Convert to NumPy array
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV

cv2.imwrite("screenshot.png", image)
