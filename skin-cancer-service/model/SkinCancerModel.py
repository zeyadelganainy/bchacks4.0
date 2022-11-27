import os
from pathlib import Path

from numpy import asarray
import pandas as pd
import pickle

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

from PIL import Image

from SkinCancer import SkinCancer

current_directory = Path(os.getcwd())
data_folder = "data"
metadata_filename = "HAM10000_metadata.csv"
metadata_file_path = current_directory / data_folder / metadata_filename

im_width = 32

metadata = pd.read_csv(metadata_file_path)

cancer_column = "dx"
image_id_column = "image_id"
image_file_path = "image_file_path"

image_ids = metadata[image_id_column]
image_file_paths = pd.DataFrame(
    [
        current_directory / data_folder / (image_id + ".csv") 
        for image_id in image_ids
    ],
    columns=[image_file_path],
)

cancer = metadata[cancer_column]
file_path_to_cancer_df = pd.concat([image_file_paths, cancer], axis=1, join="inner")


def get_training_data():
    pass


def get_testing_data():
    pass


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
            [x_train, y_train] = get_training_data()
            [x_test, y_test] = get_testing_data()

            model.fit(x_train, y_train)
            y_pred = self.model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)
            print(confusion_matrix(y_test, y_pred))

            with open(model_file_path, "wb") as f:
                pickle.dump([model, accuracy], f)

        self.model = model
        self.accuracy = accuracy

    def get_skin_cancer(self, image: Image) -> str:
        im = image.resize((im_width, im_width))
        image_arr = asarray(im)
        predicted_cancer_str: str = self.model.predict(image_arr)
        predicted_cancer = SkinCancer(predicted_cancer_str)
        return predicted_cancer.name
