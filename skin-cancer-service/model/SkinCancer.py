from enum import Enum

class SkinCancer(Enum):
    '''
    Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec),
    basal cell carcinoma (bcc),
    benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl),
    dermatofibroma (df),
    melanoma (mel),
    melanocytic nevi (nv) and
    vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc).
    '''
    AKIEC = 'akiec'
    BCC = 'bcc'
    BKL = 'bkl'
    MEL = 'mel'
    NV = 'nv'
    VASC = 'vasc'
