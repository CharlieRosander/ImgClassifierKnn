from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np


def calculate_distance(i1, i2):
    summa = numpy.sum((i1 - i2) ** 2)
    return summa


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

