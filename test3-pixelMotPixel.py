from PIL import Image
from numpy import asarray
import math
import os
import numpy as np

KATT_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"
HUND_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
TEST_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test"


def euklides_formel(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)

# def count_pixel_dist(x1, x2):


katt_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"
for filename in os.listdir(katt_dir):
    f = os.path.join(katt_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((50, 50))
        numpydata = asarray(img)

hund_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
for filename in os.listdir(hund_dir):
    f = os.path.join(hund_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((50, 50))
        numpydata = asarray(img)
        print(numpydata)
    dog_value_list = []
    for row in numpydata:
        for value in row:
            dog_value_list.append(value)
            # print(dog_value_list)

# test1 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test/2.jpg")
# test1 = test1.convert("L")
# test1 = test1.resize((50, 50))
# test1_data = asarray(test1)
#
#
# print(f"Hund värde: {dog_value_list}")
#
# test_value_list = []
# for row2 in test1_data:
#     for value2 in row2:
#         test_value_list.append(value2)
# print(f"Test-bild värde: {test_value_list}")
#
# distance_list = []
# index = 0
# while index < len(dog_value_list):
#     x1 = dog_value_list[index]
#     x2 = test_value_list[index]
#     index += 1
#     distance_list.append(euklides_formel(x1, x2))
#
#     if index == len(dog_value_list):
#         break
#
# print(f"Distans-värde mellan pixlarna: {distance_list}")
