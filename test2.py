import math
import numpy
from PIL import Image
from numpy import asarray

# hund_bilder = ['images/dog.1.jpg', 'images/dog.2.jpg', 'images/dog.3.jpg', 'images/dog.4.jpg', 'images/dog.5.jpg',
#                'images'
#                '/dog.6.jpg', 'images/dog.7.jpg', 'images/dog.8.jpg', 'images/dog.9.jpg', 'images/dog.10.jpg']
#
# katt_bilder = ['images/cat.1.jpg', 'images/cat.2.jpg', 'images/cat.3.jpg', 'images/cat.4.jpg', 'images/cat.5.jpg',
#                'images'
#                '/cat.6.jpg', 'images/cat.7.jpg', 'images/cat.8.jpg', 'images/cat.9.jpg', 'images/cat.10.jpg']
katt_list = []
hund_list = []


def calculate_distance(i1, i2):
    summa = numpy.sum((i1 - i2) ** 2)
    hund_list.append(summa)
    return summa


def hund_calc_medelv():
    medel = sum(hund1)


def calculate_distance2(i1, i2):
    summa2 = numpy.sum((i1 - i2) ** 2)
    katt_list.append(summa2)
    return summa2


def calculate_distance3(i1, i2):
    summa = numpy.sum((i1 - i2) ** 2)
    return summa


# Öppna bilden i en variabel
dog1 = Image.open('images/dog.1.jpg')
dog2 = Image.open("images/dog.2.jpg")
dog3 = Image.open("images/dog.3.jpg")
dog4 = Image.open("images/dog.4.jpg")
dog5 = Image.open("images/dog.5.jpg")
dog6 = Image.open("images/dog.6.jpg")
dog7 = Image.open("images/dog.7.jpg")
dog8 = Image.open("images/dog.8.jpg")
dog9 = Image.open("images/dog.9.jpg")
dog10 = Image.open("images/dog.10.jpg")

cat1 = Image.open('images/cat.1.jpg')
cat2 = Image.open("images/cat.2.jpg")
cat3 = Image.open("images/cat.3.jpg")
cat4 = Image.open("images/cat.4.jpg")
cat5 = Image.open("images/cat.5.jpg")
cat6 = Image.open("images/cat.6.jpg")
cat7 = Image.open("images/cat.7.jpg")
cat8 = Image.open("images/cat.8.jpg")
cat9 = Image.open("images/cat.9.jpg")
cat10 = Image.open("images/cat.10.jpg")

# Gör bilden svart-vit
dog1 = dog1.convert("L")
dog2 = dog2.convert("L")
dog3 = dog3.convert("L")
dog4 = dog4.convert("L")
dog5 = dog5.convert("L")
dog6 = dog6.convert("L")
dog7 = dog7.convert("L")
dog8 = dog8.convert("L")
dog9 = dog9.convert("L")
dog10 = dog10.convert("L")

# Ändra bildens storlek till 30x30
dog1 = dog1.resize((30, 30))
dog2 = dog2.resize((30, 30))
dog3 = dog3.resize((30, 30))
dog4 = dog4.resize((30, 30))
dog5 = dog5.resize((30, 30))
dog6 = dog6.resize((30, 30))
dog7 = dog7.resize((30, 30))
dog8 = dog8.resize((30, 30))
dog9 = dog9.resize((30, 30))
dog10 = dog10.resize((30, 30))

cat1 = cat1.convert("L")
cat2 = cat2.convert("L")
cat3 = cat3.convert("L")
cat4 = cat4.convert("L")
cat5 = cat5.convert("L")
cat6 = cat6.convert("L")
cat7 = cat7.convert("L")
cat8 = cat8.convert("L")
cat9 = cat9.convert("L")
cat10 = cat10.convert("L")

# Ändra bildens storlek till 30x30
cat1 = cat1.resize((30, 30))
cat2 = cat2.resize((30, 30))
cat3 = cat3.resize((30, 30))
cat4 = cat4.resize((30, 30))
cat5 = cat5.resize((30, 30))
cat6 = cat6.resize((30, 30))
cat7 = cat7.resize((30, 30))
cat8 = cat8.resize((30, 30))
cat9 = cat9.resize((30, 30))
cat10 = cat10.resize((30, 30))

# Visa bilden
# img.show()


# Gör om bilden till en NuMPy matris
hund1 = asarray(dog1)
hund2 = asarray(dog2)
hund3 = asarray(dog3)
hund4 = asarray(dog4)
hund5 = asarray(dog5)
hund6 = asarray(dog6)
hund7 = asarray(dog7)
hund8 = asarray(dog8)
hund9 = asarray(dog9)
hund10 = asarray(dog10)


katt1 = asarray(cat1)
katt2 = asarray(cat2)
katt3 = asarray(cat3)
katt4 = asarray(cat4)
katt5 = asarray(cat5)
katt6 = asarray(cat6)
katt7 = asarray(cat7)
katt8 = asarray(cat8)
katt9 = asarray(cat9)
katt10 = asarray(cat10)

print(f"Hund: {calculate_distance(hund6, hund2)}")
print(f"Hund: {calculate_distance(hund3, hund5)}")
print(f"Hund: {calculate_distance(hund1, hund9)}")
print(f"Hund: {calculate_distance(hund7, hund4)}")
print(f"Hund: {calculate_distance(hund10, hund8)}")

print("")
print(f"Katt: {calculate_distance2(katt3, katt5)}")
print(f"Katt: {calculate_distance2(katt4, katt1)}")
print(f"Katt: {calculate_distance2(katt2, katt8)}")
print(f"Katt: {calculate_distance2(katt7, katt10)}")
print(f"Katt: {calculate_distance2(katt9, katt6)}")

print("")
print(f"Katt med hund: {calculate_distance3(katt2, hund10)}")

katt_list.sort()
hund_list.sort()
print(f"Hundar: {hund_list}")
print(f"Katter: {katt_list}")
print(f"Medelvärde hund: {sum(hund_list) / 10} och katt: {sum(katt_list) / 10}")
# Skriv ut pixel-värde i pixel 0,0
# print(hund1[0, 0])
