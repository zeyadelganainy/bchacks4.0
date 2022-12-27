from typing import Union

from numpy import asarray
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network._multilayer_perceptron import MLPClassifier
from PIL import Image

ACCEPTABLE_MODEL_TYPES = Union[LogisticRegression, MLPClassifier]


class ImageClassificationModel:
    model: ACCEPTABLE_MODEL_TYPES
    accuracy: float
    image_width: int
    image_height: int

    def __init__(
        self,
        model: ACCEPTABLE_MODEL_TYPES,
        accuracy: float,
        image_width: int,
        image_height: int,
    ) -> None:
        self.model = model
        self.accuracy = accuracy
        self.image_width = image_width
        self.image_height = image_height

    def classify_image(self, image: Image):
        im = image.resize((self.image_width, self.image_height))
        image_arr = asarray(im)
        classification = self.model.predict(image_arr)
        return classification
