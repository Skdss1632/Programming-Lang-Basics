import pyautogui

# move get value as an argument along x and y axis for moving the cursor from cursor current position
pyautogui.move(100, 0)


# moveTo does not get any effect from cursor position, it will move the cursor whereever position value is given
pyautogui.moveTo(100, 0)