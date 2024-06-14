import pyautogui as py
import json
import pytesseract
from PIL import Image
import schedule
import time
import datetime
import pyperclip

parent_img_path = "/home/intern/Documents/gitlearning//Programming_Lang_Basics/automation_project/irctc_images/"
# Load configuration from JSON file
with open('config.json', 'r') as f:
    config = json.load(f)


def click_browser():
    browser_location = py.locateCenterOnScreen(image=get_image_path("chrome_image"), confidence=0.80, minSearchTime=5)
    py.click(browser_location)


def open_url():
    py.write("https://www.irctc.co.in/nget/train-search", interval=0.1)
    py.press("enter")


def click_book_now_inside_select_train(book_now_img_path: str):
    book_now_location = py.locateCenterOnScreen(image=book_now_img_path, confidence=0.90, minSearchTime=60)
    py.moveTo(book_now_location)
    py.click(book_now_location)


def click_on_wl_or_avalible_btn():
    wl_or_available_img_path = ""
    if get_booking_details("is_ticket_waiting"):
        wl_or_available_img_path = get_image_path("waiting_list_image")
    elif get_booking_details("is_ticket_available"):
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

        if passenger_name != "nishant kr":
            py.press("tab", presses=3)
            py.press("enter")
            # there is delay in appearing passenger detail input fld after clicking on add pass detail so verify the img first then perform action
            py.locateCenterOnScreen(image=get_image_path("passenger_name_input_fld_image"),
                                    confidence=0.90, minSearchTime=120)


def click_book_only_if_confirm_berth_alloted(img_path: str):
    scroll_until_element_visible_not_visible(img_path=img_path, no_of_scrolls=-2)
    txt_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=60)
    py.click(txt_location)


def click_continue_btn_inside_review_journey(captcha_fill_delay: int, img_path: str):
    scroll_until_element_visible_not_visible(img_path=img_path, no_of_scrolls=3)
    py.sleep(captcha_fill_delay)
    button_location = py.locateCenterOnScreen(image=img_path, confidence=0.90, minSearchTime=60)
    py.click(button_location)


def click_irctc_e_wallet(img_path: str):
    wallet_location = py.locateCenterOnScreen(image=img_path, confidence=0.80, minSearchTime=60)
    py.moveTo(wallet_location)
    py.click(wallet_location)


def click_search_btn():
    sign_in_btn = py.locateCenterOnScreen(image=get_image_path("search_btn_image"), confidence=0.90,
                                          minSearchTime=60)
    py.click(sign_in_btn)


def clear_input_fld():
    py.hotkey("ctrl", "a")
    py.press('backspace')


def select_ticket_type_from_dropdown():
    ticket_type_location = ""
    if get_booking_details("is_general"):
        pass  # Do nothing for "general"

    if get_booking_details("is_tatkal") or get_booking_details("is_premium_tatkal"):
        # Click on general to reset or ensure the dropdown is in a known state
        general_img_location = py.locateCenterOnScreen(image=get_image_path("general_image"), confidence=0.90,
                                                       minSearchTime=15)
        py.click(general_img_location)
        if get_booking_details("is_premium_tatkal"):
            general_blue_location = py.locateCenterOnScreen(image=get_image_path("general_blue_image"), confidence=0.90,
                                                            minSearchTime=15)
            py.moveTo(general_blue_location)
            py.scroll(-0.3)

            ticket_type_location = py.locateCenterOnScreen(image=get_image_path("premium_tatkal_image"),
                                                           confidence=0.90,
                                                           minSearchTime=15)
        if get_booking_details("is_tatkal"):
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
                                            minSearchTime=60)
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
    # if get_booking_details("is_premium_tatkal"):
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


def click_confirm_btn_inside_otp(confirm_btn_img_path: str):
    pass
    # btn_location = py.locateCenterOnScreen(image=confirm_btn_img_path, confidence=0.80, minSearchTime=10)
    # py.click(btn_location)


def click_otp_fld(otp_fld_img_path: str):
    # max wait time while tatkal
    py.locateCenterOnScreen(image=otp_fld_img_path, confidence=0.80, minSearchTime=120)
    py.press("tab")


def scroll_until_element_visible_not_visible(img_path: str, no_of_scrolls=-3):
    while True:
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
    if get_booking_details("is_sleeper"):
        coach_type_img_path = get_image_path("sleeper_btn_image")
    elif get_booking_details("is_ac_3_tier"):
        coach_type_img_path = get_image_path("ac_3_tier_btn_image")
    elif get_image_path("ac_3_economy_image"):
        coach_type_img_path = get_image_path("ac_3_economy_image")

    btn_location = list(py.locateAllOnScreen(image=coach_type_img_path, grayscale=False, confidence=0.95))
    print(btn_location)
    py.moveTo(btn_location[0])
    py.click(btn_location[0])
    print("total no of sleeper btn visible on ui", len(btn_location))


def get_image_path(image_name):
    return parent_img_path + config["image_paths"][image_name]


def get_booking_details(booking_key: str):
    return config["booking_details"][booking_key]


def get_credentials(credentials_key: str):
    return config["credentials"][credentials_key]


def click_captcha_fld():
    py.press("tab", presses=7)


def read_and_write_otp_from_mail():
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
    for string in otp:
        py.write(string)
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
    payment_with_upi_loc = py.locateCenterOnScreen(image=get_image_path("pay_with_upi_checkbox_image"), confidence=0.90,
                                                   minSearchTime=25)
    py.moveTo(payment_with_upi_loc)
    py.click(payment_with_upi_loc)


def click_bhim_upi_ssd():
    click_bhim_upi_ssd_loc = py.locateCenterOnScreen(image=get_image_path("bhim_upi_txt_image"), confidence=0.90,
                                                     minSearchTime=25)
    py.moveTo(click_bhim_upi_ssd_loc)
    py.click(click_bhim_upi_ssd_loc)


def is_irctc_wallet_clicked():
    # verify irctc e wallet btn is clicked
    py.locateCenterOnScreen(image=get_image_path("an_amt_of_10_applicable_txt_image"), confidence=0.90,
                            minSearchTime=60)


def click_pay_using_bhim_paytm_txt():
    py.locateCenterOnScreen(image=get_image_path("pay_using_bhim_paytm_txt_image"),
                                                       confidence=0.90, minSearchTime=60)
    py.press("tab", presses=2)
    py.click("enter")
    py.locateCenterOnScreen(image=get_image_path("paytm_upi_txt_correct_sign_image"),
                            confidence=0.90, minSearchTime=15)


def get_passenger_details():
    return config["booking_details"]["passenger_details"]


def click_continue_btn_inside_pass_details():
    if get_booking_details("is_payment_with_upi"):
        no_of_press = 2
    elif get_booking_details("passenger_phn_no") != "":
        no_of_press = 7
    else:
        no_of_press = 9
    py.press("tab", presses=no_of_press)
    py.press("enter")


def input_passenger_phn_no():
    if get_booking_details("passenger_phn_no") != "":
        py.press("tab", presses=6)
        py.write(get_booking_details("passenger_phn_no"))