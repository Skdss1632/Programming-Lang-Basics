import pyautogui as py
import pytesseract
from PIL import Image
import schedule
import time
import datetime
parent_img_path = "/home/intern/Documents/gitlearning/Programming_Lang_Basics/project_using_pyautogui/irctc_images/"


def click_browsers():
    browser_location = py.locateCenterOnScreen(image=parent_img_path + "chrome.png", confidence=0.80, minSearchTime=5)
    py.click(browser_location)


def open_url():
    py.write("https://www.irctc.co.in/nget/train-search", interval=0.1)
    py.press("enter")


def click_available_btn(img_path: str):
    py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    py.click(x=651, y=603)


def click_book_now(book_now_img_path: str):
    book_now_location = py.locateCenterOnScreen(image=book_now_img_path, confidence=0.90, minSearchTime=10)
    py.click(book_now_location)

def click_on_wl_or_avalible_btn(wl_or_available_img_path: str):
    wl_or_available_location = py.locateCenterOnScreen(image=wl_or_available_img_path, confidence=0.90,
                                                       minSearchTime=10)
    py.click(wl_or_available_location)

def select_passenger_from_master_lst(passenger_detail_img_path: str):
    # Select passenger name by index and navigate
    py.locateCenterOnScreen(image=passenger_detail_img_path, confidence=0.90, minSearchTime=15)
    #
    input_passenger_name(passenger_name="SO")


def input_passenger_name(passenger_name: str):
    py.scroll(-1)
    try:
        py.locateCenterOnScreen(image=parent_img_path + "india.png", confidence=0.90, minSearchTime=10)

    except py.ImageNotFoundException:
        cross_location = py.locateCenterOnScreen(image=parent_img_path + "cross.png", confidence=0.90, minSearchTime=5)
        py.click(cross_location)
        add_passenger_location = py.locateCenterOnScreen(image=parent_img_path + "add_passenger.png", confidence=0.90, minSearchTime=5)
        py.click(add_passenger_location)

    passenger_name_input_fld_location = py.locateOnScreen(image=parent_img_path + "passenger_name_input_fld.png",
                                                          confidence=0.75,
                                                          minSearchTime=5)
    py.click(passenger_name_input_fld_location)
    passenger_name_location = py.locateOnScreen(image=parent_img_path + "passenger_name_from_dropdown.png",
                                                confidence=0.80,
                                                minSearchTime=5)
    py.click(passenger_name_location)

    # py.sleep(0.1)
    # # click on passenger name fld
    # py.click(147, 739)
    # py.sleep(0.1)
    # # 0.118 s == 118 milliseconds
    # py.typewrite(message=passenger_name, interval=0.1)
    # py.sleep(0.125)
    # py.press("down")
    # py.sleep(0.1)
    # py.press("enter")
    # # py.locateCenterOnScreen(image=parent_img_path + "filled_pass_name.png", confidence=0.90, minSearchTime=3)






def click_book_only_if_confirm_berth_alloted(img_path: str):
    scroll_until_element_visible_not_visible(img_path=img_path)
    txt_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    py.click(txt_location)


def click_continue_btn_inside_passenger_details(continue_btn_img_path: str):
    scroll_until_element_visible_not_visible(img_path=continue_btn_img_path)
    btn_location = py.locateCenterOnScreen(image=continue_btn_img_path, confidence=0.90, minSearchTime=10)
    py.click(btn_location)


def click_continue_btn_inside_review_journey(captcha_fill_delay: int, img_path: str):
    scroll_until_element_visible_not_visible(img_path=img_path)
    py.sleep(captcha_fill_delay)
    button_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    py.click(button_location)


def click_irctc_e_wallet(img_path: str):
    wallet_location = py.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=10)
    py.click(wallet_location)


def click_search_btn():
    py.press("enter")


def input_station_name(from_: str, to: str):
    py.sleep(1)
    py.click(x=280, y=424)
    clear_input_fld()
    py.write(from_)
    py.press("shift")
    py.press("down")
    py.press("shift")
    py.press("enter")


    py.sleep(1)
    py.click(x=250, y=495)
    clear_input_fld()
    py.write(to)
    py.press("shift")
    py.press("down")
    py.press("shift")
    py.press("enter")


def input_booking_date(tatkal_book_date: str):
    py.click(x=764, y=426)
    clear_input_fld()
    py.write(tatkal_book_date)
    py.press("enter")


def clear_input_fld():
    py.hotkey("ctrl", "a")
    py.press('backspace')


def select_ticket_type_from_dropdown(ticket_type_img_path: str, ticket_type_for_book: str):
    # if image_path == "general.png":
    #     pass  # Do nothing for "general.png"
    # else:
    #     py.click(255, 561)
    #
    # if image_path == "premium_tatkal.png":
    #     py.moveTo(237, 633)
    #     py.scroll(-1)

    if ticket_type_for_book == "general.png":
        pass  # Do nothing for "general.png"

    else:
        # click on general
        general_img_location = py.locateCenterOnScreen(image=parent_img_path + "general.png", confidence=0.90, minSearchTime=5)
        py.click(general_img_location)

    if ticket_type_img_path:
        # click on whatever type of ticket you want to book
        ticket_type_location = py.locateCenterOnScreen(image=ticket_type_img_path, confidence=0.90, minSearchTime=5)
        py.click(ticket_type_location)


def input_account_username(username: str, username_image_path: str):
    username_fld_location = py.locateCenterOnScreen(image=username_image_path, confidence=0.90, minSearchTime=5)
    py.click(username_fld_location)
    py.hotkey("ctrl", "a")
    py.press('backspace')
    py.write(username)


def input_account_password(password: str, password_image_path: str):
    password_fld = py.locateCenterOnScreen(image=password_image_path, confidence=0.90, minSearchTime=5)
    py.click(password_fld)
    py.hotkey("ctrl", "a")
    py.press('backspace')
    py.write(password)


def input_irctc_account(username: str, password: str):
    try:
        # Try locating the images on the screen
        sign_in_btn = py.locateCenterOnScreen(image=parent_img_path + "large_sign_in_btn.png", confidence=0.90,
                                              minSearchTime=4)
    except py.ImageNotFoundException:
        sign_in_btn = None

    try:
        sign_in_btn1 = py.locateCenterOnScreen(image=parent_img_path + "small_sign_in_btn.png", confidence=0.90,
                                               minSearchTime=4)
    except py.ImageNotFoundException:
        sign_in_btn1 = None

    # Check if either image is found
    if sign_in_btn or sign_in_btn1:
        input_account_username(username=username, username_image_path=parent_img_path + "username_fld.png")
        input_account_password(password=password, password_image_path=parent_img_path + "password_fld.png")


def input_source_n_destination_station(source_station: str, destination: str):
    from_location = py.locateCenterOnScreen(image=parent_img_path + "source_station.png", confidence=0.90,
                                            minSearchTime=25)
    py.click(from_location)
    py.write(source_station)
    blue_location = py.locateCenterOnScreen(image=parent_img_path + "blue_color_in_dropdwn.png", confidence=0.90,
                                            minSearchTime=25)
    py.click(blue_location)

    destination_location = py.locateCenterOnScreen(image=parent_img_path + "destination_img.png",
                                                   confidence=0.90,
                                                   minSearchTime=25)
    py.click(destination_location)
    py.write(destination)
    blue_location = py.locateCenterOnScreen(image=parent_img_path + "blue_color_in_dropdwn.png", confidence=0.90,
                                            minSearchTime=25)
    py.click(blue_location)


def open_chrome_browser_with_irctc_page():
    click_browsers()
    py.hotkey("ctrl", "t")
    open_url()
    # verifying that after opening the url login btn is present, if login btn present url loaded successfully otherwise
    # not
    login_btn_location = py.locateCenterOnScreen(image=parent_img_path + "login_btn.png", confidence=0.80,
                                                 minSearchTime=25)
    py.click(login_btn_location)


def scroll_to_view(no_of_scroll: float):
    py.scroll(no_of_scroll)


def click_pay_n_book(img_path: str):
    pay_n_book_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    py.click(pay_n_book_location)


def click_confirm_btn_inside_otp(otp_fill_delay: int, img_path: str):
    py.sleep(otp_fill_delay)
    btn_location = py.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=10)
    py.click(btn_location)


def close_login_popup():
    py.click(1494, 229)


def scroll_until_element_visible_not_visible(img_path: str):
    i = -1
    while True:
        i -= 1
        scroll_to_view(no_of_scroll=i)
        try:
            if py.locateCenterOnScreen(image=img_path, confidence=0.80) is not None:
                return True
        except py.ImageNotFoundException:
            # Image not found, continue loop
            pass


def select_train_for_booking(train_name_img_path: str, coach_type_img_path: str):
    # TODO: bug in this func, except of this all funcnatlies of automation is working fine
    scroll_until_element_visible_not_visible(img_path=train_name_img_path)

    # pass img path of train name with time and sleeper visible
    # coach_type_location = py.locateCenterOnScreen(image=coach_type_img_path, confidence=0.90, minSearchTime=10)
    # py.click(coach_type_location)
    # wl_or_available_location = py.locateCenterOnScreen(image=wl_or_available_img_path, confidence=0.90,
    #                                                     minSearchTime=10)
    # py.click(wl_or_available_location)
    # img_path: str = parent_img_path + "book_now.png"
    # click_book_now(img_path=img_path)

    py.sleep(0.5)
    sleeper_location = list(py.locateAllOnScreen(image=parent_img_path + "sleeper_btn.png", grayscale=False, confidence=0.90))
    py.click(sleeper_location[0])











