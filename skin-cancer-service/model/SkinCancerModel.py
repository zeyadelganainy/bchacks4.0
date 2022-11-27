import os
from pathlib import Path
import numpy as np
from numpy import asarray

import pandas as pd
import pickle
from PIL import Image

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

from SkinCancer import SkinCancer

current_directory = Path(os.getcwd())
data_folder = "data"
metadata_filename = "HAM10000_metadata.csv"
metadata_file_path = current_directory / data_folder / metadata_filename

metadata = pd.read_csv(metadata_file_path)

cancer_column = "dx"
image_id_column = "image_id"
image_file_path = "image_file_path"

image_ids = metadata[image_id_column]
image_file_paths = pd.DataFrame(
    [current_directory / data_folder / (image_id + ".jpg") for image_id in image_ids],
    columns=[image_file_path],
)

cancer = metadata[cancer_column]
file_path_to_cancer_df = pd.concat([image_file_paths, cancer], axis=1, join="inner")

classes = [i for i in range(7)]
im_width = 32

class_dict = {"akiec": 0, "bcc": 1, "bkl": 2, "df": 3, "mel": 4, "nv": 5, "vasc": 6}


def get_data(df, im_width, dict):

    x = np.empty((len(df), im_width**2))
    y = np.empty((len(df), 1))

    for i in df.index:
        path = df[image_file_path][i]
        im = Image.open(path).convert("L")
        im = im.resize((im_width, im_width))
        im_array = asarray(im)
        x[i, :] = im_array.reshape(1, -1)
        y[i,0] = dict[df[cancer_column][i]]

    return x, y


x, y = get_data(file_path_to_cancer_df, im_width, class_dict)
# train_samples = 9015

def get_training_testing_data():
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    return [x_train, x_test, y_train, y_test]



current_directory = Path(os.getcwd())
model_file_path = current_directory / "model.pickle"


class SkinCancerModel:
    model: LogisticRegression
    accuracy: float

    def __init__(self) -> None:
        # create the skin cancer machine-learning model
        model: LogisticRegression
        accuracy: float
        try:
            with open(model_file_path, "rb") as f:
                [model, accuracy] = pickle.load(f)

        except (FileExistsError, FileNotFoundError):
            [x_train, x_test, y_train, y_test] = get_training_testing_data()
            model = LogisticRegression()
            model.fit(x_train, y_train)

            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(confusion_matrix(y_test, y_pred))

            with open(model_file_path, "wb") as f:
                pickle.dump([model, accuracy], f)

        self.model = model
        self.accuracy = accuracy

    def get_skin_cancer(self, image: str) -> str:
        predicted_cancer_str: str = self.model.predict(image)
        predicted_cancer = SkinCancer(predicted_cancer_str)
        return predicted_cancer.name
