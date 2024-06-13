from Programming_Lang_Basics.automation_project.utility_functions import *
click_browser()
py.sleep(1)
# py.scroll(-1)
train_name_img_path = get_image_path("train_name_image")
scroll_until_element_visible_not_visible(img_path=train_name_img_path)

