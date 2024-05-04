import pyautogui

# to get the cursor location value along x and y axis
pos = pyautogui.position()
print(pos)

# to get the screen size in width and height
siz = pyautogui.size()
print(siz)


# to get the location of screen is present or not using width and height as an argument, it return boolean value
screen = pyautogui.onScreen(1377, 200)
print(screen)