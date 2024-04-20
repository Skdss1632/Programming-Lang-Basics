from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


def Schedule_task_at_specific_time():
    # open_chrome_browser_with_irctc_page()
    # if wait_until_image_found("/home/intern/Pictures/Screenshots/login_btn.png"):
    #     login_irctc_account(username="skdss16321", password="Sourav99#", sleep_time_to_fill_captcha=10)
    pyautogui.sleep(3)
    journey_details(from_="dalsinghsarai", to="samastipur", select_date_for_tatakal="01/08/2024")

    if wait_until_image_found("/home/intern/Pictures/Screenshots/sleeper_refresh.png"):
        select_coach_type_for_booking(coach_type="sleeper")

    if wait_until_image_found("/home/intern/Pictures/Screenshots/avalible_ticket.png"):
        click_on_available_btn()
        click_on_book_now()

    if wait_until_image_found("/home/intern/Pictures/Screenshots/add_infrant_without_berth.png"):
        click_on_passenger_name_input_fld()
        select_passenger_name()
        scroll_to_continue_btn(-7)
        click_on_book_only_if_confirm_berth_are_alloted_checkbox()
        click_on_continue_btn_inside_passenger_details()

    if wait_until_image_found("/home/intern/Pictures/Screenshots/view_cancellation_policy.png"):
        scroll_to_continue_btn(-6)

    if wait_until_image_found("/home/intern/Pictures/Screenshots/continue_btn.png"):
        click_on_continue_btn_inside_review_journey(sleep_time_to_fill_captcha=10, image_path="/home/intern/Pictures/Screenshots/continue_btn.png")

    if wait_until_image_found("/home/intern/Pictures/Screenshots/irctc_ewallet.png"):
        click_on_irctc_ewallet()
        click_and_pay()

    if wait_until_image_found("/home/intern/Pictures/Screenshots/confirm_btn.png"):
        click_on_confirm_btn_inside_otp(sleep_time_to_fill_otp=5)


Schedule_task_at_specific_time()




# Schedule the task to run at 11:00 AM every day
# schedule.every().day.at("03:44").do(my_task)

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     pyautogui.sleep(1)  # Sleep for 1 second to avoid high CPU usage

# my_task()




























