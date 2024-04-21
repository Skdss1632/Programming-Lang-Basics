import pyautogui
import pytesseract
# from PIL import Image
# import schedule
# import time
# import datetime


def click_browsers():
    pyautogui.click(x=484, y=1045)


def click_on_login_btn():
    pyautogui.sleep(1)
    pyautogui.click(x=543, y=140)


def open_new_tab():
    pyautogui.hotkey("ctrl", "t")


def open_url():
    # pyautogui.write("https://www.irctc.co.in/nget/train-search")
    # pyautogui.sleep(3)
    # pyautogui.press('enter')
    # pyautogui.sleep(1)
    url = "https://www.irctc.co.in/nget/train-search"
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


def click_available_btn():
    pyautogui.click(x=651, y=603)


def click_book_now():
    pyautogui.click(x=546, y=711)


def click_passenger_name_fld():
    pyautogui.click(x=214, y=737)


def select_passenger_name(input_passenger_name_index: int):
    pyautogui.click(x=201, y=719)
    pyautogui.press("shift")
    pyautogui.press("down", presses=input_passenger_name_index)
    pyautogui.press("shift")
    pyautogui.press("enter")


def click_book_only_if_confirm_berth_alloted():
    pyautogui.click(x=727, y=374)


def click_continue_btn_inside_passenger_details():
    pyautogui.click(x=137, y=888)


def click_continue_btn_inside_review_journey(captcha_fill_delay: int, image_path: str):
    pyautogui.sleep(captcha_fill_delay)
    button_location = pyautogui.locateCenterOnScreen(image_path)
    pyautogui.click(button_location)


def click_irctc_e_wallet():
    pyautogui.click(x=159, y=481)


def click_search_btn():
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
    # pyautogui.hotkey('shift', 'down', 'shift', 'enter')

    pyautogui.sleep(1)
    pyautogui.click(x=250, y=495)
    clear_input_fld()
    pyautogui.write(to)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.press("shift")
    pyautogui.press("enter")


def tatkal_booking_date(tatkal_booking_date: str):
    pyautogui.click(x=764, y=426)
    clear_input_fld()
    pyautogui.write(tatkal_booking_date)
    pyautogui.press("enter")


def clear_input_fld():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')


def select_tatkal_from_dropdown():
    # pyautogui.sleep(1)
    pyautogui.click(x=255, y=561)
    pyautogui.click(x=255, y=764)


def select_coach_type_for_booking(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.click(x=617, y=571)


def input_username_irctc_account(username: str, username_image_path: str):
    username_fld = pyautogui.locateCenterOnScreen(username_image_path)
    pyautogui.click(username_fld)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')
    pyautogui.write(username)


def input_password_irctc_account(password: str, password_image_path: str):
    password_fld = pyautogui.locateCenterOnScreen(password_image_path)
    pyautogui.click(password_fld)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')
    pyautogui.write(password)


def login_irctc_account(username: str, password: str, captcha_fill_delay: int):
    click_on_login_btn()
    pyautogui.sleep(2)
    if wait_until_image_visible(image_path="/home/intern/Pictures/Screenshots/username_fld.png"):
        input_username_irctc_account(username=username, username_image_path="/home/intern/Pictures/Screenshots/username_fld.png")

    if wait_until_image_visible(image_path="/home/intern/Pictures/Screenshots/password_fld.png"):
        input_password_irctc_account(password=password, password_image_path="/home/intern/Pictures/Screenshots/password_fld.png")

    pyautogui.sleep(captcha_fill_delay)
    click_on_sinin_btn()


def input_journey_details(from_: str, to: str, booking_date: str):
    input_station_name(from_=from_, to=to)
    # select_tatkal_from_dropdown()
    tatkal_booking_date(booking_date)
    click_search_btn()


def open_chrome_browser_with_irctc_page():
    click_browsers()
    open_new_tab()
    open_url()


def scroll_to_continue_btn(no_of_scroll: float):
    pyautogui.scroll(no_of_scroll)


def click_pay_and_book():
    pyautogui.click(771, 883)


def wait_until_image_visible(image_path):
    while True:
        try:
            if pyautogui.locateCenterOnScreen(image_path, confidence=0.80) is not None:
                return True
        except pyautogui.ImageNotFoundException:
            # Image not found, continue loop
            pass


def click_confirm_btn_inside_otp(otp_fill_delay: int):
    pyautogui.sleep(otp_fill_delay)
    pyautogui.click(711, 541)


def close_login_popup():
    pyautogui.click(1494, 229)
    click_on_login_btn()









