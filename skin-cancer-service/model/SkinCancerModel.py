from sklearn.linear_model import LogisticRegression
from .SkinCancer import SkinCancer


class SkinCancerModel:
    model: LogisticRegression

    def __init__(self) -> None:
        # create the skin cancer machine-learning model
        pass

    def get_skin_cancer(image: str) -> SkinCancer:
        pass
