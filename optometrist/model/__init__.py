from pathlib import Path

MODEL_FILENAME = "model.pkl"
MODEL_DIR = Path(__file__).parent
MODEL_FILEPATH = MODEL_DIR / MODEL_FILENAME
DERMA_DIR = MODEL_DIR.parent
DATA_DIR = DERMA_DIR / "data"

IMAGE_WIDTH = 32
