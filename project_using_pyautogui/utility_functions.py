import pyautogui
import pytesseract
# from PIL import Image
# import schedule
# import time
# import datetime
#
# from selenium.webdriver.edge.webdriver import WebDriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC


def click_on_browsers():
    pyautogui.moveTo(74, 175)
    # pyautogui.click(x=74, y=175)
    pyautogui.sleep(2)
    pyautogui.click()


def click_on_login_btn():
    pyautogui.moveTo(543, 140)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(1)


def open_new_tab():
    pyautogui.keyDown('ctrl')
    pyautogui.press('t')
    pyautogui.keyUp('ctrl')



def open_url():
    # pyautogui.write("https://www.irctc.co.in/nget/train-search")
    # pyautogui.sleep(3)
    # pyautogui.press('enter')
    # pyautogui.sleep(1)
    url = "https://www.irctc.co.in/nget/train-search"

    # Iterate through each character in the URL and type it slowly
    for char in url:
        pyautogui.write(char)
    pyautogui.press("enter")



# def get_image_txt():
#     # Take a screenshot of the area containing the text
#     # screenshot = pyautogui.screenshot(region=(x, y, 559, 716))   # Adjust x, y, width, height as needed
#
#     # Save the screenshot image temporarily
#     # screenshot.save('screenshot.png')
#
#     # Perform OCR on the saved image
#     text = pytesseract.image_to_string(Image.open('screenshot.png'))
#
#     # Print the extracted text
#     print(text)


def click_on_sinin_btn():
    pyautogui.moveTo(639, 867)
    pyautogui.sleep(1)
    pyautogui.click()


def click_on_available_btn():
    pyautogui.moveTo(651, 603)
    pyautogui.sleep(1)
    pyautogui.click()




def click_on_book_now():
    pyautogui.click(x=600, y=709)


def click_on_passenger_name_input_fld():
    pyautogui.click(x=214, y=737)
    pyautogui.sleep(1)


def select_passenger_name():
    pyautogui.click(x=201, y=719)
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.sleep(1)
    pyautogui.press("down", presses=7)
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.press("enter")


def click_on_book_only_if_confirm_berth_are_alloted_checkbox():
    pyautogui.moveTo(768, 413)
    pyautogui.sleep(2)
    pyautogui.click()


def click_on_continue_btn_inside_passenger_details():
    pyautogui.click(x=199, y=935)
    pyautogui.sleep(1)


def click_on_continue_btn_inside_review_journey(sleep_time_to_fill_captcha: int):
    pyautogui.sleep(sleep_time_to_fill_captcha)
    pyautogui.moveTo(200, 516)
    pyautogui.sleep(1)
    pyautogui.click()


def click_on_irctc_ewallet():
    pyautogui.moveTo(159, 481)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(1)


def click_on_pay_and_book():
    pyautogui.click(x=647, y=548)


def click_on_search_btn():
    pyautogui.moveTo(238, 690)
    pyautogui.sleep(1)
    pyautogui.click()


def input_station_name(catch_train_station_name: str, to: str):
    pyautogui.moveTo(280, 424)
    pyautogui.sleep(1)
    pyautogui.click()
    clear_input_fld()
    pyautogui.write(catch_train_station_name)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.press("enter")


    pyautogui.moveTo(250, 495)
    pyautogui.sleep(1)
    pyautogui.click()
    clear_input_fld()
    pyautogui.write(to)
    pyautogui.press("shift")
    pyautogui.press("down")
    pyautogui.sleep(1)
    pyautogui.press("shift")
    pyautogui.press("enter")


def select_coach_type_for_booking_from_dropdown(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.moveTo(691, 489)
        pyautogui.sleep(1)
        pyautogui.click()
        pyautogui.press("shift")
        pyautogui.sleep(1)
        pyautogui.press("down", presses=11)
        pyautogui.sleep(1)
        pyautogui.press("shift")
        pyautogui.sleep(1)
        pyautogui.press("enter")

    if coach_type == "ac 3 tier":
        pyautogui.moveTo(691, 489)
        pyautogui.sleep(2)
        pyautogui.click()
        pyautogui.press("shift")
        pyautogui.sleep(2)
        pyautogui.press("down", presses=7)
        pyautogui.sleep(2)
        pyautogui.press("shift")
        pyautogui.press("enter")

def select_date_for_tatakal_booking():
    pyautogui.moveTo(764, 426)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.sleep(1)
    clear_input_fld()
    pyautogui.sleep(1)
    pyautogui.write("01/08/2024")
    pyautogui.sleep(1)
    pyautogui.press("enter")




    # pyautogui.click()
    # pyautogui.sleep(2)
    # pyautogui.moveTo(850, 647)
    # pyautogui.click()
    # pyautogui.sleep(2)

def clear_input_fld():
    # Press and hold Ctrl, then press A (to select all)
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')


def select_tatkal_from_dropdown():
    pyautogui.moveTo(255, 561)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(255, 764)
    pyautogui.sleep(1)
    pyautogui.click()



def select_coach_type_for_booking(coach_type: str):
    if coach_type == "sleeper":
        pyautogui.moveTo(617, 571)
        pyautogui.sleep(1)
        pyautogui.click()


def input_username_and_password_of_irctc_account(username: str, password: str) -> object:
    pyautogui.moveTo(611, 341)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
    pyautogui.write(username)
    pyautogui.sleep(1)

    pyautogui.moveTo(558, 391)
    pyautogui.sleep(1)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
    pyautogui.write(username)
    pyautogui.sleep(1)



def scroll_to_continue_btn():
    # pyautogui.scroll(-10)
    scrolls = 20
    # Loop to simulate scrolling down
    for _ in range(scrolls):
        pyautogui.press('down')  # Simulate pressing the down arrow key
    pyautogui.sleep(2)

















