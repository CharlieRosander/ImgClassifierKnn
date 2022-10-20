from PIL import Image
import numpy as np
import pandas as pd
import os
import copy
from collections import Counter
from math import sqrt

imageDirectory = r"C:\Users\Magnus\Desktop\grupp\data\train100"

"""
We are creating an empyt list and then using os. to access the folder with our original/unpreocessed images.
Every image is opened with PIL Image and then converted into gray scale with 'L' and then rezised into 30*30 resolution. 
Then we convert the image into a numpy array and append those images to our imageArrList.
We convert this list into an array as well and name it X_train since that is customary in ML.
"""
imageArrList = []
for file in os.listdir(imageDirectory):
    f = os.path.join(imageDirectory, file)
    img = Image.open(f)
    img = img.convert("L")
    img = img.resize((30, 30))
    ImageArr = np.array(img)
    imageArrList.append(ImageArr)

X_train = np.array(imageArrList)

# testDirectory = r"C:\Users\Magnus\Desktop\grupp\test1"
testDirectory = r"C:\Users\Magnus\Desktop\grupp\data\test50"  # the path to my test images
"""
We do the same for our testing images.
"""

imageArrList = []
for file in os.listdir(testDirectory):
    f = os.path.join(testDirectory, file)
    img = Image.open(f)
    img = img.convert("L")
    img = img.resize((30, 30))
    ImageArr = np.array(img)
    # ImageArr = ImageArr / 255 # This might improve the results
    imageArrList.append(ImageArr)

X_test = np.array(imageArrList)

"""
We create a folder where we append append the dog or cat name of the pictures. we later use this folder as an index lookup.
(this can be done in the first processing step).

We define the k-value by using the rule of thum of where you take the square of the number of training samples. 
then we make sure that k is not even.
"""

categories = [i for i in os.listdir(imageDirectory)]
labelText = ['dog' if imageName[:3] == 'dog' else 'cat' for imageName in categories]

k = int(sqrt(len(labelText)))

if k % 2 == 0:
    k += 1

print(F'{k=}')

# Dont think these will be used not used ?
testImagesFileNames = [i for i in os.listdir(testDirectory)]
testLabel = ['dog' if imageName[:3] == 'dog' else 'cat' for imageName in testImagesFileNames]

"""
We define the dists function which has the parameter X which is our processed training test images (X_test).
dists calculates the L2 Euclidean distance.

we need a L2 value for each test picture for each training picture.

we get these valus by lots of looping...

So if we have 3 test images and 5 train images then we need to calculate and L2 value between all the images (i.e. 3x5)
matrixAbsDifference = np.absolute(X[ix]-X_train[idx]) does the actual L2 calculation which is then appened to our distList.

To keep track of which l2 values belong to which picture we put each X_test values l2 in a sublist in the distListList. 
The distList gets reset/emptied once we start calculating a new test image.
We make a deewp copy of the distListList since we later sort the sublists and need the order in order for using the index of the L2 values to find if the value belongs to a cat or dag
(not an effective or good way to do this)

"""


def dists(X):
    distList = []
    distListList = []

    for ix in range(len(X)):
        for idx in range(len(X_train)):
            matrixAbsDifference = np.absolute(X[ix] - X_train[idx])
            l2 = np.sum(matrixAbsDifference)
            distList.append(l2)
            # distIndex.append(int(l2))
            if len(distList) == len(X_train):
                distListList.append(distList)
                distList = []
    global unsortedDistList
    unsortedDistList = copy.deepcopy(distListList)
    return distListList


"""
we call the dist function on our test images and save it to the distList varible.
"""
distList = dists(X_test)
# print(F'{distList=}')
# print(F'{distIndex=}')


"""
We loop through our sublists that contain each l2 value. We sort the list so that we know which is the lowest (i.e. nearest)
we make another deep copy so that we can use the index later (i might have been copying the same list twise...)
We slice off the k-amount value from the sorted sublist. i.e. if k = 5 then we only select the 5 lowest numbers.
Then we append these slices to our y_pred list.

"""


def select_nearest_k(distsList, k=k):
    # global idxList
    # idxList = []
    y_pred = []
    idxList = copy.deepcopy(distList)
    for i in range(len(distsList)):
        distList[i].sort()
        nearestL2 = distList[i][0:k]
        # picPrediction = min(nearestL2)
        # y_pred.append(picPrediction)
        y_pred.append(nearestL2)

    return y_pred


"""
We run call the select_the_nearest_k function on our distList and save it into our myPrediction 

"""
k_nearest_l2_values = select_nearest_k(distList, k=k)
# print(myPredictions)


"""
def mapPredictions(predictions):
    testList = []
    found = False
    global counter
    counter = 0
    global countList
    countList = []
    global countListList
    for ix, i in enumerate(predictions):
        #print(F'{i=}')
        for subList in (unsortedDistList[ix]):
            #print(F'{subList=}')

            if subList == i:
                #print('Found')
                found = True
                countList.append(counter)
                counter = 0
                #print(F'{countList}')
                break
            counter += 1
        found = False

    return countList
"""

"""
In the mapPredictions function we map the l2 values to their respective image index so that we can label our predictions
(if we have labales which wont be aveleble on in practise)

we loop through the k-sorted sublists.
For each value we look up that value in the unsortedDistList with index()
That index value we append to another list which we intend to use to get the final label.
"""


def mapPredictions(predictions):
    countList = []
    countListList = []
    for ix, subList in enumerate(predictions):
        print(subList)
        for l2 in subList:
            l2_idx = unsortedDistList[ix].index(l2)
            countList.append(l2_idx)
        countListList.append(countList)
        countList = []

    return countListList


"""
we call the map predictions function and save it in indexValuesForPics
"""
indexValuesForPics = mapPredictions(k_nearest_l2_values)

"""
The convert_l2_values_to_label function now uses the index values for the k-nearest images and appends the results (cat or dog) to another list.
Again to make sure we get subfolders for each test image we append the list to another list once we reach the k-value amount.

"""


def convert_l2_values_to_label(ImageIndex):
    predictionLabel = []
    predictionLabelLabel = []
    for k_value in ImageIndex:
        for i in k_value:
            l2idx = labelText[i]
            predictionLabel.append(l2idx)
            if len(predictionLabel) == k:
                predictionLabelLabel.append(predictionLabel)
                predictionLabel = []

    return predictionLabelLabel


"""
we run the convert_l2_values_to_label function so that all the sublists with sorted l2 values get converted assigned a label
"""
k_values_labels = convert_l2_values_to_label(indexValuesForPics)

"""
we now use the nearest k to make the acutal predictions. 
This is done by counting the labels and selecting the lable which have the most counts.
We use the collections Counter class for this. Then append these predictions into yet another list (very ineffective)

"""


def find_k_majority(nearestL2):
    final_predictions = []
    for i in nearestL2:
        c = Counter(i)
        majority = c.most_common()[0][0]
        final_predictions.append(majority)

    return final_predictions


"""
And we run call this function
"""
finalPredictions = find_k_majority(k_values_labels)

"""
We create a right and wrong counter varibles. 
Then we loop through both the finalPredictions and the labelTest list to see if we got the prediction correct.

"""
right = 0
wrong = 0

for i, j in zip(finalPredictions, testLabel):
    print(i, j)
    if i == j:
        right += 1
    elif i != j:
        wrong += 1

"""
Printing the accuracy i.e. correct predictions compared to wrong ones.
"""
print(F'{right}')
print(F'{wrong}')
print(right / (right + wrong))
accuracy = right / (right + wrong)
print(F'{accuracy}')
percentage = "{:.0%}".format(accuracy)
percentage
