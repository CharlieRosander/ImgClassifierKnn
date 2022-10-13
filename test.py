from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import math
import glob
import

images = [cv2.imread(file) for file in glob.glob("path/to/files/*.png")]

def calculate_distance(i1, i2):
    return np.sum((i1 - i2) ** 2)


# Öppna bilden i en variabel
img = Image.open('images/dog.8.jpg')
img1 = Image.open("images/dog.2.jpg")

# Gör bilden svart-vit
img = img.convert("L")
img1 = img1.convert("L")

# Ändra bildens storlek till 30x30
img = img.resize((5, 5))
img1 = img1.resize((5, 5))

# Gör om bilden till en NuMPy matris
numpy_data1 = np.asarray(img)
numpy_data2 = np.asarray(img1)

numpy_data1 = numpy_data1.flatten()
numpy_data2 = numpy_data2.flatten()


print(calculate_distance(numpy_data1, numpy_data2))

# Skriv ut pixel-värde i pixel 0,0
# print(numpy_data[0, 0])
