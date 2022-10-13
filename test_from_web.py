from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
from collections import Counter

# Öppna och skapa arrays av tränings-bilderna
reference_image_1 = Image.open('images/dog.3.jpg')
reference_image_1.resize((30, 30))
reference_image_arr1 = np.asarray(reference_image_1)
# print(np.shape(reference_image_arr1))

reference_image_2 = Image.open('images/cat.7.jpg')
reference_image_2.resize((30, 30))
reference_image_arr2 = np.asarray(reference_image_2)
# print(np.shape(reference_image_arr2))

# Öppna och skapa arrays av test-bild
test_image_1 = Image.open('images/1.jpg')
test_image_1.resize((30, 30))
test_image_arr = np.asarray(test_image_1)

# "Flatten", gör bilderna 1D, alltså svartvita
flat_array_1 = reference_image_arr1.flatten()
flat_array_2 = reference_image_arr2.flatten()
flat_array_3 = test_image_arr.flatten()

print(np.shape(flat_array_1))
# print(np.shape(flat_array_2))
# print(np.shape(flat_array_3))

RH1 = Counter(flat_array_1)
H1 = []
for i in range(0, 256):
    if i in RH1.keys():
        H1.append(RH1[i])
    else:
        H1.append(0)
print(H1)
RH2 = Counter(flat_array_2)
H2 = []
for i in range(256):
    if i in RH2.keys():
        H2.append(RH2[i])
    else:
        H2.append(0)

RH3 = Counter(flat_array_3)
H3 = []
for i in range(256):
    if i in RH3.keys():
        H3.append(RH3[i])
    else:
        H3.append(0)


def L2Norm(H1, H2):
    distance = 0
    for i in range(len(H1)):
        distance += np.square(H1[i] - H2[i])
    return np.sqrt(distance)


# dist_test_ref_1 = L2Norm(H1, flat_array_3)
# print("The distance between Reference_Image_1 and Test Image is : {}".format(dist_test_ref_1))
#
# dist_test_ref_2 = L2Norm(H2, flat_array_3)
# print("The distance between Reference_Image_2 and Test Image is : {}".format(dist_test_ref_2))
