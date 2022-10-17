from PIL import Image
from numpy import asarray
import math
import os
import numpy as np

# Globala variabler för path till katt/hund bilderna
KATT_DIR = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/katt"
HUND_DIR = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/hund"

test1 = Image.open("C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test/11.jpg")
test1 = test1.convert("L")
test1 = test1.resize((2, 2))
test1_data = np.array(test1)
test1_data = test1_data.ravel()
test1_data = test1_data.tolist()

test2 = Image.open("C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test/9.jpg")
test2 = test2.convert("L")
test2 = test2.resize((2, 2))
test2_data = np.array(test2)
new_shape = test2_data.reshape(-1)

test3 = Image.open("C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test/9.jpg")
test3 = test3.convert("L")
test3 = test3.resize((2, 2))
test3_data = np.array(test3)
test3_data = test3_data.flatten()
test3_data = test3_data.tolist()


hund_lista = []
hund_lista.append(f"Ravel: {test1_data}")
hund_lista.append(new_shape)
hund_lista.append(f"Flatten: {test3_data}")



print(test1_data)
print(type(test1_data))
print(new_shape)
print(type(new_shape))
print(test3_data)
print(type(test3_data))
print(hund_lista)