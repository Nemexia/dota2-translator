import pyautogui
import keyboard

crop_box = (550, 600, 1400, 800)


def take_screenshot():
    screenshot = pyautogui.screenshot()
    cropped_image = screenshot.crop(crop_box)
    cropped_image.save("cropped_screenshot.png")
    print("Screenshot saved as cropped_screenshot.png")


keyboard.add_hotkey("ctrl+shift+s", take_screenshot)
print("Press Ctrl + Shift + S to take a cropped screenshot...")
keyboard.wait("esc")
