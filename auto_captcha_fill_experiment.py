from Programming_Lang_Basics.project_using_pyautogui.utility_functions import *

click_browsers()
py.sleep(2)

# Define the coordinates of the region you want to capture
# Replace these coordinates with the coordinates of the area containing the text
region_x = 100
region_y = 100
region_width = 400
region_height = 200

# Capture the screenshot of the specified region
screenshot = py.screenshot(region=(region_x, region_y, region_width, region_height))

# Save the screenshot to a file
screenshot_path = "region_screenshot.png"
screenshot.save(screenshot_path)

# Perform OCR using Tesseract
extracted_text = pytesseract.image_to_string(Image.open(screenshot_path))

# Print the extracted text
print("Extracted Text:")
print(extracted_text)







