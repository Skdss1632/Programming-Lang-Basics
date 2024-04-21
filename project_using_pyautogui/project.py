import schedule
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


def schedule_task_at_specific_time():
    """This program is designed to function correctly only on the Chrome browser with the page zoom set to 100%.
    If the browser or page size is changed,
    the program may not operate properly and also do not change the browser position on home page."""

    open_chrome_browser_with_irctc_page()
    if wait_until_image_visible("/home/intern/Pictures/Screenshots/login_btn.png"):
        login_irctc_account(username="skdss16321",
                          password="Sourav99#", captcha_fill_delay=10)


    # pyautogui.sleep(2)
    # click_browsers()
    input_journey_details(from_="NEW DELHI", to="SAMASTIPUR", booking_date="01/08/2024")

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/sleeper_refresh.png"):
        select_coach_type_for_booking(coach_type="sleeper")

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/available_ticket.png"):
        click_available_btn()
        click_book_now()

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/add_infant_without_berth.png"):
        click_passenger_name_fld()
        select_passenger_name(input_passenger_name_index=7)
        scroll_to_continue_btn(-7)
        click_book_only_if_confirm_berth_alloted()
        click_continue_btn_inside_passenger_details()

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/view_cancellation_policy.png"):
        scroll_to_continue_btn(-6)

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/continue_btn.png"):
        click_continue_btn_inside_review_journey(captcha_fill_delay=10, image_path="/home/intern/Pictures/Screenshots/continue_btn.png")

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/irctc_ewallet.png"):
        click_irctc_e_wallet()
        click_pay_and_book()

    if wait_until_image_visible("/home/intern/Pictures/Screenshots/confirm_btn.png"):
        click_confirm_btn_inside_otp(otp_fill_delay=10)


# # Schedule the task to run at 11:00 AM every day
# schedule.every().day.at("15:56").do(Schedule_task_at_specific_time)

# while True:
#     schedule.run_pending()


schedule_task_at_specific_time()



































