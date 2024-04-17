import pyautogui

# drag get value as an argument along x and y axis for moving the cursor from cursor current position
# pyautogui.drag(20, 20)


# dragTo does not get any effect from cursor position, it will move the cursor whereever position value is given
pyautogui.dragTo(100, 100, button="middle")