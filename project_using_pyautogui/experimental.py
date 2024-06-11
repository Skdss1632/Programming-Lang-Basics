
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *

click_browser()
py.sleep(3)
def click_enter_captcha_fld():
    enter_captcha_fld_img = get_image_path(config["image_paths"]["enter_captcha_fld_image"])
    enter_captcha_fld_img_location = py.locateCenterOnScreen(image=enter_captcha_fld_img, confidence=0.90, minSearchTime=25)
    py.click(enter_captcha_fld_img_location)
    print(enter_captcha_fld_img_location)

click_enter_captcha_fld()