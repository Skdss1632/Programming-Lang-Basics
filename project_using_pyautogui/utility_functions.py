import pyautogui
import pytesseract
# from PIL import Image
# import schedule
# import time
# import datetime
#
# from selenium.webdriver.edge.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


def click_on_browsers():
    pyautogui.click(x=484, y=1045)


def click_on_login_btn():
    pyautogui.sleep(1)
    pyautogui.click(x=543, y=140)
    # pyautogui.click(x=516, y=194)


def open_new_tab():
    pyautogui.hotkey("ctrl", "t")


def open_url():
    # pyautogui.write("https://www.irctc.co.in/nget/train-search")
    # pyautogui.sleep(3)
    # pyautogui.press('enter')
    # pyautogui.sleep(1)
    url = "https://www.irctc.co.in/nget/train-search"

    # Iterate through each character in the URL and type it slowly
    for char in url:
        pyautogui.write(char)
    pyautogui.press("enter")



# def get_image_txt():
#     # Take a screenshot of the area containing the text
#     # screenshot = pyautogui.screenshot(region=(x, y, 559, 716))   # Adjust x, y, width, height as needed
#
#     # Save the screenshot image temporarily
#     # screenshot.save('screenshot.png')
#
#     # Perform OCR on the saved image
#     text = pytesseract.image_to_string(Image.open('screenshot.png'))
#
#     # Print the extracted text
#     print(text)



def click_on_sinin_btn():
    pyautogui.press("enter")


def click_on_available_btn():
    pyautogui.sleep(1)
    pyautogui.click(x=651, y=603)


def click_on_book_now():
    pyautogui.click(x=546, y=711)


def click_on_passenger_name_input_fld():
    pyautogui.sleep(1)
    pyautogui.click(x=214, y=737)



def select_passenger_name():
    pyautogui.sleep(1)
    pyautogui.click(x=201, y=719)
    pyautogui.press("shift")
    pyautogui.press("down", presses=7)
    pyautogui.press("shift")
    pyautogui.press("enter")


def click_on_book_only_if_confirm_berth_are_alloted_checkbox():
    pyautogui.sleep(1)
    pyautogui.click(x=727, y=374)



def click_on_continue_btn_inside_passenger_details():
    pyautogui.sleep(1)
    pyautogui.click(x=137, y=888)


def click_on_continue_btn_inside_review_journey(sleep_time_to_fill_captcha: int):
    pyautogui.sleep(sleep_time_to_fill_captcha)
    pyautogui.click(130, 450)


def click_on_irctc_ewallet():
    pyautogui.sleep(1)
    pyautogui.click(x=159, y=481)


def click_on_pay_and_book():
    pyautogui.click(x=647, y=548)


def click_on_search_btn():
    pyautogui.sleep(1)
    pyautogui.click(x=238, y=690)


def input_station_name(from_: str, to: str):
    pyautogui.sleep(1)
    pyautogui.click(x=280, y=424)
    clear_input_fld()
    pyautogui.write(from_)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.press("shift")
    pyautogui.press("enter")


    pyautogui.sleep(1)
    pyautogui.click(x=250, y=495)
    clear_input_fld()
    pyautogui.write(to)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.press("shift")
    pyautogui.press("enter")


def select_coach_type_for_booking_from_dropdown(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.sleep(1)
        pyautogui.click(x=691, y=489)
        pyautogui.press("shift")
        pyautogui.press("down", presses=11)
        pyautogui.press("shift")
        pyautogui.press("enter")

    if coach_type == "ac 3 tier":
        pyautogui.sleep(1)
        pyautogui.sleep(1)
        pyautogui.click(x=691, y=489)
        pyautogui.press("shift")
        pyautogui.press("down", presses=7)
        pyautogui.press("shift")
        pyautogui.press("enter")

def select_date_for_tatakal_booking():
    pyautogui.sleep(1)
    pyautogui.click(x=764, y=426)
    clear_input_fld()
    pyautogui.write("01/08/2024")
    pyautogui.press("enter")


def clear_input_fld():
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')


def select_tatkal_from_dropdown():
    pyautogui.sleep(1)
    pyautogui.click(x=255, y=561)
    pyautogui.click(x=255, y=764)


def select_coach_type_for_booking(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.sleep(1)
        pyautogui.click(x=617, y=571)


def input_username_and_password_of_irctc_account(username: str, password: str):
    pyautogui.sleep(3)
    pyautogui.click(x=537, y=317)
    pyautogui.sleep(2)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')
    pyautogui.write(username)

    pyautogui.sleep(2)
    pyautogui.click(x=514, y=361)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')
    pyautogui.write(password)


def scroll_to_continue_btn(no_of_scroll: float):
    pyautogui.scroll(no_of_scroll)

def click_and_pay():
    pyautogui.sleep(1)
    pyautogui.click(771, 883)


def wait_until_image_found(image_path):
    while True:
        try:
            if pyautogui.locateCenterOnScreen(image_path, confidence=0.90) is not None:
                return True
        except pyautogui.ImageNotFoundException:
            # Image not found, continue loop
            pass


















