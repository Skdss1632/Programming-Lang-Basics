
from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


def my_task():
    click_on_browsers()
    open_new_tab()
    open_url()
    click_on_login_btn()
    input_username_and_password_of_irctc_account(username="skdss16321", password="Sourav99#")
    pyautogui.sleep(10)
    click_on_sinin_btn()
    input_station_name(catch_train_station_name="new delhi", to="samastipur")
    select_coach_type_for_booking_from_dropdown(coach_type="sleeper")
    # select_tatkal_from_dropdown()
    select_date_for_tatakal_booking()
    click_on_search_btn()
    select_coach_type_for_booking(coach_type="sleeper")
    click_on_available_btn()
    click_on_book_now()
    click_on_passenger_name_input_fld()
    select_passenger_name()
    scroll_to_continue_btn()
    click_on_book_only_if_confirm_berth_are_alloted_checkbox()
    click_on_continue_btn_inside_passenger_details()
    scroll_to_continue_btn()
    click_on_continue_btn_inside_review_journey(sleep_time_to_fill_captcha= 10)
    click_on_irctc_ewallet()




# Schedule the task to run at 11:00 AM every day
# schedule.every().day.at("03:44").do(my_task)

# # Run the scheduler
# while True:
#     schedule.run_pending()
#     pyautogui.sleep(1)  # Sleep for 1 second to avoid high CPU usage

my_task()
























