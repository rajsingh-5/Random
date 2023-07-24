import numpy as np
from keras_ocr import Reader

image = np.imread("D:/Projects/MobileImageAutomation/sourceBase/flip.png")

reader = Reader()

lines = reader.readtext(image)

for line in lines:
    print(line.text, line.coordinates)
