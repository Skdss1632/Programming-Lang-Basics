import schedule
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


def input_details():
    open_chrome_browser_with_irctc_page()
    click_login_btn()
    input_irctc_account(username="skdss16321", password="Sourav99#", username_image_path=parent_img_path + "username_fld.png", password_image_path=parent_img_path + "password_fld.png")
    input_source_n_destination_station(source_station="ndls", destination="spj")

    tatkal_or_premium_tatkal_to_book_img_path = parent_img_path + "tatkal.png"
    select_ticket_type_from_dropdown(ticket_type_img_path=tatkal_or_premium_tatkal_to_book_img_path, ticket_type_for_book="general")
    input_booking_date(tatkal_book_date="10/06/2024")

input_details()


def schedule_task_at_specific_time():
    """This function is designed to function correctly only on the Chrome browser with the page zoom level set to 100%.
    If the browser or page size is changed,
    the program may not operate properly and also do not change the browser position on home page."""

    # click_browser()
    # click_search_btn()
    modify_search_img_path = parent_img_path + "reset_filter_txt.png"
    py.locateCenterOnScreen(image=modify_search_img_path, confidence=0.90, minSearchTime=10)

    # Define paths to images used in automation
    train_name_img_path = parent_img_path + "swantatra_s_exp_with_btn.png"
    coach_type_img_path = parent_img_path + "swantatra_exp_sleeper_with_tym.png"

    # function to select train for booking
    select_train_for_booking(train_name_img_path=train_name_img_path, coach_type_img_path=coach_type_img_path)


    wl_or_available_img_path = parent_img_path + "wl_or_available_img_path.png"
    click_on_wl_or_avalible_btn(wl_or_available_img_path)


    book_now_img_path: str = parent_img_path + "book_now.png"
    click_book_now(book_now_img_path=book_now_img_path)
    passenger_detail_img_path = parent_img_path + "passenger_details.png"
    passenger_name_img_from_dropdwn = ["passenger_1_img.png", "passenger_2_img.png", "passenger_3_img.png"]
    passenger_name = ["sourav kumar"]
    blue_tick = parent_img_path + "blue_tick.png"
    select_passenger_from_master_lst(passenger_name=passenger_name, passenger_details_img_path=passenger_detail_img_path, blue_tick=blue_tick)


    # txt_img = parent_img_path + "txt_img.png"
    # click_book_only_if_confirm_berth_alloted(img_path=txt_img)
    continue_btn_img_path = parent_img_path + "continue_btn.png"
    click_continue_btn_inside_passenger_details(continue_btn_img_path=continue_btn_img_path)

    # View cancellation policy and continue journey review
    view_cancellation_img_path = parent_img_path + "review_journey_yellow_img.png"
    py.locateCenterOnScreen(image=view_cancellation_img_path, confidence=0.90, minSearchTime=15)


    # continue_btn_img_path = parent_img_path + "continue_btn.png"
    # click_continue_btn_inside_review_journey(captcha_fill_delay=10, img_path=continue_btn_img_path)

    payment_yellow_img_path = parent_img_path + "payment_yellow_img.png"
    py.locateCenterOnScreen(image=payment_yellow_img_path, confidence=0.90, minSearchTime=15)

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




































