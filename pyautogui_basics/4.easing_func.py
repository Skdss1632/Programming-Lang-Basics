import pyautogui

# easing func we can pass in moveTo function

# pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad) # start slow, end fast
#
pyautogui.moveTo(200, 200, 1, pyautogui.easeOutQuad) # strat fast, end slow
#
# pyautogui.moveTo(300, 300, 2, pyautogui.easeInOutQuad) # start and end fast, slow in the middle
#
#
# pyautogui.moveTo(400, 400, 2, pyautogui.easeInBounceQuad) # bounce at the end


# pyautogui.moveTo(500, 500, 2, pyautogui.easeInElastic) # rubber band at the end
