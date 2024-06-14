from Programming_Lang_Basics.automation_project.utility_functions import *  # Custom utility functions


def input_details():
    """Automates the process of inputting details on the IRCTC page.
    if you want to book ticket in another train take that train ss and pass the img path train_name_image"""
    open_chrome_browser_with_irctc_page()
    click_login_btn()
    py.sleep(3)
    # # validate login popup open or not
    # otp_fld_location = py.locateCenterOnScreen(image=, confidence=0.80, minSearchTime=10)

    username_field_image = get_image_path("username_field_image")
    password_field_image = get_image_path("password_field_image")
    username = get_credentials("username")
    password = get_credentials("password")
    input_irctc_account(username=username, password=password, username_image_path=username_field_image,
                        password_image_path=password_field_image)

    source_station = get_booking_details("source_station")
    destination_station = get_booking_details("destination_station")
    input_source_n_destination_station(source_station=source_station, destination=destination_station)

    select_ticket_type_from_dropdown()

    tatkal_book_date = get_booking_details("travel_date")
    input_travel_date(tatkal_book_date=tatkal_book_date)

    reset_filter_txt_img_path = get_image_path("reset_filter_image")
    py.locateCenterOnScreen(image=reset_filter_txt_img_path, confidence=0.90, minSearchTime=60)
    py.sleep(1)

    train_name_img_path = get_image_path("train_name_image")
    scroll_until_element_visible_not_visible(img_path=train_name_img_path)
    py.sleep(0.2)
    # py.sleep(8)


def schedule_task_at_specific_time():
    py.sleep(2)
    click_on_coach_on_selected_train()

    click_on_wl_or_avalible_btn()

    book_now_img_path = get_image_path("book_now_image")
    scroll_until_element_visible_not_visible(book_now_img_path, train_name_img_path="")
    click_book_now_inside_select_train(book_now_img_path=book_now_img_path)

    # passenger_detail_img_path = get_image_path("passenger_details_image")
    # passenger_names = get_booking_details("passenger_names")
    # select_passenger_from_master_lst(passenger_names=passenger_names,
    #                                  passenger_details_img_path=passenger_detail_img_path)

    input_passenger_names()

    if get_booking_details("is_tatkal") or get_booking_details("is_premium_tatkal"):
        click_book_only_if_confirm_berth_alloted(get_image_path("book_only_if_get_confirm_berth"))

    continue_btn_img_path = get_image_path("continue_button_image")
    scroll_until_element_visible_not_visible(img_path=continue_btn_img_path, train_name_img_path="")
    if get_booking_details("is_payment_with_upi"):
        click_pay_with_upi()

    # click continue btn inside passenger details
    click_continue_btn_inside_passenger_details(continue_btn_img_path=continue_btn_img_path)

    py.sleep(1)
    scroll_until_element_visible_not_visible(img_path=get_image_path("connected_us_on_social_media_image"), train_name_img_path="")
    click_captcha_fld()

    py.locateCenterOnScreen(image=get_image_path("payment_yellow_image"), confidence=0.90, minSearchTime=60)
    py.sleep(1)

    if get_booking_details("is_payment_with_upi"):
        click_bhim_upi_ssd()
        click_pay_using_bhim_paytm_txt()
    else:
        # if want to pay with wallet verify you have wallet and have required amt in it
        click_irctc_e_wallet(img_path=get_image_path("irctc_e_wallet_image"))
        is_irctc_wallet_clicked()

    pay_n_book_img_path = get_image_path("pay_n_book_image")
    scroll_until_element_visible_not_visible(pay_n_book_img_path, train_name_img_path="")
    click_pay_n_book(img_path=pay_n_book_img_path)

    click_otp_fld(otp_fld_img_path=get_image_path("otp_fld_image"), no_of_clicks=1)
    if get_booking_details("is_read_and_write_otp_from_mail"):
        read_and_write_otp_from_mail()

    click_confirm_btn_inside_otp(confirm_btn_img_path=get_image_path("confirm_btn_image"))


# input_details()
schedule_task_at_specific_time()


# Schedule the task to run at 07:25 AM every day
if get_booking_details("is_ac_3_tier"):
    time = "10:00:00"
else:
    time = "11:00:00"
schedule.every().day.at(time).do(schedule_task_at_specific_time)
while True:
    schedule.run_pending()
