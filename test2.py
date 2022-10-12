import math
from PIL import Image
from numpy import asarray

# x1 = 10
# x2 = 20
# y1 = 15
# y2 = 5
# euklides = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
#
# print(euklides)

# Öppna bilden i en variabel
img = Image.open('dog.1.jpg')
img1 = Image.open("dog.2.jpg")

# Gör bilden svart-vit
img = img.convert("L")
img1 = img1.convert("L")
# Ändra bildens storlek till 30x30
img = img.resize((30, 30))
img1 = img1.resize((30, 30))

# Visa bilden
# img.show()
# img1.show()

# Gör om bilden till en NuMPy matris
hund1 = asarray(img)
hund2 = asarray(img1)
# Skriv ut pixel-värde i pixel 0,0
print(hund1[0, 0])
print(hund2[0, 0])

euklides = math.sqrt(math.pow(hund1[0, 0], 2) + math.pow(hund2[0, 0], 2))
print(euklides)
