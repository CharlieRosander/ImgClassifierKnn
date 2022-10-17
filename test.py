from PIL import Image
from numpy import asarray
import math
import os
import numpy as np

# Globala variabler för path till katt/hund bilderna
KATT_DIR = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/katt"
HUND_DIR = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/hund"


# Formel/funktion för att räkna ut distansen mellan pixlar, x1 = pixelvärde från bild 1, x2 = pixelvärde från bild 2
def beräkna_pixel_distans(i1, i2):
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
        hund_data = hund_data.flatten()
        hund_data = hund_data.tolist()
        hund_pixel_lista.append(hund_data)

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
        katt_img = katt_img.resize((30, 30))
        katt_data = np.array(katt_img)
        katt_data = katt_data.flatten()
        katt_data = katt_data.tolist()
        katt_pixel_lista.append(katt_data)

# TEST-BILD
# Öppnar och konverterar test bilden
test1 = Image.open("C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test/11.jpg")
test1 = test1.convert("L")
test1 = test1.resize((30, 30))
test1_data = np.array(test1)
pixel_värde_test = test1_data.sum()

# Lägger in pixel-värdena från test bilden i en lista
test_img_value_list = []
for row2 in test1_data:
    for value2 in row2:
        test_img_value_list.append(value2)
print(test_img_value_list)

# Summerar varje enskild katts värde och lägger det i en lista som en egen lista
pixel_värde_katt = []
katt_count = 0
for i in katt_pixel_lista:
    summa_av_katt_bild = sum(i)
    pixel_värde_katt.append(f"Katt {katt_count}: {[summa_av_katt_bild]}")
    katt_count += 1

# Summerar varje enskild hunds värde och lägger det i en lista som en egen lista
pixel_värde_hund = []
hund_count = 0
for i in hund_pixel_lista:
    summa_av_hund_bild = sum(i)
    pixel_värde_hund.append(f"Hund {hund_count}: {[summa_av_hund_bild]}")
    hund_count += 1

# Beräknar distansen mellan varje enskild pixel mellan katt och test
# katt_distance_list = []
# index1 = 0
# while index1 <= len(katt_pixel_lista):
#     x1 = katt_pixel_lista[index1]
#     x2 = test_img_value_list[index1]
#     index1 += 1
#     katt_distance_list.append(beräkna_pixel_distans(x1, x2))
#
#     if index1 == len(katt_pixel_lista):
#         break
#
# # Beräknar distansen mellan varje enskild pixel mellan hund och test
# hund_distance_list = []
# index2 = 0
# while index2 <= len(hund_pixel_lista):
#     x1 = hund_pixel_lista[index2]
#     x2 = test_img_value_list[index2]
#     index2 += 1
#     hund_distance_list.append(beräkna_pixel_distans(x1, x2))
#
#     if index2 == len(hund_pixel_lista):
#         break


# print(katt_distance_list)
# print(hund_distance_list)


print(katt_pixel_lista)
print(hund_pixel_lista)

print(pixel_värde_katt)
print(pixel_värde_hund)
print(pixel_värde_test)
# print(test_img_value_list)
