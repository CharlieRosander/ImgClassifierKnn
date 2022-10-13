from PIL import Image
from numpy import asarray
import matplotlib.pyplot as plt

# Öppna bilden i en variabel
img = Image.open('dog.8.jpg')

# Gör bilden svart-vit
img = img.convert("L")

# Ändra bildens storlek till 30x30
img = img.resize((30, 30))

# Visa bilden
# img.show()

# Gör om bilden till en NuMPy matris
numpydata = asarray(img)

plt.imshow(img)

# euklides = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

# Skriv ut pixel-värde i pixel 0,0
print(numpydata)
plt.show()
