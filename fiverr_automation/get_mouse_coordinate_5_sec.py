import pyautogui as pui
import time as t
from datetime import datetime as dt

while (True):
    t.sleep(5)
    print(pui.position(), dt.now())
