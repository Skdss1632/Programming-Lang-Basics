import pyautogui

pyautogui.sleep(3)
# negative value will scroll downside and positive will upside
pyautogui.scroll(-1000)


pyautogui.sleep(3)
pyautogui.scroll(-1000)

# these can't work on windows
pyautogui.hscroll()
pyautogui.vscroll()