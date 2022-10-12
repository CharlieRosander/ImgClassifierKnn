from PIL import Image
from numpy import asarray

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


# Skriv ut pixel-värde i pixel 0,0
print(numpydata[0, 0])

