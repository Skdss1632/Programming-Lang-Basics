import pyautogui
import pyautogui
import pytesseract
from PIL import Image
from future.moves import sys

print(sys.path)

def click_on_login_btn():
    pyautogui.click(x=555, y=140)


def click_on_browsers():
    pyautogui.click(x=21, y=125)


def click_on_new_tab():
    pyautogui.click(x=220, y=264)


def get_image_txt():
    # Take a screenshot of the area containing the text
    screenshot = pyautogui.screenshot(region=(x, y, 559, 716))   # Adjust x, y, width, height as needed

    # Save the screenshot image temporarily
    screenshot.save('screenshot.png')

    # Perform OCR on the saved image
    text = pytesseract.image_to_string(Image.open('screenshot.png'))

    # Print the extracted text
    print(text)


def click_on_sinin_btn():
    pyautogui.click(x=614, y=873)


def click_on_sleeper_btn(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.click(x=601, y=572)
    else:
        pyautogui.click(x=916, y=548)


def click_on_avalible_btn():
    pyautogui.click(x=644, y=599)


def click_on_book_now():
    pyautogui.click(x=600, y=709)


def click_on_passenger_name():
    pyautogui.click(x=218, y=554)


def click_on_passenger_name():
    pyautogui.click(x=179, y=848)


def click_on_book_only_if_confirm_berth_are_alloted_checkbox():
    pyautogui.click(x=563, y=588)


def click_on_continue_btn_inside_passenger_details():
    pyautogui.click(x=213, y=621)


def click_on_continue_btn_inside_review_journey():
    pyautogui.click(x=230, y=603)


def click_on_irctc_ewallet():
    pyautogui.click(x=220, y=482)


def click_on_pay_and_book():
    pyautogui.click(x=647, y=548)






