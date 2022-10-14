from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np


def calculate_distance(i1, i2):
    summa = numpy.sum((i1 - i2) ** 2)
    return summa


katt_dir = 'C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/katt'
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

hund_dir = 'C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/hund'
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

test1 = Image.open("images/test/1.jpg")
test1 = test1.convert("L")
test1 = test1.resize((30,30))
test1_arr = asarray(test1)
test1_sum = test1_arr.sum()

test2 = Image.open("images/test/5.jpg")
test2 = test2.convert("L")
test2 = test2.resize((30,30))
test2_arr = asarray(test2)
test2_sum = test2_arr.sum()

test3 = Image.open("images/test/2.jpg")
test3 = test3.convert("L")
test3 = test3.resize((30,30))
test3_arr = asarray(test3)
test3_sum = test3_arr.sum()


print(f"Test 1(Hund) med hund medelV: {math.sqrt((medelvärdeH - test1_sum)**2)}")
print(f"Test 1(Hund) med katt medelV: {math.sqrt((medelvärdeK - test1_sum)**2):.2f}")
print("")
print(f"Test 2(Katt) med hund medelV: {math.sqrt((medelvärdeH - test2_arr.sum())**2)}")
print(f"Test 2(Katt) med katt medelV: {math.sqrt((medelvärdeK - test2_arr.sum())**2):.2f}")
print("")
print(f"Test 3(Hund) med hund medelV: {math.sqrt((medelvärdeH - test3_sum)**2)}")
print(f"Test 3(Hund) med katt medelV: {math.sqrt((medelvärdeK - test3_sum)**2):.2f}")