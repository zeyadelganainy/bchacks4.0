import os
import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from PIL import Image
from sklearn.metrics import confusion_matrix, accuracy_score
from pathlib import Path

# current_dir = Path(os.getcwd())
# current_str = str(current_dir)
# print("Current: " + current_str)
lab = preprocessing.LabelEncoder()
folder_training_0 = "data/teeth_dataset/training/without_caries/"
folder_training_1 = "data/teeth_dataset/training/caries/"
folder_testing_0 = "data/teeth_dataset/testing/without_caries/" 
folder_testing_1 = "data/teeth_dataset/testing/caries/"

# ../data/teeth_dataset/training/
# folder_training_cav = '../data/teeth_dataset/training/caries'
# folder_training_no_cav = '../data/teeth_dataset/training/without_caries'
# folder_testing_cav = '../data/teeth_dataset/testing/caries'
# folder_testing_no_cav = '../data/teeth_dataset/testing/without_caries'

classes = [i for i in range(2)] # 0 class is no cavity, 1 class is for cavity
# print(classes)
im_width = 32

def get_data(folder, im_width, label):
    files_array = os.listdir(folder)
    x = np.empty((len(files_array), im_width**2))
    y = np.empty((len(files_array), 1))
    
    for i in range(len(files_array)):
        path = folder + files_array[i]
        im = Image.open(path).convert('L')
        im = im.resize((im_width, im_width))
        im_array = asarray(im)
        x[i,:] = im_array.reshape(1,-1)
        y[i,0] = classes[label]
            
    return x, y

#training
x_train_0 = np.empty((len(os.listdir(folder_training_0)), im_width**2))
y_train_0 = np.empty((len(os.listdir(folder_training_0)), 1))
x_train_1 = np.empty((len(os.listdir(folder_training_1)), im_width**2))
y_train_1 = np.empty((len(os.listdir(folder_training_1)), 1))


x_train_0, y_train_0 = get_data(folder_training_0, im_width,0)
x_train_1, y_train_1 = get_data(folder_training_1, im_width,1)

x_train = np.concatenate([x_train_0, x_train_1])
y_train = np.concatenate([y_train_0, y_train_1])



model = LogisticRegression()
model.fit(x_train, y_train)

# # # #testing
x_test_0 = np.empty((len(os.listdir(folder_testing_0)), im_width**2))
y_test_0 = np.empty((len(os.listdir(folder_testing_0)), 1))
x_test_1 = np.empty((len(os.listdir(folder_testing_1)), im_width**2))
y_test_1 = np.empty((len(os.listdir(folder_testing_1)), 1))


x_test_0, y_test_0 = get_data(folder_testing_0, im_width,0)
x_test_1, y_test_1 = get_data(folder_testing_1, im_width,1)

x_test = np.concatenate([x_test_0, x_test_1])
y_test = np.concatenate([y_test_0, y_test_1])



y_pred = model.predict(x_test)
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
