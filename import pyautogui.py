import pyautogui
import time

#This is going to start the program at the Search Stock textbox
time.sleep(2)
pyautogui.moveTo(318, 501, 2)
pyautogui.click()
pyautogui.write("AAPL")
pyautogui.moveTo(469, 466)
pyautogui.click()
pyautogui.hotkey("tab")
time.sleep(1)
pyautogui.write("AAPL")
pyautogui.hotkey("tab")
pyautogui.write("165")
time.sleep(1)
pyautogui.hotkey("tab")
pyautogui.write("10")
time.sleep(2)
pyautogui.hotkey("tab")
pyautogui.write("1650")
pyautogui.moveTo(49,301, 1)
pyautogui.click()
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
pyautogui.write("04-24-2023")
pyautogui.moveTo(36, 377, 1)
pyautogui.click()
pyautogui.moveTo(365, 429, 1)
time.sleep(3)
pyautogui.moveTo(318, 501, 1)
pyautogui.click()



#shows the current position of the mouse
#print(pyautogui.position())