from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np

katt_dir = 'C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/katt'
ls = []
summa = 0
for filename in os.listdir(katt_dir):
    f = os.path.join(katt_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((300, 300))
        numpydata = asarray(img)
        summa = numpydata.sum()
        ls.append(summa)

medelvärdeK = sum(ls) / len(ls)
print(f'Medelvärdet på kattbilderna är : {medelvärdeK}')

hund_dir = 'C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/hund'
ls2 = []
summa = 0
for filename in os.listdir(hund_dir):
    f = os.path.join(hund_dir, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((300, 300))
        numpydata = asarray(img)
        summa = numpydata.sum()
        ls2.append(summa)

medelvärdeH = sum(ls2) / len(ls2)
print(f'Medelvärdet på hundbilderna är : {medelvärdeH}')

test_list = []
test_dir = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test"
for filename in os.listdir(test_dir):
    f = os.path.join(test_dir, filename)
    if os.path.isfile(f):
        test_img = Image.open(f)
        test_img = test_img.convert("L")
        test_img = test_img.resize((300, 300))
        test_data = asarray(test_img)
        summa = test_data.sum()
        test_list.append(summa)

# print(test_list)

distance_list = []
for index, each_value in enumerate(test_list):
    # counter_sum = str(counter)
    distance_value = math.sqrt((medelvärdeH - each_value) ** 2)
    distance_list.append(f"Test {index + 1} med hund medelvärde: {distance_value:.2f}")

for e in distance_list:
    print(e)
# print(f"Test 1(Hund) med hund medelV: {math.sqrt((medelvärdeH - test1_sum)**2)}")
