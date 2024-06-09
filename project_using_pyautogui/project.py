import schedule
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


def input_details():
    open_chrome_browser_with_irctc_page()
    input_irctc_account(username="skdss16321", password="Sourav99#")
    input_source_n_destination_station(source_station="ndls", destination="spj")

    tatkal_or_premium_tatkal_to_book_img_path = parent_img_path + "tatkal.png"
    select_ticket_type_from_dropdown(ticket_type_img_path=tatkal_or_premium_tatkal_to_book_img_path, ticket_type_for_book="general")
    input_booking_date(tatkal_book_date="09/06/2024")

input_details()


def schedule_task_at_specific_time():
    """This function is designed to function correctly only on the Chrome browser with the page zoom level set to 100%.
    If the browser or page size is changed,
    the program may not operate properly and also do not change the browser position on home page."""

    # click_browsers()
    # click_search_btn()
    modify_search_img_path = parent_img_path + "reset_filter_txt.png"
    py.locateCenterOnScreen(image=modify_search_img_path, confidence=0.80, minSearchTime=10)

    # Define paths to images used in automation
    train_name_img_path = parent_img_path + "swantatra_s_exp_with_btn.png"
    coach_type_img_path = parent_img_path + "swantatra_exp_sleeper_with_tym.png"
    wl_or_available_img_path = parent_img_path + "wl_or_available_img_path.png"


    # function to select train for booking
    select_train_for_booking(train_name_img_path=train_name_img_path, coach_type_img_path=coach_type_img_path,
                             wl_or_available_img_path=wl_or_available_img_path)

    # Select passenger name by index and navigate
    passenger_detail_img_path = parent_img_path + "passenger_detail.png"
    py.locateCenterOnScreen(image=passenger_detail_img_path, confidence=0.90, minSearchTime=15)
    #
    py.scroll(-1)
    input_passenger_name(passenger_name="SO")

    txt_img = parent_img_path + "txt_img.png"
    # click_book_only_if_confirm_berth_alloted(img_path=txt_img)
    continue_btn_img_path = parent_img_path + "continue_btn.png"
    click_continue_btn_inside_passenger_details(continue_btn_img_path=continue_btn_img_path)

    # View cancellation policy and continue journey review
    view_cancellation_img_path = parent_img_path + "view_cancellation_policy.png"
    py.locateCenterOnScreen(image=view_cancellation_img_path, confidence=0.90, minSearchTime=15)

    continue_btn_img_path = parent_img_path + "continue_btn.png"
    click_continue_btn_inside_review_journey(captcha_fill_delay=10, img_path=continue_btn_img_path)

    # Payment options and booking
    irctc_e_wallet_img_path = parent_img_path + "irctc_ewallet.png"
    click_irctc_e_wallet(img_path=irctc_e_wallet_img_path)
    # pay_n_book_img_path = parent_img_path + "pay_n_book.png"
    # click_pay_n_book(img_path=pay_n_book_img_path)
    # confirm_btn_img_path = parent_img_path + "confirm_btn.png"
    # click_confirm_btn_inside_otp(otp_fill_delay=10, img_path=confirm_btn_img_path)




schedule_task_at_specific_time()


# # Schedule the task to run at 07:25 AM every day
# schedule.every().day.at("07:29").do(schedule_task_at_specific_time)
#
# while True:
#     schedule.run_pending()
#     schedule_task_at_specific_time()  # Move the function call inside the loop




































