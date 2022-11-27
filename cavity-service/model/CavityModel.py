import os

import numpy as np
from numpy import asarray

import pickle
from PIL import Image
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score


classes = [i for i in range(2)]  # 0 class is no cavity, 1 class is for cavity
im_width = 32


def get_data(folder, im_width, label):
    files_array = os.listdir(folder)
    x = np.empty((len(files_array), im_width**2))
    y = np.empty((len(files_array), 1))

    for i in range(len(files_array)):
        path = folder / files_array[i]
        im = Image.open(path).convert("L")
        im = im.resize((im_width, im_width))
        im_array = asarray(im)
        x[i, :] = im_array.reshape(1, -1)
        y[i, 0] = classes[label]

    return x, y


def get_training_data():
    folder_training_0 = current_directory / "data" / "training" / "without_caries"
    folder_training_1 = current_directory / "data" / "training" / "caries"

    # training
    x_train_0 = np.empty((len(os.listdir(folder_training_0)), im_width**2))
    y_train_0 = np.empty((len(os.listdir(folder_training_0)), 1))
    x_train_1 = np.empty((len(os.listdir(folder_training_1)), im_width**2))
    y_train_1 = np.empty((len(os.listdir(folder_training_1)), 1))

    x_train_0, y_train_0 = get_data(folder_training_0, im_width, 0)
    x_train_1, y_train_1 = get_data(folder_training_1, im_width, 1)

    x_train = np.concatenate([x_train_0, x_train_1])
    y_train = np.concatenate([y_train_0, y_train_1])

    return [x_train, y_train]


def get_testing_data():
    folder_testing_0 = current_directory / "data" / "testing" / "without_caries"
    folder_testing_1 = current_directory / "data" / "testing" / "caries"

    # # # #testing
    x_test_0 = np.empty((len(os.listdir(folder_testing_0)), im_width**2))
    y_test_0 = np.empty((len(os.listdir(folder_testing_0)), 1))
    x_test_1 = np.empty((len(os.listdir(folder_testing_1)), im_width**2))
    y_test_1 = np.empty((len(os.listdir(folder_testing_1)), 1))

    x_test_0, y_test_0 = get_data(folder_testing_0, im_width, 0)
    x_test_1, y_test_1 = get_data(folder_testing_1, im_width, 1)

    x_test = np.concatenate([x_test_0, x_test_1])
    y_test = np.concatenate([y_test_0, y_test_1])

    return [x_test, y_test]


current_directory = Path(os.getcwd())
model_file_path = current_directory / "model" / "model.pickle"


class CavityModel:
    model: LogisticRegression
    accuracy: float

    def __init__(self) -> None:
        # create the skin cancer machine-learning model
        model: LogisticRegression
        accuracy: float
        try:
            with open(str(model_file_path), "rb") as f:
                [model, accuracy] = pickle.load(f)

        except (FileExistsError, FileNotFoundError):
            [x_train, y_train] = get_training_data()
            [x_test, y_test] = get_testing_data()

            model = LogisticRegression()
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(confusion_matrix(y_test, y_pred))

            with open(model_file_path, "wb") as f:
                pickle.dump([model, accuracy], f)

        self.model = model
        self.accuracy = accuracy

    def get_is_cavity(self, image: Image):
        im = image.resize((im_width, im_width))
        image_arr = asarray(im)
        is_cavity: int = self.model.predict(image_arr)
        is_cavity_str = "yes" if is_cavity else "no"
        return is_cavity_str
