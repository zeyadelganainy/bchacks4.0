import os
from pathlib import Path
import numpy as np
from numpy import asarray
import pandas as pd
import pickle as pkl
from PIL import Image

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from ImageClassificationModel import ImageClassificationModel

from SkinCancer import SkinCancer
from dermatologist.model import DATA_DIR, IMAGE_WIDTH, MODEL_FILEPATH

metadata_filename = "HAM10000_metadata.csv"
metadata_file_path = DATA_DIR / metadata_filename

cancer_column = "dx"
image_id_column = "image_id"
image_file_path = "image_file_path"

class_dict = {
    "akiec": 0,
    "bcc": 1,
    "bkl": 2,
    "df": 3,
    "mel": 4,
    "nv": 5,
    "vasc": 6,
}


def get_data(df, dict):

    x = np.empty((len(df), IMAGE_WIDTH**2))
    y = np.empty((len(df), 1))

    for i in df.index:
        path = df[image_file_path][i]
        im = Image.open(path).convert("L")
        im = im.resize((IMAGE_WIDTH, IMAGE_WIDTH))
        im_array = asarray(im)
        x[i, :] = im_array.reshape(1, -1)
        y[i, 0] = dict[df[cancer_column][i]]

    return x, y


def get_training_testing_data():
    metadata = pd.read_csv(metadata_file_path)
    image_ids = metadata[image_id_column]
    image_file_paths = pd.DataFrame(
        [
            DATA_DIR / (image_id + ".jpg")
            for image_id in image_ids
        ],
        columns=[image_file_path],
    )

    cancer = metadata[cancer_column]
    file_path_to_cancer_df = pd.concat(
        [image_file_paths, cancer], axis=1, join="inner"
    )
    x, y = get_data(file_path_to_cancer_df, IMAGE_WIDTH, class_dict)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    return [x_train, x_test, y_train, y_test]


class Dermatologist(ImageClassificationModel):
    def __init__(self, new_model) -> None:
        if new_model:
            [x_train, x_test, y_train, y_test] = get_training_testing_data()
            model = LogisticRegression()
            model.fit(x_train, y_train)

            y_pred = model.predict(x_test)
            accuracy = accuracy_score(y_test, y_pred)

            with open(MODEL_FILEPATH, "wb") as f:
                pkl.dump([model, accuracy], f)
        else:
            with open(MODEL_FILEPATH, "rb") as f:
                [model, accuracy] = pkl.load(f)

        super().__init__(
            model=model,
            accuracy=accuracy,
            image_width=IMAGE_WIDTH,
            image_height=IMAGE_WIDTH,
        )

    def get_skin_cancer(self, image: Image) -> str:
        predicted_cancer_str: str = self.classify_image(image)
        predicted_cancer = SkinCancer(predicted_cancer_str)
        return predicted_cancer.name
