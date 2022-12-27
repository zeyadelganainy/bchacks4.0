import os

import numpy as np
from numpy import asarray

import pickle as pkl
from PIL import Image

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from ImageClassificationModel import ImageClassificationModel
from dentist.model import DATA_DIR, IMAGE_WIDTH, MODEL_FILEPATH
from dentist.model.Cavity import Cavity


def get_data(folder, IMAGE_WIDTH, label):
    files_array = os.listdir(folder)
    x = np.empty((len(files_array), IMAGE_WIDTH**2))
    y = np.empty((len(files_array), 1))

    for i in range(len(files_array)):
        path = folder / files_array[i]
        im = Image.open(path).convert("L")
        im = im.resize((IMAGE_WIDTH, IMAGE_WIDTH))
        im_array = asarray(im)
        x[i, :] = im_array.reshape(1, -1)
        y[i, 0] = label

    return x, y


def get_training_data():
    folder_training_0 = DATA_DIR / "training" / "no_cavities"
    folder_training_1 = DATA_DIR / "training" / "cavities"

    # training
    x_train_0 = np.empty((len(os.listdir(folder_training_0)), IMAGE_WIDTH**2))
    y_train_0 = np.empty((len(os.listdir(folder_training_0)), 1))
    x_train_1 = np.empty((len(os.listdir(folder_training_1)), IMAGE_WIDTH**2))
    y_train_1 = np.empty((len(os.listdir(folder_training_1)), 1))

    x_train_0, y_train_0 = get_data(folder_training_0, IMAGE_WIDTH, 0)
    x_train_1, y_train_1 = get_data(folder_training_1, IMAGE_WIDTH, 1)

    x_train = np.concatenate([x_train_0, x_train_1])
    y_train = np.concatenate([y_train_0, y_train_1])

    return [x_train, y_train]


def get_testing_data():
    folder_testing_0 = DATA_DIR / "testing" / "no_cavities"
    folder_testing_1 = DATA_DIR / "testing" / "cavities"

    # # # #testing
    x_test_0 = np.empty((len(os.listdir(folder_testing_0)), IMAGE_WIDTH**2))
    y_test_0 = np.empty((len(os.listdir(folder_testing_0)), 1))
    x_test_1 = np.empty((len(os.listdir(folder_testing_1)), IMAGE_WIDTH**2))
    y_test_1 = np.empty((len(os.listdir(folder_testing_1)), 1))

    x_test_0, y_test_0 = get_data(folder_testing_0, IMAGE_WIDTH, 0)
    x_test_1, y_test_1 = get_data(folder_testing_1, IMAGE_WIDTH, 1)

    x_test = np.concatenate([x_test_0, x_test_1])
    y_test = np.concatenate([y_test_0, y_test_1])

    return [x_test, y_test]


class Dentist(ImageClassificationModel):
    def __init__(self, new_model: bool) -> None:
        if new_model:
            [x_train, y_train] = get_training_data()
            [x_test, y_test] = get_testing_data()

            model = LogisticRegression()
            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)

            with open(MODEL_FILEPATH, "wb") as f:
                pkl.dump([model, accuracy], f)
        else:
            with open(str(MODEL_FILEPATH), "rb") as f:
                [model, accuracy] = pkl.load(f)

        super().__init__(
            model=model,
            accuracy=accuracy,
            image_width=IMAGE_WIDTH,
            image_height=IMAGE_WIDTH,
        )

    def is_cavity(self, image: Image):
        is_cavity: int = self.classify_image(image)
        cavity: Cavity = Cavity(is_cavity)
        return cavity.name
