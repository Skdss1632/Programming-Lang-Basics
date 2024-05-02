import schedule
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


parent_img_path: str = "/home/intern/Pictures/Screenshots/"


def input_details():
    # open_chrome_browser_with_irctc_page()
    click_browsers()
    ticket_type_img_path = parent_img_path + "tatkal.png"
    input_journey_details(from_="NEW DELHI", to="SAMASTIPUR", booking_date="29/04/2024",
                          ticket_type_img_path=ticket_type_img_path)
    # click_search_btn()

# input_details()


def schedule_task_at_specific_time():
    """This function is designed to function correctly only on the Chrome browser with the page zoom set to 100%.
    If the browser or page size is changed,
    the program may not operate properly and also do not change the browser position on home page."""



    click_browsers()
    click_search_btn()
    modify_search_img_path = parent_img_path + "modify_search.png"
    pyautogui.locateCenterOnScreen(image=modify_search_img_path, confidence=0.80, minSearchTime=60)

    # Define paths to images used in automation
    pyautogui.sleep(2)
    train_name_img_path = parent_img_path + "swantatra_s_exp_with_btn.png"
    coach_type_img_path = parent_img_path + "swantatra_exp_sleeper_with_tym.png"
    wl_or_available_img_path = parent_img_path + "available_ticket.png"


    # function to select train for booking
    select_train_for_booking(train_name_img_path=train_name_img_path, coach_type_img_path=coach_type_img_path,
                             wl_or_available_img_path=wl_or_available_img_path)

    # Select passenger name by index and navigate
    passenger_detail_img_path = parent_img_path + "passenger_detail.png"
    pyautogui.locateCenterOnScreen(image=passenger_detail_img_path, confidence=0.90, minSearchTime=60)
    input_passenger_name(passenger_name="SOURAV KUMAR")


    txt_img = parent_img_path + "txt_img.png"
    click_book_only_if_confirm_berth_alloted(img_path=txt_img)
    continue_btn_img_path = parent_img_path + "continue_btn.png"
    click_continue_btn_inside_passenger_details(continue_btn_img_path=continue_btn_img_path)

    # View cancellation policy and continue journey review
    view_cancellation_img_path = parent_img_path + "view_cancellation_policy.png"
    pyautogui.locateCenterOnScreen(image=view_cancellation_img_path, confidence=0.90, minSearchTime=60)


    continue_btn_img_path = parent_img_path + "continue_btn.png"
    click_continue_btn_inside_review_journey(captcha_fill_delay=10, img_path=continue_btn_img_path)

    # Payment options and booking
    irctc_e_wallet_img_path = parent_img_path + "irctc_ewallet.png"
    click_irctc_e_wallet(img_path=irctc_e_wallet_img_path)
    pay_n_book_img_path = parent_img_path + "pay_n_book.png"
    click_pay_n_book(img_path=pay_n_book_img_path)
    confirm_btn_img_path = parent_img_path + "confirm_btn.png"
    # click_confirm_btn_inside_otp(otp_fill_delay=10, img_path=confirm_btn_img_path)


# Schedule the task to run at 07:25 AM every day
schedule.every().day.at("07:29").do(schedule_task_at_specific_time)

while True:
    schedule.run_pending()
    schedule_task_at_specific_time()  # Move the function call inside the loop




































