from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt

# Öppna bilden i en variabel
hund1 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund/dog.1.jpg")
hund2 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund/dog.2.jpg")
katt1 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt/cat.1.jpg")
katt2 = Image.open("C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt/cat.2.jpg")

# Gör bilden svart-vit
hund1 = hund1.convert("L")
hund2 = hund2.convert("L")
katt1 = katt1.convert("L")
katt2 = katt2.convert("L")

# Ändra bildens storlek till 30x30
hund1 = hund1.resize((30, 30))
hund1 = hund1.resize((30, 30))
katt1 = katt1.resize((30, 30))
katt2 = katt2.resize((30, 30))

# Gör om bilden till en NuMPy matris
hund_data1 = asarray(hund1)
hund_data2 = asarray(hund2)
katt_data1 = asarray(katt1)
katt_data2 = asarray(katt2)

hund_sum1 = hund_data1.sum() / 100
hund_sum2 = hund_data2.sum() / 100
katt_sum1 = katt_data1.sum() / 100
katt_sum2 = katt_data2.sum() / 100

# plt.imshow(img)

# Graf
x1 = hund_sum1
x2 = hund_sum2
x3 = katt_sum1
x4 = katt_sum2
x = [hund_sum1, hund_sum2, katt_sum1, katt_sum2]

y = []


y1 = 0
y2 = 1
# plt.scatter(x, y, label="dots", color="k", marker="o", s=25)

# x-axis label
plt.xlabel('x - axis')
# frequency label
plt.ylabel('y - axis')
# plot title
plt.title('My scatter plot!')
# showing legend
plt.legend()

print(hund_sum1)
print(hund_sum2)
print(katt_sum1)
print(katt_sum2)
# function to show the plot
plt.show()

# Skriv ut pixel-värde i pixel 0,0

# plt.show()
