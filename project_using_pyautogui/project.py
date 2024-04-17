from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *


# pyautogui.sleep(5)
# print(pyautogui.position())




click_on_browsers()
open_new_tab()
open_url()
click_on_login_btn()
click_on_username_input_fld()

pyautogui.sleep(20)
click_on_sinin_btn()

input_station_name(catch_train_station_name="new delhi", to="samastipur")
# select_date_for_tatakal_booking func should be call after input station name-- do not chnage their order
select_date_for_tatakal_booking()
select_coach_type_for_booking_from_dropdown(coach_type="sleeper")
select_tatkal_from_dropdown()

click_on_search_btn()
select_coach_type_for_booking(coach_type="sleeper")
click_on_avalible_btn()
click_on_book_now()







# click_on_passenger_name_input_fld()
# click_on_book_only_if_confirm_berth_are_alloted_checkbox()
# select_passenger_name()
# click_on_continue_btn_inside_passenger_details()
# click_on_continue_btn_inside_review_journey(sleep_time_to_fill_captcha= 20)
# click_on_irctc_ewallet()










