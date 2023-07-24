# from pprint import pprint
#
# from PIL import Image
# import pytesseract
#
# image = Image.open("D:/Projects/MobileImageAutomation/sourceBase/flip.png")
# image = image.convert('L')
# data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
# print(data['char'])

import pytesseract
from PIL import Image

# Load the image
# image = Image.open("D:/Projects/MobileImageAutomation/sourceBase/flip.png")
#
# # Perform OCR and get the text
# extracted_text = pytesseract.image_to_string(image, lang='eng+hin')
# lines = extracted_text.split('\n')
#
# # Iterate through each line and print its text and coordinates
# for line in lines:
#     print("Line:", line)
# Calculate the coordinates for the line (you may need additional processing here)
# x_start, y_start, x_end, y_end = ...
# print("Coordinates:", x_start, y_start, x_end, y_end)


import pytesseract
import pyocr
import pyautogui
image = Image.open("D:/Projects/MobileImageAutomation/sourceBase/flip.png")
extracted_text = pytesseract.image_to_string(image, lang="eng+hin")
# icon_coordinates = pyautogui.locateOnScreen("D:/Projects/MobileImageAutomation/sourceBase/flip.png")
# text_box = image.crop(icon_coordinates)

# Use Tesseract to extract the text from the text box
text = pytesseract.image_to_string(image)
print(text)