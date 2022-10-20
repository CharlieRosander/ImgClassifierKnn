from PIL import Image
from numpy import asarray
import numpy
import math
import os
import numpy as np

HUND_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/hund"
KATT_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/katt"
TEST_DIR = "C:/Users/Kaliber/Desktop/AI-Developer-Jensen/PythonProjects/ImgClassifierKnn/images/test"

distans_katter = []
distans_hundar = []
test = []
katter = []
hundar = []


class Djur:

    def __init__(self, directory):
        self.directory = directory
        self.train = katter
        self.distans = distans_katter
        self.train1 = hundar
        self.distans1 = distans_hundar

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                img = Image.open(f)
                img = img.convert("L")
                img = img.resize((50, 50))
                data = asarray(img)
                data_sum = data.sum()
                if directory == KATT_DIR:
                    katter.append(data_sum)
                if directory == HUND_DIR:
                    hundar.append(data_sum)
                if directory == TEST_DIR:
                    test.append(data_sum)

    @classmethod
    def test_katt(cls, trainlista, testlista):
        index = 0
        while index < len(trainlista):
            x1 = trainlista[index]
            x2 = testlista[0]
            index += 1
            distans_katter.append(Djur.euklides_formel(x1, x2))

    @classmethod
    def test_hund(cls, trainlista, testlista):
        index = 0
        while index < len(trainlista):
            x1 = trainlista[index]
            x2 = testlista[0]
            index += 1
            distans_katter.append(Djur.euklides_formel(x1, x2))

    @classmethod
    def euklides_formel(cls, x1, x2):
        return math.sqrt((float(x1) - float(x2)) ** 2)

    @classmethod
    def knn(cls, kattsumma, hundsumma):

        knn_list = kattsumma + hundsumma
        k_värde = 0
        hund_count = 0
        katt_count = 0
        rank = 1

        while True:

            for i, x in enumerate(knn_list):
                if x == min(knn_list) and i <= 10:
                    print(f'Rank {rank} : Pixelavstånd {x} i bild nr {i} - KATT.')
                    k_värde += 1
                    rank += 1
                    katt_count += 1
                    del knn_list[i]

                if x == min(knn_list) and i >= 10:
                    print(f'Rank {rank} : Pixelavstånd {x} i bild nr {i} - HUND.')
                    k_värde += 1
                    rank += 1
                    hund_count += 1
                    del knn_list[i]

                if k_värde == 5:
                    break

            if k_värde == 5 and hund_count < katt_count:
                print("Att bilden föreställer en katt är bortom allt rimligt tvivel")
                break

            if k_värde == 5 and hund_count > katt_count:
                print("Att bilden föreställer en hund är bortom allt rimligt tvivel")
                break


a = Djur(KATT_DIR)
b = Djur(HUND_DIR)
c = Djur(TEST_DIR)
a.test_katt(katter, test)
b.test_hund(hundar, test)
Djur.knn(a.distans, b.distans1)
