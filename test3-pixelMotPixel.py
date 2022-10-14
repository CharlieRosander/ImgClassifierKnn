from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np
import matplotlib.pyplot as plt


def uträkning(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)


dog1 = Image.open('images/hund/dog.3.jpg')
dog1 = dog1.convert("L")
dog1 = dog1.resize((2, 2))
dog_data1 = asarray(dog1)

test1 = Image.open("images/test/2.jpg")
test1 = test1.convert("L")
test1 = test1.resize((2, 2))
test1_data = asarray(test1)

# plot = plt.imshow(test1_data)
# plt.show()

value_list = []
for row in dog_data1:
    for value in row:
        value_list.append(value)

print(value_list)

value_list2 = []
for row2 in test1_data:
    for value2 in row2:
        value_list2.append(value2)

print(value_list2)

distance_list = []
counter2 = len(value_list)
print(counter2)
counter = 0
index = 0
while counter < counter2:
    x1 = value_list[index]
    x2 = value_list2[index]
    index += 1
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
    distance_list.append(uträkning(x1, x2))
    print(distance_list)
    if index == counter2:
        break
# for i in value_list:
#     x1 = i
#     print(f"I är : {i}")
#     for k in value_list2:
#         x2 = k
#         print(f"k är: {k}")
#         summa = math.sqrt((float(x1) - float(x2)) ** 2)
#         distance_list.append(summa)
#
# print(distance_list)
# uträkning(x1, x2)
# print(value_list)
# print(value_list2)
