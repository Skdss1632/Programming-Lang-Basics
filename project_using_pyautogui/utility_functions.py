import pyautogui as py
import json
import pytesseract
from PIL import Image
import schedule
import time
import datetime
parent_img_path = "/home/intern/Documents/gitlearning/Programming_Lang_Basics/project_using_pyautogui/irctc_images/"
# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)


def click_browser():
    browser_location = py.locateCenterOnScreen(image=parent_img_path + "chrome.png", confidence=0.80, minSearchTime=5)
    py.click(browser_location)


def open_url():
    py.write("https://www.irctc.co.in/nget/train-search", interval=0.1)
    py.press("enter")


def click_available_btn(img_path: str):
    py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    py.click(x=651, y=603)


def click_book_now_inside_select_train(book_now_img_path: str):
    book_now_location = py.locateCenterOnScreen(image=book_now_img_path, confidence=0.90, minSearchTime=10)
    py.click(book_now_location)


def click_on_wl_or_avalible_btn(wl_or_available_img_path: str):
    wl_or_available_location = py.locateCenterOnScreen(image=wl_or_available_img_path, confidence=0.90,
                                                       minSearchTime=10)
    py.click(wl_or_available_location)


def select_passenger_from_master_lst(passenger_name: list, passenger_details_img_path: str, blue_tick: str):
    py.locateCenterOnScreen(image=passenger_details_img_path, confidence=0.90, minSearchTime=15)
    try:
        py.locateCenterOnScreen(image=parent_img_path + "india.png", confidence=0.90, minSearchTime=10)

    except py.ImageNotFoundException:
        cross_location = py.locateCenterOnScreen(image=parent_img_path + "cross.png", confidence=0.90, minSearchTime=5)
        py.click(cross_location)
        add_passenger_location = py.locateCenterOnScreen(image=parent_img_path + "add_passenger.png", confidence=0.90,
                                                         minSearchTime=5)
        py.click(add_passenger_location)

    for name in passenger_name:
        passenger_name_input_fld_location = py.locateOnScreen(image=parent_img_path + "passenger_name_input_fld.png",
                                                              confidence=0.90, minSearchTime=5)

        py.click(passenger_name_input_fld_location)
        py.write(name)
        py.sleep(0.5)
        py.press("down")
        py.sleep(0.1)
        py.press("enter")

        # blue_tick_location = py.locateOnScreen(image=blue_tick, confidence=0.75, minSearchTime=10)
        # py.click(blue_tick_location)

        if name != passenger_name[-1]:
            add_passenger_location = py.locateOnScreen(image=parent_img_path + "add_passenger.png", confidence=0.80,
                                                       minSearchTime=10)
            py.click(add_passenger_location)


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
    sign_in_btn = py.locateCenterOnScreen(image=parent_img_path + "search_btn.png", confidence=0.90,
                                          minSearchTime=10)
    py.click(sign_in_btn)


def input_booking_date(tatkal_book_date: str):
    py.click(x=764, y=426)
    clear_input_fld()
    py.write(tatkal_book_date)
    py.press("enter")


def clear_input_fld():
    py.hotkey("ctrl", "a")
    py.press('backspace')


def select_ticket_type_from_dropdown(img_path, ticket_type_for_book: str):
    if ticket_type_for_book == "general":
        pass  # Do nothing for "general"

    if ticket_type_for_book in ["tatkal", "premium_tatkal"]:
        # Click on general to reset or ensure the dropdown is in a known state
        general_img_location = py.locateCenterOnScreen(image=parent_img_path + "general.png", confidence=0.90,
                                                       minSearchTime=15)
        py.click(general_img_location)
        if ticket_type_for_book == "premium_tatkal":
            general_blue_location = py.locateCenterOnScreen(image=parent_img_path + "general_blue.png", confidence=0.90,
                                                           minSearchTime=15)
            py.moveTo(general_blue_location)
            py.scroll(-1)

        ticket_type_location = py.locateCenterOnScreen(image=img_path, confidence=0.90,
                                                       minSearchTime=15)
        py.click(ticket_type_location)


def input_irctc_account(username: str, password: str, username_image_path: str, password_image_path):
    password_filled_img_path = get_image_path(config["image_paths"]["password_filled_image"])
    try:
        py.locateCenterOnScreen(image=password_filled_img_path, confidence=0.90, minSearchTime=5)
        # If password filled image is found, skip the rest of the code
    except py.ImageNotFoundException:
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
            for image, text in [(username_image_path, username), (password_image_path, password)]:
                field_location = py.locateCenterOnScreen(image=image, confidence=0.85, minSearchTime=25)
                py.click(field_location)
                py.hotkey("ctrl", "a")
                py.press('backspace')
                py.write(text)

    enter_captcha_fld_img = get_image_path(config["image_paths"]["enter_captcha_fld_image"])
    enter_captcha_fld_img_location = py.locateCenterOnScreen(image=enter_captcha_fld_img, confidence=0.90,
                                                                 minSearchTime=25)
    py.click(enter_captcha_fld_img_location)


def input_source_n_destination_station(source_station: str, destination: str):
    from_location = py.locateCenterOnScreen(image=parent_img_path + "source_station.png", confidence=0.90,
                                            minSearchTime=25)
    py.click(from_location)
    py.write(source_station)
    blue_location = py.locateCenterOnScreen(image=parent_img_path + "blue_color_in_dropdwn.png", confidence=0.90,
                                            minSearchTime=25)
    py.moveTo(blue_location)
    py.click(blue_location)

    destination_location = py.locateCenterOnScreen(image=parent_img_path + "destination_img.png",
                                                   confidence=0.90,
                                                   minSearchTime=25)
    py.click(destination_location)
    py.write(destination)
    py.sleep(0.5)
    blue_location = py.locateCenterOnScreen(image=parent_img_path + "blue_color_in_dropdwn.png", confidence=0.90,
                                            minSearchTime=25)
    py.moveTo(blue_location)
    py.sleep(0.5)
    py.click(blue_location)


def open_chrome_browser_with_irctc_page():
    click_browser()
    py.hotkey("ctrl", "t")
    open_url()


def click_login_btn():
    # verifying that after opening the url login btn is present, if login btn present url loaded successfully otherwise
    # not
    login_btn_location = py.locateCenterOnScreen(image=parent_img_path + "login_btn.png", confidence=0.90,
                                                 minSearchTime=25)
    py.click(login_btn_location)


def scroll_to_view(no_of_scroll: float):
    py.scroll(no_of_scroll)


def click_pay_n_book(img_path: str):
    pay_n_book_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=10)
    py.click(pay_n_book_location)


def click_confirm_btn_inside_otp(img_path: str, otp_fld_img_path: str):
    otp_fld_location = py.locateCenterOnScreen(image=otp_fld_img_path, confidence=0.80, minSearchTime=10)
    py.click(otp_fld_location)
    # btn_location = py.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=10)
    # py.click(btn_location)


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


def click_on_coach_on_selected_train(coach_type_img_path: str):
    """click on sleeper or third ac or any other coach if you pass img path to this func"""
    sleeper_location = list(py.locateAllOnScreen(image=coach_type_img_path, grayscale=False, confidence=0.90))
    py.click(sleeper_location[1])
    print("total no of sleeper btn visible on ui", len(sleeper_location))


# Function to get the full image path
def get_image_path(image_name):
    return parent_img_path + image_name


def click_enter_captcha_fld():
    enter_captcha_fld_img = get_image_path(config["image_paths"]["enter_captcha_fld_image"])
    enter_captcha_fld_img_location = py.locateCenterOnScreen(image=enter_captcha_fld_img, confidence=0.90, minSearchTime=25)
    py.moveTo(enter_captcha_fld_img_location)
    py.click(enter_captcha_fld_img_location)











