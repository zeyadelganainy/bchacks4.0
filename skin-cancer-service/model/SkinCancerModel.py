import os
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression

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
    [
        current_directory / data_folder / (image_id + ".csv")
        for image_id in image_ids
    ],
    columns=[image_file_path],
)

cancer = metadata[cancer_column]
file_path_to_cancer_df = pd.concat(
    [image_file_paths, cancer],
    axis=1,
    join="inner"
)


class SkinCancerModel:
    model: LogisticRegression
    accuracy: float

    def __init__(self) -> None:
        # create the skin cancer machine-learning model
        self.model = LogisticRegression()
        # self.model.fit(x_train, y_train)

    def get_skin_cancer(self, image: str) -> SkinCancer:
        predicted_cancer_str: str = self.model.predict(image)
        predicted_cancer = SkinCancer(predicted_cancer_str)
        return predicted_cancer
