import os
from pathlib import Path
import numpy as np
import pandas as pd
import pickle as pkl
from PIL import Image

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from ImageClassificationModel import ImageClassificationModel
from optometrist.model import MODEL_FILEPATH, IMAGE_WIDTH


def get_training_testing_data():
    pass


class Optometrist(ImageClassificationModel):
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

    def get_eye_disease(self, image: Image) -> str:
        eye_disease: str = self.classify_image(image)
        return eye_disease
