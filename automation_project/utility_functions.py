import pyautogui as py
import json
import pytesseract
from PIL import Image
import pyperclip
import os
import platform
import schedule
import time
import datetime


parent_img_path = "/home/intern/Documents/gitlearning//Programming_Lang_Basics/automation_project/irctc_images/"
with open('json_config/automation_img_filenames.json', 'r') as f:
    img_config = json.load(f)

with open('json_config/booking_config.json', 'r') as f:
    booking_config = json.load(f)

with open('json_config/login_credentials.json', 'r') as f:
    login_credentials = json.load(f)

with open('json_config/passenger_data.json', 'r') as f:
    passenger_data = json.load(f)


def get_coach_booking_preferences(key: str):
    return booking_config["coach_booking_preferences"].get(key)


def get_ticket_type_selection(key: str):
    return booking_config["ticket_type_selection"].get(key)


def get_ticket_availability_status(key: str):
    return booking_config["ticket_availability_status"].get(key)


def get_otp_and_payment_options(key: str):
    return booking_config["otp_and_payment_options"].get(key)


def get_passenger_details():
    return passenger_data["passenger_details"]


def get_booking_details(key: str):
    return booking_config["booking_details"].get(key)


def get_image_path(image_name: str):
    return parent_img_path + img_config["image_file_name"][image_name]


def get_login_credentials(credentials_key: str):
    return login_credentials["credentials"][credentials_key]


def click_browser():
    system = platform.system()
    if system == "Windows":
        os.system("start chrome")
    elif system == "Linux":
        os.system("google-chrome &")
    else:
        raise NotImplementedError("Unsupported operating system")


def open_url():
    py.write("https://www.irctc.co.in/nget/train-search", interval=0.1)
    py.press("enter")


def click_book_now_inside_select_train(book_now_img_path: str):
    book_now_location = py.locateCenterOnScreen(image=book_now_img_path, confidence=0.90, minSearchTime=60)
    py.moveTo(book_now_location)
    py.click(book_now_location)


def click_on_wl_or_avalible_btn():
    wl_or_available_img_path = ""
    if get_ticket_availability_status("is_ticket_waiting"):
        wl_or_available_img_path = get_image_path("waiting_list_image")
    elif get_ticket_availability_status("is_ticket_available"):
        wl_or_available_img_path = get_image_path("available_ticket_image")
    wl_or_available_location = py.locateCenterOnScreen(image=wl_or_available_img_path, confidence=0.90,
                                                       minSearchTime=60)
    py.click(wl_or_available_location)


def input_passenger_names(no_of_passenger_for_booking: int):
    #     catering_loc = ""
    #     try:
    #         # select no food if catering option avl
    #         py.locateCenterOnScreen(image=get_image_path("catering_option_image"), confidence=0.90)
    #         py.press("tab", presses=5)
    #         py.press("right", presses=3)
    #
    #     except py.ImageNotFoundException:
    #         print("No catering option")

    py.locateCenterOnScreen(image=get_image_path("passenger_name_input_fld_image"),
                            confidence=0.90, minSearchTime=120)
    passenger_details = get_passenger_details()
    i = 0
    for passenger in passenger_details:
        passenger_name = passenger.get("NAME")
        py.write(passenger_name)
        py.press("tab")
        py.write(str(passenger.get("AGE")))
        py.press("tab")
        if passenger.get("GENDER") == "Female":
            py.press('right', presses=2)
        else:
            py.press('right')

        if passenger_name != "sourav":
            py.press("tab", presses=3)
            py.press("enter")
            # there is delay in appearing passenger detail input fld after clicking on add pass detail so verify the img first then perform action
            py.locateCenterOnScreen(image=get_image_path("passenger_name_input_fld_image"),
                                    confidence=0.90, minSearchTime=120)


no_of_press = 0


def click_book_only_if_confirm_berth_alloted():
    global no_of_press
    if get_passenger_phn_no() != "":
        no_of_press = 4
    elif get_passenger_phn_no() == "":
        no_of_press = 10
    py.press("tab", presses=no_of_press)
    py.press("space")


def click_continue_btn_inside_review_journey(captcha_fill_delay: int, img_path: str):
    scroll_until_element_visible_not_visible(img_path=img_path, no_of_scrolls=3)
    py.sleep(captcha_fill_delay)
    button_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=240)
    py.click(button_location)


def click_irctc_e_wallet(img_path: str):
    wallet_location = py.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=240)
    py.moveTo(wallet_location)
    py.click(wallet_location)


def click_search_btn():
    sign_in_btn = py.locateCenterOnScreen(image=get_image_path("search_btn_image"), confidence=0.90,
                                          minSearchTime=240)
    py.click(sign_in_btn)


def clear_input_fld():
    py.hotkey("ctrl", "a")
    py.press('backspace')


def select_ticket_type_from_dropdown():
    ticket_type_location = ""
    if get_coach_booking_preferences("is_general"):
        pass  # Do nothing for "general"

    if get_ticket_type_selection("is_tatkal") or get_ticket_type_selection("is_premium_tatkal"):
        # Click on general to reset or ensure the dropdown is in a known state
        general_img_location = py.locateCenterOnScreen(image=get_image_path("general_image"), confidence=0.90,
                                                       minSearchTime=15)
        py.click(general_img_location)
        if get_ticket_type_selection("is_premium_tatkal"):
            general_blue_location = py.locateCenterOnScreen(image=get_image_path("general_blue_image"), confidence=0.90,
                                                            minSearchTime=15)
            py.moveTo(general_blue_location)
            py.scroll(-0.3)

            ticket_type_location = py.locateCenterOnScreen(image=get_image_path("premium_tatkal_image"),
                                                           confidence=0.90,
                                                           minSearchTime=15)
        if get_ticket_type_selection("is_tatkal"):
            ticket_type_location = py.locateCenterOnScreen(image=get_image_path("tatkal_image"), confidence=0.90,
                                                           minSearchTime=15)
        py.click(ticket_type_location)


# def input_irctc_account(username: str, password: str, username_image_path: str, password_image_path):
#     password_filled_img_path = get_image_path("password_filled_image")
#     try:
#         py.locateCenterOnScreen(image=password_filled_img_path, confidence=0.75, minSearchTime=5)
#         # If password filled image is found, skip the rest of the code
#     except py.ImageNotFoundException:
#         try:
#             # Try locating the images on the screen
#             large_sign_in_btn = py.locateCenterOnScreen(image=get_image_path("large_sign_in_btn"), confidence=0.90,
#                                                         minSearchTime=5)
#         except py.ImageNotFoundException:
#             large_sign_in_btn = None
#
#         try:
#             small_sign_in_btn = py.locateCenterOnScreen(image=get_image_path("small_sign_in_btn"), confidence=0.90,
#                                                         minSearchTime=5)
#         except py.ImageNotFoundException:
#             small_sign_in_btn = None
#
#         # Check if either image is found
#         if small_sign_in_btn or large_sign_in_btn:
#             for image, text in [(username_image_path, username), (password_image_path, password)]:
#                 field_location = py.locateCenterOnScreen(image=image, confidence=0.85, minSearchTime=25)
#                 py.click(field_location)
#                 # py.hotkey("ctrl", "a")
#                 # py.press('backspace')
#                 py.write(text)
#         # go inside captcha fld
#         py.press("tab", presses=2)


# def input_irctc_account(username: str, password: str):
#     password_filled_img_path = get_image_path("password_filled_image")
#     try:
#         py.locateCenterOnScreen(image=password_filled_img_path, confidence=0.75, minSearchTime=5)
#         # If password filled image is found, skip the rest of the code
#     except py.ImageNotFoundException:
#         try:
#             # Try locating the images on the screen
#             large_sign_in_btn = py.locateCenterOnScreen(image=get_image_path("large_sign_in_btn"), confidence=0.90,
#                                                         minSearchTime=5)
#         except py.ImageNotFoundException:
#             large_sign_in_btn = None
#
#         try:
#             small_sign_in_btn = py.locateCenterOnScreen(image=get_image_path("small_sign_in_btn"), confidence=0.90,
#                                                         minSearchTime=5)
#         except py.ImageNotFoundException:
#             small_sign_in_btn = None
#
#         # Check if either image is found
#         if small_sign_in_btn or large_sign_in_btn:
#             py.sleep(1)
#             py.hotkey("ctrl", "a")
#             py.press('backspace')
#             py.write(username)
#             py.press('tab')
#             py.write(password)
#             # go inside captcha fld
#             py.press("tab", presses=2)


def input_source_n_destination_station(source_station: str, destination: str):
    # go inside source station input fld
    source_loc = py.locateCenterOnScreen(image=get_image_path("source_station_image"), confidence=0.90,
                                         minSearchTime=240)
    py.moveTo(source_loc)
    py.click(source_loc)
    py.write(source_station, interval=0.1)
    py.sleep(1)
    py.locateCenterOnScreen(image=get_image_path("blue_color_in_dropdwn_image"), confidence=0.85,
                            minSearchTime=10)
    py.press("enter")

    # go inside destination input fld
    py.press("tab", presses=2)
    py.write(destination, interval=0.1)
    py.sleep(1)
    py.locateCenterOnScreen(image=get_image_path("blue_color_in_dropdwn_image"), confidence=0.85, minSearchTime=10)
    py.sleep(0.5)
    py.press("enter")

    # enter travel date
    py.press("tab", presses=1)
    py.write(get_booking_details("travel_date"))
    py.press("enter")

    # # go to general dropdwn
    # py.press("tab", presses=2)
    # if get_booking_details("is_tatkal"):
    #     py.press("up", presses=2)
    # if get_ticket_type_selection("is_premium_tatkal"):
    #     py.press("up")


def open_chrome_browser_with_irctc_page():
    click_browser()
    py.hotkey("ctrl", "t")
    open_url()


def click_login_btn():
    # verifying that after opening the url login btn is present, if login btn present url loaded successfully otherwise
    # not and click on it
    login_btn_location = py.locateCenterOnScreen(image=get_image_path("login_btn_image"), confidence=0.90,
                                                 minSearchTime=25)
    py.click(login_btn_location)


def click_pay_n_book(no_of_press: int):
    py.press("tab", presses=no_of_press)
    py.press("enter")


def click_otp_fld(otp_fld_img_path: str):
    # max wait time while tatkal
    py.locateCenterOnScreen(image=otp_fld_img_path, confidence=0.80, minSearchTime=120)
    py.press("tab")


def scroll_until_element_visible_not_visible(img_path: str, no_of_scrolls=-3):
    for _ in range(20):
        py.scroll(no_of_scrolls)
        try:
            if py.locateCenterOnScreen(image=img_path, confidence=0.90) is not None:
                return True
        except py.ImageNotFoundException:
            # Image not found, continue loop
            pass


def click_on_coach_on_selected_train():
    """click on sleeper or third ac or any other coach if you pass img path to this func"""
    coach_type_img_path = ""
    if get_coach_booking_preferences("is_sleeper"):
        coach_type_img_path = get_image_path("sleeper_btn_image")
    elif get_coach_booking_preferences("is_ac_3_tier"):
        coach_type_img_path = get_image_path("ac_3_tier_btn_image")
    elif get_image_path("ac_3_economy_image"):
        coach_type_img_path = get_image_path("ac_3_economy_image")

    btn_location = list(py.locateAllOnScreen(image=coach_type_img_path, grayscale=False, confidence=0.95))
    print(btn_location)
    py.moveTo(btn_location[0])
    py.click(btn_location[0])
    print("total no of sleeper btn visible on ui", len(btn_location))


def click_captcha_fld():
    py.press("tab", presses=7)


def read_and_write_otp_from_mail():
    """this function reads otp from mail
     and writes it to otp box work only if only two tabs are open in browser one is mail and another is booking web"""
    py.hotkey("ctrl", "tab")
    otp_txt_in_mail_image = py.locateCenterOnScreen(image=get_image_path("otp_txt_in_mail_image"), confidence=0.90,
                                                    minSearchTime=120)
    py.click(otp_txt_in_mail_image)
    py.locateCenterOnScreen(image=get_image_path("your_one_tym_otp_txt_image"), confidence=0.90,
                            minSearchTime=25)
    py.moveTo(707, 472)
    py.click(707, 472, clicks=2)
    py.hotkey("ctrl", "c")
    # delete the otp mail after copying it
    delete_location = py.locateCenterOnScreen(image=get_image_path("delete_icon_of_mail_image"), confidence=0.90,
                                              minSearchTime=15)
    py.moveTo(delete_location)
    py.click(delete_location)
    py.hotkey("ctrl", "tab")
    otp = pyperclip.paste()
    py.write(otp)
    # go to confirm btn
    py.press("tab")
    print(otp)


def read_and_fill_otp():
    # Path to Tesseract executable (you may need to change this based on your system)
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

    def solve_captcha(image_path):
        # Open the captcha image
        with Image.open(image_path) as img:
            # Convert the image to grayscale for better OCR accuracy
            img = img.convert('L')

            # Use pytesseract to perform OCR on the image
            captcha_text = pytesseract.image_to_string(img)

            return captcha_text.strip()

    # Example usage:
    captcha_text = solve_captcha('captcha.png')
    print("Captcha Text:", captcha_text)


def click_pay_with_upi():
    global no_of_press
    if get_ticket_type_selection("is_tatkal") or get_ticket_type_selection("is_premium_tatkal"):
        no_of_press = 6
    py.press("tab", presses=no_of_press)
    py.press("down")


def click_bhim_upi_ssd():
    loc = py.locateCenterOnScreen(image=get_image_path("bhim_upi_txt_image"), confidence=0.90,
                                  minSearchTime=25)
    py.moveTo(loc)
    py.click(loc)


def is_irctc_wallet_clicked():
    # verify irctc e wallet btn is clicked
    py.locateCenterOnScreen(image=get_image_path("an_amt_of_10_applicable_txt_image"), confidence=0.90,
                            minSearchTime=240)


def click_pay_using_bhim_paytm_txt():
    py.locateCenterOnScreen(image=get_image_path("pay_using_bhim_paytm_txt_image"),
                            confidence=0.90, minSearchTime=240)
    py.press("tab", presses=2)
    py.press("enter")
    # py.locateCenterOnScreen(image=get_image_path("paytm_upi_txt_correct_sign_image"),
    #                         confidence=0.90, minSearchTime=15)


def click_continue_btn_inside_pass_details():
    global no_of_press
    # if is_payment_with_upi True then cursor is inside pay through bhim upi count the tab press from there
    if get_otp_and_payment_options("is_payment_with_upi"):
        no_of_press = 2
    # if tatkal True then currently cursor is inside this checkbox-- book only if i et confirm berth
    elif get_ticket_type_selection("is_tatkal") or get_ticket_type_selection("is_premium_tatkal"):
        no_of_press = 8
    # if not tatkal and phn no == "" then count the tab press from gender box
    else:
        no_of_press = 18
    py.press("tab", presses=no_of_press)
    py.press("enter")


def get_passenger_phn_no():
    return passenger_data.get("passenger_phn_no")


def input_passenger_phn_no():
    passenger_phn_no = get_passenger_phn_no()
    if passenger_phn_no:
        py.press("tab", presses=6)
        py.write(passenger_phn_no)



