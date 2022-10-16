from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np

katt_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"
ls = []
summa = 0
for filename in os.listdir(katt_dir):
    f = os.path.join(katt_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((30, 30))
        numpydata = asarray(img)
        summa = numpydata.sum()
        ls.append(summa)

medelvärdeK = sum(ls) / len(ls)
print(f'Medelvärdet på kattbilderna är : {medelvärdeK}')

hund_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
ls2 = []
summa = 0
for filename in os.listdir(hund_dir):
    f = os.path.join(hund_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((30, 30))
        numpydata = asarray(img)
        summa = numpydata.sum()
        ls2.append(summa)

medelvärdeH = sum(ls2) / len(ls2)
print(f'Medelvärdet på hundbilderna är : {medelvärdeH}')
# print(ls2)

# test_list = []
# test_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test"
# for filename in os.listdir(test_dir):
#     f = os.path.join(test_dir, filename)
#     if os.path.isfile(f):
#         test_img = Image.open(f)
#         test_img = test_img.convert("L")
#         test_img = test_img.resize((30, 30))
#         test_data = asarray(test_img)
#         summa = test_data.sum()
#         test_list.append(summa)


test1 = Image.open("images/test/7.jpg")
test1 = test1.convert("L")
test1 = test1.resize((4, 4))
test1_data = asarray(test1).sum()

# print(test_list)

# distance_list = []
# for index, each_value in enumerate(test_list):
#     distance_value = math.sqrt((medelvärdeH - each_value) ** 2)
#     distance_list.append(f"Test {index + 1} med hund medelvärde: {distance_value:.2f}")
#
# for e in distance_list:
#     print(e)
# print(test_list)
distance_dog_list = []
dist_list = []
for dog_nr, dog_value in enumerate(ls2):
    distance_value = math.sqrt((float(dog_value) - float(test1_data)) ** 2)
    distance_dog_list.append(f"Test 1(Hund) med hund {dog_nr + 1}: {distance_value:.2f}")
    dist_list.append(distance_value)
# for e in distance_dog_list:
    # print(e)

dist_list.sort()
print(dist_list)



distance_cat_list = []
dist_list2 = []
for cat_nr, cat_value in enumerate(ls):
    distance_value2 = math.sqrt((float(cat_value) - float(test1_data)) ** 2)
    distance_cat_list.append(f"Test 1(Hund) med katt {cat_nr + 1}: {distance_value2:.2f}")
    dist_list2.append(distance_value2)
# for e in distance_cat_list:
    # print(e)

dist_list2.sort()
print(dist_list2)
print(len(dist_list))
print(len(dist_list2))
print(sum(dist_list), sum(dist_list2))