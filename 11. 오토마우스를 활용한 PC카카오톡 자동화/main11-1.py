import pyautogui
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

picPosition = pyautogui.locateOnScreen('pic1.png')
print(picPosition)

if picPosition is None:
	picPosition = pyautogui.locateOnScreen('pic2.png')
	print(picPosition)
