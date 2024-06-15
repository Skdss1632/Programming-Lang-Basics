from Programming_Lang_Basics.automation_project.utility_functions import *  # Custom utility functions


def input_details():
    """Automates the process of inputting details on the IRCTC page.
    if you want to book ticket in another train take that train ss and pass the img path train_name_image"""
    open_chrome_browser_with_irctc_page()
    click_login_btn()
    py.sleep(3)
    username = get_login_credentials("username")
    password = get_login_credentials("password")
    # input_irctc_account(username=username, password=password)

    source_station = get_booking_details("source_station")
    destination_station = get_booking_details("destination_station")
    input_source_n_destination_station(source_station=source_station, destination=destination_station)

    # select_ticket_type_from_dropdown()

    reset_filter_txt_img_path = get_image_path("reset_filter_image")
    py.locateCenterOnScreen(image=reset_filter_txt_img_path, confidence=0.90, minSearchTime=60)
    py.sleep(1)

    train_name_img_path = get_image_path("train_name_image")
    scroll_until_element_visible_not_visible(img_path=train_name_img_path, no_of_scrolls=-1)
    py.sleep(0.2)
    # py.sleep(8)


def schedule_task_at_specific_time():
    py.sleep(2)
    # click_on_coach_on_selected_train()

    click_on_wl_or_avalible_btn()
    scroll_until_element_visible_not_visible(img_path=get_image_path("book_now_image"), no_of_scrolls=-1)
    click_book_now_inside_select_train(book_now_img_path=get_image_path("book_now_image"))

    # if want to perform any action inside pass details count the presses from gender
    input_passenger_names(no_of_passenger_for_booking=get_booking_details("no_of_passenger_for_booking"))

    input_passenger_phn_no()

    if get_ticket_type_selection("is_tatkal") or get_ticket_type_selection("is_premium_tatkal"):
        click_book_only_if_confirm_berth_alloted()

    if get_otp_and_payment_options("is_payment_with_upi"):
        scroll_until_element_visible_not_visible(img_path=get_image_path("pay_through_bhim_upi_image"))
        click_pay_with_upi()

    click_continue_btn_inside_pass_details()

    # here page start buffering
    py.locateCenterOnScreen(image=get_image_path("review_journey_image"), confidence=0.90, minSearchTime=240)
    # click captcha fld
    py.sleep(1)
    click_captcha_fld()
    # press enter manually after filling captcha

    py.locateCenterOnScreen(image=get_image_path("payment_yellow_image"), confidence=0.90, minSearchTime=240)
    py.sleep(1)

    if get_otp_and_payment_options("is_payment_with_upi"):
        click_bhim_upi_ssd()
        click_pay_using_bhim_paytm_txt()
        click_pay_n_book(no_of_press=4)
    else:
        # if want to pay with wallet verify you have created wallet in acc and have required amt in it
        click_irctc_e_wallet(img_path=get_image_path("irctc_e_wallet_image"))
        is_irctc_wallet_clicked()
        click_pay_n_book(no_of_press=10)
        # if want to pay with wallet need to click on otp fld otherwise not, there is no need to click on otp fld if want to pay with upi just scan qr and pay
        click_otp_fld(otp_fld_img_path=get_image_path("otp_fld_image"))

    if get_otp_and_payment_options("is_read_and_write_otp_from_mail"):
        read_and_write_otp_from_mail()



schedule_task_at_specific_time()










# Schedule the task to run at 11:00:00 AM for sleeper and 10:00:00 AM  every day
if get_coach_booking_preferences("is_ac_3_tier") or get_coach_booking_preferences("is_ac_tier_3_economy"):
    time = "10:00:00"
else:
    time = "11:00:00"
schedule.every().day.at(time).do(schedule_task_at_specific_time)
while True:
    schedule.run_pending()
