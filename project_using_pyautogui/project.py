import schedule
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


def schedule_task_at_specific_time():
    """This function is designed to function correctly only on the Chrome browser with the page zoom set to 100%.
    If the browser or page size is changed,
    the program may not operate properly and also do not change the browser position on home page."""

    parent_img_path: str = "/home/intern/Pictures/Screenshots/"
    # open_chrome_browser_with_irctc_page()
    # img_path: str = parent_img_path + "login_btn.png"
    # pyautogui.locateCenterOnScreen(img_path, confidence=0.90, minSearchTime=60)
    # username = "skdss16321"
    # password = "Sourav99#"
    # login_irctc_account(username=username, password=password, captcha_fill_delay=10)
    pyautogui.sleep(3)
    # click_browsers()
    # click_search_btn()
    # input_journey_details(from_="NEW DELHI", to="SAMASTIPUR", booking_date="22/04/2024")



    # Define paths to images used in automation
    train_name_img_path = parent_img_path + "vaisahli_exp.png"
    coach_type_img_path = parent_img_path + "vaishali_exp_sleeper_with_tym.png"
    wl_or_available_img_path = parent_img_path + "WL.png"

    # function to select train for booking
    select_train_for_booking(train_name_img_path=train_name_img_path, coach_type_img_path=coach_type_img_path,
                             wl_or_available_img_path=wl_or_available_img_path)

    # # Select passenger name by index and navigate
    passenger_detail_img_path = parent_img_path + "passenger_detail.png"
    click_passenger_name_fld(img_path=passenger_detail_img_path)
    select_passenger_name(input_passenger_name_index=7)


    txt_img = parent_img_path + "txt_img.png"
    # click_book_only_if_confirm_berth_alloted(img_path=txt_img)
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
    # click_pay_n_book(img_path=pay_n_book_img_path)
    # confirm_btn_img_path = parent_img_path + "confirm_btn.png"
    # click_confirm_btn_inside_otp(otp_fill_delay=10, img_path=confirm_btn_img_path)


# # Schedule the task to run at 11:00 AM every day
# schedule.every().day.at("15:56").do(Schedule_task_at_specific_time)

# while True:
#     schedule.run_pending()


schedule_task_at_specific_time()



































