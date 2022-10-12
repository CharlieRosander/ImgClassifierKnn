from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt

# Öppna bilden i en variabel
img = Image.open('dog.8.jpg')
img1 = Image.open("cat.2.jpg")
img2 = Image.open("cat.4.jpg")

# Gör bilden svart-vit
img = img.convert("L")
img1 = img1.convert("L")
img2 = img2.convert("L")

# Ändra bildens storlek till 30x30
img = img.resize((30, 30))
# img1 = img1.resize((30, 30))
# img2 = img2.resize((30, 30))

# Visa bilden
# img.show()
# img1.show()

# Gör om bilden till en NuMPy matris
numpy_data = asarray(img)
# numpy_data = numpy_data.reshape(18, 50)
print(numpy_data.size)

numpy_data1 = asarray(img1)
print(numpy_data1.size)

numpy_data2 = asarray(img2)
print(numpy_data2.size)

# Skriv ut pixel-värde i pixel 0,0
# print(numpy_data[0, 0])
print(numpy_data)
# print(numpy_data1[0, 30])
# print(numpy_data2[0, 30])
# print(numpy_data.sum())
# print(numpy_data1.sum())
# print(numpy_data2.sum())