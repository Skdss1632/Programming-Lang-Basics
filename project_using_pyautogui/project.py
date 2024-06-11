import schedule
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *  # Custom utility functions


def input_details():
    """Automates the process of inputting details on the IRCTC page."""
    open_chrome_browser_with_irctc_page()
    click_login_btn()

    username = config["credentials"]["username"]
    password = config["credentials"]["password"]
    username_image_path = get_image_path(config["image_paths"]["username_field_image"])
    password_image_path = get_image_path(config["image_paths"]["password_field_image"])
    input_irctc_account(username=username, password=password, username_image_path=username_image_path,
                        password_image_path=password_image_path)

    source_station = config["booking_details"]["source_station"]
    destination = config["booking_details"]["destination_station"]
    input_source_n_destination_station(source_station=source_station, destination=destination)

    ticket_type = config["image_paths"]["tatkal_image"]
    select_ticket_type_from_dropdown(img_path=ticket_type, ticket_type_for_book="general")

    tatkal_book_date = config["booking_details"]["booking_date"]
    input_booking_date(tatkal_book_date=tatkal_book_date)

    reset_filter_txt_img_path = get_image_path(config["image_paths"]["reset_filter_image"])
    py.locateCenterOnScreen(image=reset_filter_txt_img_path, confidence=0.90, minSearchTime=25)

    train_name_img_path = get_image_path(config["image_paths"]["train_name_image"])
    scroll_until_element_visible_not_visible(img_path=train_name_img_path)
    py.sleep(0.2)


def schedule_task_at_specific_time():
    coach_type_img_path = get_image_path(config["image_paths"]["sleeper_btn_image"])
    click_on_coach_on_selected_train(coach_type_img_path=coach_type_img_path)

    wl_or_available_img_path = get_image_path(config["image_paths"]["waiting_list_image"])
    click_on_wl_or_avalible_btn(wl_or_available_img_path)

    dark_color_book_now_img_path = get_image_path(config["image_paths"]["book_now_image"])
    click_book_now_inside_select_train(book_now_img_path=dark_color_book_now_img_path)

    passenger_detail_img_path = get_image_path(config["image_paths"]["passenger_details_image"])
    passenger_names = config["booking_details"]["passenger_names"]
    blue_tick = get_image_path(config["image_paths"]["blue_tick_image"])
    select_passenger_from_master_lst(passenger_name=passenger_names,
                                     passenger_details_img_path=passenger_detail_img_path,
                                     blue_tick=blue_tick)

    continue_btn_img_path = get_image_path(config["image_paths"]["continue_button_image"])
    click_continue_btn_inside_passenger_details(continue_btn_img_path=continue_btn_img_path)

    view_cancellation_img_path = get_image_path(config["image_paths"]["review_journey_image"])
    py.locateCenterOnScreen(image=view_cancellation_img_path, confidence=0.90, minSearchTime=25)
    py.scroll(-2.5)
    py.sleep(0.1)
    click_enter_captcha_fld()

    payment_yellow_img_path = get_image_path(config["image_paths"]["payment_yellow_image"])
    py.locateCenterOnScreen(image=payment_yellow_img_path, confidence=0.90, minSearchTime=25)

    irctc_e_wallet_img_path = get_image_path(config["image_paths"]["irctc_ewallet_image"])
    click_irctc_e_wallet(img_path=irctc_e_wallet_img_path)

    pay_n_book_img_path = get_image_path(config["image_paths"]["pay_n_book_img_image"])
    click_pay_n_book(img_path=pay_n_book_img_path)

    confirm_btn_img_path = get_image_path(config["image_paths"]["confirm_btn_image"])
    otp_fld_img_path = get_image_path(config["image_paths"]["otp_image"])
    click_confirm_btn_inside_otp(img_path=confirm_btn_img_path, otp_fld_img_path=otp_fld_img_path)


# Execute the input details function
input_details()


# Schedule the task to run at 07:25 AM every day
schedule.every().day.at("10:55").do(schedule_task_at_specific_time)

while True:
    schedule.run_pending()



