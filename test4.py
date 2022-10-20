from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np

HUND_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
KATT_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"

knn_result = []
min_distance_and_label = []


# Funktion för att sortera distanserna i storleksordning, sen ta dom k minsta och lägga till dom i en ny lista
# med namnet på bilden samt värdet
def knn():
    knn_list = distance_list_hund + distance_list_katt
    knn_list.sort()
    k_värde = 11

    for l2_value in label_and_l2_value:
        for value in knn_list[0:k_värde]:
            if value == l2_value[1]:
                min_distance_and_label.append(l2_value)
                break


# Funktion för att räkna rösterna och klasifficera bilden
def vote_count():
    hund_count = 0
    katt_count = 0

    while True:
        for label_and_value in min_distance_and_label:
            for label in label_and_value:
                if "Hund" in label:
                    hund_count += 1
                if "Katt" in label:
                    katt_count += 1
                print(label_and_value)
                break

        if hund_count < katt_count:
            print("Bilden är en katt")
            break
        else:
            print("Bilden är en hund")
            break


def euklides_formel(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)


# Går igenom hund värdena och skickar det till uträknaren och lägger sedan till det värdet i distance_list_hund
distance_list_hund = []
label_and_l2_value = []


def hund_mot_test(train, test):
    index = 0
    while index < len(hund_pixel_sum):
        x1 = hund_pixel_sum[index]
        x2 = test_pixel_sum[0]
        index += 1
        label_and_l2_value.append([f"Hund {index}", euklides_formel(x1, x2)])
        distance_list_hund.append(euklides_formel(x1, x2))

# Går igenom katt värdena och skickar det till uträknaren och lägger sedan till det värdet i distance_list_katt
distance_list_katt = []


def katt_mot_test(train, test):
    index = 0
    while index < len(katt_pixel_sum):
        x1 = katt_pixel_sum[index]
        x2 = test_pixel_sum[0]
        index += 1
        label_and_l2_value.append([f"Katt {index}", euklides_formel(x1, x2)])
        distance_list_katt.append(euklides_formel(x1, x2))

# Öppnar test bilden,
test_pixel_sum = []
test_img1 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test/6.jpg")
test_img1 = test_img1.convert("L")
test_img1 = test_img1.resize((50, 50))
test1_data = asarray(test_img1)
test1_data_sum = test1_data.sum()
test_pixel_sum.append(test1_data_sum)

# HUNDAR
# Öppnar och konverterar hundbilderna, samt summerar pixelvärdena i bilden
hund_pixel_sum = []
for filename in os.listdir(HUND_DIR):
    f = os.path.join(HUND_DIR, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((50, 50))
        hund_data = asarray(img)
        hund_data_sum = hund_data.sum()
        hund_pixel_sum.append(hund_data_sum)

hund_mot_test(hund_pixel_sum, test_pixel_sum)

# KATTER
# Öppnar och konverterar kattbilderna
katt_pixel_sum = []
for filename in os.listdir(KATT_DIR):
    f = os.path.join(KATT_DIR, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        img = img.convert("L")
        img = img.resize((50, 50))
        katt_data = asarray(img)
        katt_data_sum = katt_data.sum()
        katt_pixel_sum.append(katt_data_sum)

katt_mot_test(katt_pixel_sum, test_pixel_sum)

knn()
vote_count()
