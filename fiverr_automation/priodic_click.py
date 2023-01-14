import pyautogui as pui
import time
from datetime import datetime as dt
import random

# Move the mouse to the point
pui.moveTo(100, 200)

# Click the left mouse button
pui.click()

pui.click(button='right')

while(True):
    pui.moveTo(100, 100)
    pui.click()

    random_sleep_time = random.uniform(30, 60)
    time.sleep(random_sleep_time)
    print(dt.now())
