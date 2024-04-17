import pyautogui
import pyautogui
import pytesseract
from PIL import Image
from future.moves import sys


def click_on_browsers():
    pyautogui.click(x=21, y=125)


def click_on_login_btn():
    pyautogui.moveTo(543, 140)
    pyautogui.sleep(2)
    pyautogui.click()


def open_new_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')



def open_url():
    pyautogui.write("https://www.irctc.co.in/nget/train-search")
    pyautogui.sleep(3)
    pyautogui.press('enter')


def get_image_txt():
    # Take a screenshot of the area containing the text
    # screenshot = pyautogui.screenshot(region=(x, y, 559, 716))   # Adjust x, y, width, height as needed

    # Save the screenshot image temporarily
    # screenshot.save('screenshot.png')

    # Perform OCR on the saved image
    text = pytesseract.image_to_string(Image.open('screenshot.png'))

    # Print the extracted text
    print(text)


def click_on_sinin_btn():
    pyautogui.moveTo(639, 867)
    pyautogui.sleep(2)
    pyautogui.click()


def click_on_avalible_btn():
    pyautogui.click(x=644, y=599)


def click_on_book_now():
    pyautogui.click(x=600, y=709)


def click_on_passenger_name_input_fld():
    pyautogui.click(x=156, y=676)


def select_passenger_name():
    pyautogui.click(x=201, y=719)


def click_on_book_only_if_confirm_berth_are_alloted_checkbox():
    pyautogui.click(x=563, y=588)


def click_on_continue_btn_inside_passenger_details():
    pyautogui.click(x=213, y=621)


def click_on_continue_btn_inside_review_journey(sleep_time_to_fill_captcha: int):
    pyautogui.sleep(sleep_time_to_fill_captcha)
    pyautogui.click(x=230, y=603)


def click_on_irctc_ewallet():
    pyautogui.click(x=220, y=482)


def click_on_pay_and_book():
    pyautogui.click(x=647, y=548)


def click_on_search_btn():
    pyautogui.moveTo(238, 690)
    pyautogui.sleep(1)
    pyautogui.click()


def input_station_name(catch_train_station_name: str, to: str):
    pyautogui.moveTo(309, 422)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.write(catch_train_station_name)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.press("enter")


    pyautogui.moveTo(247, 498)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.write(to)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.press("enter")


def select_coach_type_for_booking_from_dropdown(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.moveTo(714, 494)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.press("shift")
        pyautogui.sleep(2)
        pyautogui.press("down", presses=11)
        pyautogui.sleep(2)
        pyautogui.press("shift")
        pyautogui.press("enter")

    if coach_type == "ac 3 tier":
        pyautogui.moveTo(714, 494)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.press("shift")
        pyautogui.sleep(2)
        pyautogui.press("down", presses=7)
        pyautogui.sleep(2)
        pyautogui.press("shift")
        pyautogui.press("enter")

def select_date_for_tatakal_booking():
    pyautogui.moveTo(690, 423)
    pyautogui.click()
    pyautogui.sleep(2)
    pyautogui.moveTo(850, 647)
    pyautogui.click()
    pyautogui.sleep(2)


def select_tatkal_from_dropdown():
    pyautogui.moveTo(255, 561)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(255, 764)
    pyautogui.sleep(1)
    pyautogui.click()



def select_coach_type_for_booking(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.moveTo(597, 567)
        pyautogui.sleep(1)
        pyautogui.click()


def click_on_username_input_fld():
    pyautogui.moveTo(611, 341)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.press("shift")
    pyautogui.sleep(1)
    pyautogui.press("down")
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.press("enter")












