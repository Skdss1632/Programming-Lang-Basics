import pyautogui

# fail_safes uses to remove the error from program if present it will abort or exit
pyautogui.PAUSE = 5
pyautogui.moveTo(100, 200)

# pause will stop the program after execution of program for some time
pyautogui.PAUSE = 5
pyautogui.moveTo(10, 10)







# FAILSAFE is used to disable the fail safe exception i.e -- PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen.
# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 5
pyautogui.moveTo(0, 0)


pyautogui.PAUSE = 5
pyautogui.moveTo(10, 10)
