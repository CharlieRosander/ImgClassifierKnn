from PIL import Image
from numpy import asarray
import math
import os


# En klass för att öppna, konvertera och lagra alla bilder
class SkapaDjur:
    hund_pixel_sum = []
    hund_dir = "images/hund"
    katt_pixel_sum = []
    katt_dir = "images/katt"
    test_pixel_sum = []

    # HUNDAR
    # Öppnar och konverterar hundbilderna, samt summerar varje bilds totala pixelvärde
    # och lägger det i en ny lista tillsammans med en etikett
    # för att senare kunna komma åt etiketten när röstningen ska genomföras
    @classmethod
    def läs_in_hund(cls):
        hund_counter = 0
        for filename in os.listdir(SkapaDjur.hund_dir):
            f = os.path.join(SkapaDjur.hund_dir, filename)
            if os.path.isfile(f):
                img = Image.open(f)
                img = img.convert("L")
                img = img.resize((70, 70))
                hund_data = asarray(img)
                hund_data_sum = hund_data.sum()
                SkapaDjur.hund_pixel_sum.append([f"Hund {hund_counter}", hund_data_sum])
                hund_counter += 1

        return SkapaDjur.hund_pixel_sum

    # KATTER
    # Öppnar och konverterar kattbilderna, samt summerar varje bilds totala pixelvärde
    # och lägger det i en ny lista tillsammans med en etikett
    # för att senare kunna komma åt etiketten när röstningen ska genomföras
    @classmethod
    def läs_in_katt(cls):
        katt_counter = 0
        for filename in os.listdir(SkapaDjur.katt_dir):
            f = os.path.join(SkapaDjur.katt_dir, filename)
            if os.path.isfile(f):
                img = Image.open(f)
                img = img.convert("L")
                img = img.resize((70, 70))
                katt_data = asarray(img)
                katt_data_sum = katt_data.sum()
                SkapaDjur.katt_pixel_sum.append([f"Katt {katt_counter}", katt_data_sum])
                katt_counter += 1

        return SkapaDjur.katt_pixel_sum

    # TEST
    # Öppnar och konverterar testbilden, samt summerar bildens totala pixelvärde
    # och lägger det i en ny lista.
    @classmethod
    def läs_in_test(cls):
        test_img1 = Image.open("images/test/17.jpg")
        test_img1 = test_img1.convert("L")
        test_img1 = test_img1.resize((70, 70))
        test1_data = asarray(test_img1)
        test1_data_sum = test1_data.sum()
        SkapaDjur.test_pixel_sum.append(test1_data_sum)

        return SkapaDjur.test_pixel_sum


# En klass för att hantera Knn
# här är knn_result listan som distanserna samt etiketterna finns från dom andra funktionerna
class Knn:
    knn_result = []

    # Den här funktionen hanterar räkningen och röstningen för att avgöra om det är en hund eller katt.
    # Här sätts också k-värdet som avgör hur många röster som ska räknas.
    # Vi använder en speciell funktion "lambda"
    # som används för att sortera knn_result i storleksordning baserat på värdet i index[1]
    @classmethod
    def vote(cls):
        hund_count = 0
        katt_count = 0
        k_värde = 5
        Knn.knn_result.sort(key=lambda x: x[1])

        print("Dom kortaste distanserna är:")
        for value in Knn.knn_result[0:k_värde]:
            print(value)
            for label in value:
                if "Hund" in label:
                    hund_count += 1
                if "Katt" in label:
                    katt_count += 1
                break
        if hund_count > katt_count:
            print("Bilden är en hund")
        else:
            print("Bilden är en katt")


# Funktion för att gå skicka varje bilds pixelvärde från listan "hund_pixel_sum" till euklides formel
# och sedan lägga till resultatet i "knn_result".
# "hund_pixel_sum" ser ut såhär: [['Hund 0', 279889]...] så här används indexering för att komma åt namn/värde
def hund_mot_test(x1, x2):
    index = 0
    while index < len(SkapaDjur.hund_pixel_sum):
        x1 = SkapaDjur.hund_pixel_sum[index][1]
        x2 = SkapaDjur.test_pixel_sum[0]
        Knn.knn_result.append([f"Hund {index}", euklides_formel(x1, x2)])
        index += 1


# Funktion för att gå skicka varje bilds pixelvärde från listan "katt_pixel_sum" till euklides formel
# och sedan lägga till resultatet i "knn_result".
# "katt_pixel_sum" ser ut såhär: [['Katt 0', 279889]...] så här används indexering för att komma åt namn/värde
def katt_mot_test(x1, x2):
    index = 0
    while index < len(SkapaDjur.katt_pixel_sum):
        x1 = SkapaDjur.katt_pixel_sum[index][1]
        x2 = SkapaDjur.test_pixel_sum[0]
        Knn.knn_result.append([f"Katt {index}", euklides_formel(x1, x2)])

        index += 1


# Euklides distans formel, för att räkna ut distansen mellan summeringen av alla pixlar i varje bild
def euklides_formel(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)


# Här kallar vi på alla klasser/funktioner
SkapaDjur.läs_in_hund()
SkapaDjur.läs_in_katt()
SkapaDjur.läs_in_test()
hund_mot_test(SkapaDjur.hund_pixel_sum, SkapaDjur.test_pixel_sum)
katt_mot_test(SkapaDjur.katt_pixel_sum, SkapaDjur.test_pixel_sum)
Knn.vote()
