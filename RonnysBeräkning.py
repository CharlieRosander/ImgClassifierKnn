from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np

bild = ''
pixelavstånd = []

directory = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
directory1 = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"


knn_result = []
def räknare():
    varv1 = 0
    while True:
        while True:
            varv1 += 1

            lägsta = pixelavstånd[0]
            index1 = 0

            for i, x in enumerate(pixelavstånd):

                if x < lägsta:
                    lägsta = x
                    index1 = i
            if index1 <= 300:
                bild = 'Hund'
                break
            if index1 >= 300:
                bild = 'Katt'
                break

        knn_result.append(bild)
        print(f'Det minsta avståndet är {lägsta} på bild nr {index1}, som är en {bild}')

        del pixelavstånd[index1]

        if varv1 == 11:
            break
        else:
            continue


def uträkning(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)


def matrix(x, y):
    value_list = []
    for row in data1:
        for value in row:
            value_list.append(value)

    distance_list = []
    index = 0

    while index < len(value_list):
        x1 = value_list[index]
        x2 = test_value_list[index]
        index += 1
        distance_list.append(uträkning(x1, x2))

        if index == len(value_list):
            variabel = sum(distance_list)
            pixelavstånd.append(variabel)
            break

    # print(f"Distans-värde mellan pixlarna: {distance_list}")


test1 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test/1.jpg")
test1 = test1.convert("L")
test1 = test1.resize((50, 50))
test1_data = asarray(test1)
test1_sum = test1_data.sum()

test_value_list = []
for row2 in test1_data:
    for value2 in row2:
        test_value_list.append(value2)

pixel_värde_hund = []
varv = 0
for filename in os.listdir(directory):
    varv += 1
    # print(f'Hundbild nr : {varv}')
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((50, 50))
        data1 = asarray(img)
        data1_sum = data1.sum()
        # pixel_värde_hund.append(data1.sum())
        matrix(test1_sum, data1_sum)

pixel_värde_katt = []
varv = 0
for filename in os.listdir(directory1):
    bild = filename
    varv += 1
    # print(f'Kattbild nr : {varv}')
    f = os.path.join(directory1, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((50, 50))
        data1 = asarray(img)

        # pixel_värde_katt.append(data1.sum())
        matrix(test1_sum, data1_sum)

# print(test1_sum)
räknare()
antal_hundar = knn_result.count("Hund")
antal_katter = knn_result.count("Katt")
if antal_hundar < antal_katter:
    print("Bilden är en katt")
else:
    print("Bilden är en hund")
print(pixelavstånd)
# print(data1_sum)
# print(pixel_värde_katt)
# print(pixel_värde_hund)
# print(test1_sum)
