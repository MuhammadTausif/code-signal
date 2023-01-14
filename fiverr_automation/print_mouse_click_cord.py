import pyautogui

def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at {x}, {y}')

pyautogui.onClick(on_click)
