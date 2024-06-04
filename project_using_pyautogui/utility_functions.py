import pyautogui
import pytesseract
# from PIL import Image
# import schedule
# import time
# import datetime
parent_img_path = "/home/intern/Pictures/Screenshots/"


def click_browsers():
    browser_location = pyautogui.locateCenterOnScreen(image=parent_img_path + "chrome.png", confidence=0.80, minSearchTime=5)
    pyautogui.click(browser_location)


def click_on_login_btn():
    pyautogui.sleep(1)
    pyautogui.click(x=543, y=140)


def open_new_tab():
    pyautogui.hotkey("ctrl", "t")


def open_url():
    pyautogui.write("https://www.irctc.co.in/nget/train-search", interval=0.1)


def click_on_sinin_btn():
    pyautogui.press("enter")


def click_available_btn(img_path: str):
    pyautogui.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(x=651, y=603)


def click_book_now(img_path: str):
    book_now_location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(book_now_location)


def input_passenger_name(passenger_name: str):
    try:
        pyautogui.locateCenterOnScreen(image=parent_img_path + "india.png", confidence=0.90, minSearchTime=1)

    except pyautogui.ImageNotFoundException:
        location = pyautogui.locateCenterOnScreen(image=parent_img_path + "cross.png", confidence=0.90, minSearchTime=5)
        pyautogui.click(location)
        add_location = pyautogui.locateCenterOnScreen(image=parent_img_path + "add_passenger.png", confidence=0.90, minSearchTime=5)
        pyautogui.click(add_location)

    pyautogui.sleep(0.1)
    pyautogui.click(147, 739)
    pyautogui.typewrite(message=passenger_name, interval=0.2)
    pyautogui.sleep(1)
    pyautogui.press("down")
    pyautogui.press("enter")
    # pyautogui.locateCenterOnScreen(image=parent_img_path + "filled_pass_name.png", confidence=0.90, minSearchTime=3)


def click_book_only_if_confirm_berth_alloted(img_path: str):
    scroll_until_train_name_image_visible(img_path=img_path)
    txt_location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(txt_location)


def click_continue_btn_inside_passenger_details(continue_btn_img_path: str):
    scroll_until_train_name_image_visible(img_path=continue_btn_img_path)
    btn_location = pyautogui.locateCenterOnScreen(image=continue_btn_img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(btn_location)


def click_continue_btn_inside_review_journey(captcha_fill_delay: int, img_path: str):
    scroll_until_train_name_image_visible(img_path=img_path)
    pyautogui.sleep(captcha_fill_delay)
    button_location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(button_location)


def click_irctc_e_wallet(img_path: str):
    pyautogui.sleep(1)
    wallet_location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=10)
    pyautogui.click(wallet_location)


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


    pyautogui.sleep(1)
    pyautogui.click(x=250, y=495)
    clear_input_fld()
    pyautogui.write(to)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.press("shift")
    pyautogui.press("enter")


def tatkal_booking_date(tatkal_book_date: str):
    pyautogui.click(x=764, y=426)
    clear_input_fld()
    pyautogui.write(tatkal_book_date)
    pyautogui.press("enter")


def clear_input_fld():
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')


def select_ticket_type_from_dropdown(image_path: str):
    pyautogui.sleep(1)
    if image_path == "general.png":
        pass  # Do nothing for "general.png"
    else:
        pyautogui.click(255, 561)

    if image_path == "premium_tatkal.png":
        pyautogui.moveTo(237, 633)
        pyautogui.scroll(-1)

    ticket_type_location = pyautogui.locateCenterOnScreen(image=image_path, confidence=0.90, minSearchTime=5)
    pyautogui.click(ticket_type_location)



def input_username_irctc_account(username: str, username_image_path: str):
    # username_fld = pyautogui.locateCenterOnScreen(image=username_image_path, confidence=0.90, minSearchTime=10)
    # pyautogui.click(username_fld)
    pyautogui.click(705, 935)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')
    pyautogui.write(username)


def input_password_irctc_account(password: str, password_image_path: str):
    # password_fld = pyautogui.locateCenterOnScreen(image=password_image_path, confidence=0.90, minSearchTime=10)
    # pyautogui.click(password_fld)
    pyautogui.click(555, 355)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press('backspace')
    pyautogui.write(password)


def login_irctc_account(username: str, password: str, captcha_fill_delay: int, img_path: str):
    click_on_login_btn()
    pyautogui.sleep(2)
    pyautogui.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    input_username_irctc_account(username=username, username_image_path=parent_img_path + "username_fld.png")
    input_password_irctc_account(password=password, password_image_path=parent_img_path + "password_fld.png")
    pyautogui.sleep(captcha_fill_delay)
    click_on_sinin_btn()


def input_journey_details(from_: str, to: str, booking_date: str, ticket_type_img_path: str):
    input_station_name(from_=from_, to=to)
    select_ticket_type_from_dropdown(image_path=ticket_type_img_path)
    tatkal_booking_date(booking_date)


def open_chrome_browser_with_irctc_page():
    click_browsers()
    open_new_tab()
    open_url()


def scroll_to_view(no_of_scroll: float):
    pyautogui.scroll(no_of_scroll)


def click_pay_n_book(img_path: str):
    pay_n_book_location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(pay_n_book_location)


def wait_until_image_visible(image_path: str):
    while True:
        try:
            if pyautogui.locateCenterOnScreen(image_path, confidence=0.80) is not None:
                return True
        except pyautogui.ImageNotFoundException:
            # Image not found, continue loop
            pass


def click_confirm_btn_inside_otp(otp_fill_delay: int, img_path: str):
    pyautogui.sleep(otp_fill_delay)
    btn_location = pyautogui.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=10)
    pyautogui.click(btn_location)


def close_login_popup():
    pyautogui.click(1494, 229)
    click_on_login_btn()


def scroll_until_train_name_image_visible(img_path: str):
    i = -1
    while True:
        i -= 1
        scroll_to_view(no_of_scroll=i)
        try:
            if pyautogui.locateCenterOnScreen(image=img_path, confidence=0.80) is not None:
                return True
        except pyautogui.ImageNotFoundException:
            # Image not found, continue loop
            pass


def select_train_for_booking(train_name_img_path: str, coach_type_img_path: str, wl_or_available_img_path: str):
    scroll_until_train_name_image_visible(img_path=train_name_img_path)
    # pass img path of train name with time and sleeper visible
    coach_type_location = pyautogui.locateCenterOnScreen(image=coach_type_img_path, confidence=0.90, minSearchTime=10)
    pyautogui.click(coach_type_location)
    wl_or_available_location = pyautogui.locateCenterOnScreen(image=wl_or_available_img_path, confidence=0.90,
                                                        minSearchTime=10)
    pyautogui.click(wl_or_available_location)
    img_path: str = parent_img_path + "book_now.png"
    click_book_now(img_path=img_path)











