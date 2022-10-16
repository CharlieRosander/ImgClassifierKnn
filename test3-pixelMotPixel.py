import numpy
from PIL import Image
from numpy import asarray
import math
import os
import matplotlib.pyplot as plt


def uträkning(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)


# katt_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"
# ls = []
# summa = 0
# for filename in os.listdir(katt_dir):
#     f = os.path.join(katt_dir, filename)
#     if os.path.isfile(f):
#         img = Image.open(f)
#         img = img.convert("L")
#         img = img.resize((4, 4))
#         numpydata = asarray(img)
#         ls.append(numpydata)
#
#
# hund_dir = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
# ls2 = []
# summa = 0
# counter = 0
# for filename in os.listdir(hund_dir):
#     f = os.path.join(hund_dir, filename)
#     if os.path.isfile(f):
#         img = Image.open(f)
#         img = img.convert("L")
#         img = img.resize((2, 2))
#         numpydata = asarray(img)

dog1 = Image.open('images/hund/dog.3.jpg')
dog1 = dog1.convert("L")
dog1 = dog1.resize((4, 4))
dog_data1 = asarray(dog1)

dog2 = Image.open('images/hund/dog.21.jpg')
dog2 = dog2.convert("L")
dog2 = dog2.resize((4, 4))
dog_data2 = asarray(dog2)

cat1 = Image.open('images/katt/cat.14.jpg')
cat1 = cat1.convert("L")
cat1 = cat1.resize((4, 4))
cat_data1 = asarray(cat1)

cat2 = Image.open('images/katt/cat.38.jpg')
cat2 = cat2.convert("L")
cat2 = cat2.resize((4, 4))
cat_data2 = asarray(cat2)

test1 = Image.open("images/test/2.jpg")
test1 = test1.convert("L")
test1 = test1.resize((4, 4))
test1_data = asarray(test1)

dog_value_list = []
for row in dog_data1:
    for value in row:
        dog_value_list.append(value)
print(f"Hund värde: {dog_value_list}")


test_value_list = []
for row2 in test1_data:
    for value2 in row2:
        test_value_list.append(value2)
print(f"Test-bild värde: {test_value_list}")

distance_list = []
index = 0
while index < len(dog_value_list):
    x1 = dog_value_list[index]
    x2 = test_value_list[index]
    index += 1
    distance_list.append(uträkning(x1, x2))

    if index == len(dog_value_list):
        break

print(f"Distans-värde mellan pixlarna: {distance_list}")
