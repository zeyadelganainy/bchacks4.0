from enum import Enum


class SkinCancer(Enum):
    '''
    7 different types of skin cancer
    AKIEC: Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec)
    BCC: basal cell carcinoma (bcc)
    BKL: benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl)
    DF: dermatofibroma (df)
    MEL: melanoma (mel)
    NV: melanocytic nevi
    VASC: vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc).
    '''
    AKIEC = 'akiec'
    BCC = 'bcc'
    BKL = 'bkl'
    DF = 'df'
    MEL = 'mel'
    NV = 'nv'
    VASC = 'vasc'
