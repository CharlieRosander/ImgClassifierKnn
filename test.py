from PIL import Image
from numpy import asarray
import math
import os
import numpy as np

# Globala variabler för path till katt/hund bilderna
KATT_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"
HUND_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"


# Formel/funktion för att räkna ut distansen mellan pixlar, x1 = pixelvärde från bild 1, x2 = pixelvärde från bild 2
def uträkning(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)

# TRAIN-BILDERNA
# Öppnar, konverterar till svartvit, resize, gör till array och sen reshape:ar arrayen så varje bilds värden samlas
# som en lista i listan, samt lägger till det i listan. Varje hunds värden blir då till ett element så man kan
# separera allas värden
hund_pixel_lista = []
for filename in os.listdir(HUND_DIR):
    f = os.path.join(HUND_DIR, filename)
    if os.path.isfile(f):
        hund_img = Image.open(f)
        hund_img = hund_img.convert("L")
        hund_img = hund_img.resize((30, 30))
        hund_data = np.array(hund_img, int)
        new_shape = hund_data.reshape(-1)
        hund_pixel_lista.append(new_shape)

# TRAIN-BILDERNA
# Öppnar, konverterar till svartvit, resize, gör till array och sen reshape:ar arrayen så varje bilds värden samlas
# som en lista i listan, samt lägger till det i listan. Varje katts värden blir då till ett element så man kan
# separera allas värden
katt_pixel_lista = []
for filename in os.listdir(KATT_DIR):
    f = os.path.join(KATT_DIR, filename)
    if os.path.isfile(f):
        katt_img = Image.open(f)
        katt_img = katt_img.convert("L")
        katt_img = katt_img.resize((2, 2))
        katt_data = np.array(katt_img, int)
        new_shape = katt_data.reshape(-1)
        katt_pixel_lista.append(new_shape)

# TEST-BILD
# Öppnar och konverterar test bilden
test1 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test/11.jpg")
test1 = test1.convert("L")
test1 = test1.resize((2, 2))
test1_data = np.array(test1, int)

# Lägger in pixel-värdena från test bilden i en lista
test_img_value_list = []
for row2 in test1_data:
    for value2 in row2:
        test_img_value_list.append(value2)

# Summerar varje enskild bilds värde och lägger det i en lista som en egen lista
pixel_värde_katt = []
katt_count = 0
for i in katt_pixel_lista:
    summa_av_bild = sum(i)
    pixel_värde_katt.append(f"Katt {katt_count}: {[summa_av_bild]}")
    katt_count += 1

# distance_list = []
# index = 0
# while index < len(hund_pixel_lista):
#     x1 = hund_pixel_lista[index]
#     x2 = test_value_list[index]
#     index += 1
#     distance_list.append(uträkning(x1, x2))
#
#     if index == len(hund_pixel_lista):
#         break


print(katt_pixel_lista)
print(pixel_värde_katt)
# print(test_value_list)
