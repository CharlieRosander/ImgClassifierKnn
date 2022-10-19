from PIL import Image
from numpy import asarray
import math
import os


class Knn:
    knn_result = []

    k_värde = 11

    # for l2_value in label_and_l2_value:
    #     for value in knn_list[0:k_värde]:
    #         if value == l2_value[1]:
    #             min_distance_and_label.append(l2_value)
    #             break
    @classmethod
    def get_result(cls):
        return Knn.knn_result

    # @classmethod
    # def set_result(cls):
    #     index = 0
    #     while index < len(SkapaDjur.hund_pixel_sum):
    #         x1 = SkapaDjur.hund_pixel_sum[index]
    #         x2 = SkapaDjur.test_pixel_sum[0]
    #         index += 1
    #         Knn.knn_result.append(euklides_formel(x1, x2))
    #     return Knn.knn_result


class SkapaDjur:
    hund_pixel_sum = []
    hund_dir = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/hund"
    katt_pixel_sum = []
    katt_dir = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/katt"
    test_pixel_sum = []
    test_dir = "C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test/4.jpg"

    @classmethod
    def läs_in_hund(cls):
        # HUNDAR
        # Öppnar och konverterar hundbilderna
        name_counter = 0
        for filename in os.listdir(SkapaDjur.hund_dir):
            f = os.path.join(SkapaDjur.hund_dir, filename)
            if os.path.isfile(f):
                img = Image.open(f)
                img = img.convert("L")
                img = img.resize((50, 50))
                hund_data = asarray(img)
                hund_data_sum = hund_data.sum()
                SkapaDjur.hund_pixel_sum.append([f"Hund {name_counter}", hund_data_sum])
                name_counter += 1
        return SkapaDjur.hund_pixel_sum

    @classmethod
    def läs_in_katt(cls):
        # KATTER
        # Öppnar och konverterar kattbilderna
        for filename in os.listdir(SkapaDjur.katt_dir):
            f = os.path.join(SkapaDjur.katt_dir, filename)
            if os.path.isfile(f):
                img = Image.open(f)
                img = img.convert("L")
                img = img.resize((50, 50))
                katt_data = asarray(img)
                katt_data_sum = katt_data.sum()
                SkapaDjur.katt_pixel_sum.append(katt_data_sum)
        return SkapaDjur.katt_pixel_sum

    @classmethod
    def läs_in_test(cls):
        # Öppnar test bilden,
        test_img1 = Image.open("C:/Users/charl/PycharmProjects/GruppArbete-AIprojekt/images/test/4.jpg")
        test_img1 = test_img1.convert("L")
        test_img1 = test_img1.resize((50, 50))
        test1_data = asarray(test_img1)
        test1_data_sum = test1_data.sum()
        SkapaDjur.test_pixel_sum.append(test1_data_sum)

        return SkapaDjur.test_pixel_sum


def euklides_formel(i1, i2):
    return math.sqrt((float(i1) - float(i2)) ** 2)


def hund_mot_test(x1, x2):
    index = 0
    while index < len(SkapaDjur.hund_pixel_sum):
        x1 = SkapaDjur.hund_pixel_sum[index]
        x2 = SkapaDjur.test_pixel_sum[0]
        index += 1
        # label_and_l2_value.append([f"Hund {index}", euklides_formel(x1, x2)])
        Knn.knn_result.append(euklides_formel(x1, x2))


# Går igenom katt värdena och skickar det till uträknaren och lägger sedan till det värdet i distance_list_katt
def katt_mot_test(train, test):
    index = 0
    while index < len(SkapaDjur.katt_pixel_sum):
        x1 = SkapaDjur.katt_pixel_sum[index]
        x2 = SkapaDjur.test_pixel_sum[0]
        index += 1
        # label_and_l2_value.append([f"Katt {index}", euklides_formel(x1, x2)])
        Knn.knn_result.append(euklides_formel(x1, x2))


hund_mot_test(SkapaDjur.läs_in_hund(), SkapaDjur.läs_in_test())
katt_mot_test(SkapaDjur.läs_in_katt(), SkapaDjur.läs_in_test())


# DEBUGGING/TESTING
# print(SkapaDjur.läs_in_hund())
# print(SkapaDjur.läs_in_katt())
# print(SkapaDjur.läs_in_test())
print(SkapaDjur.hund_pixel_sum)
# print(Knn.set_result())
print(Knn.knn_result)