from enum import Enum


class ClinicalClassification(str, Enum):
    """Clinical Classification"""
    INTERNADO = 'INTERNADO'
    LEVE = 'LEVE'
    SINDROME_GRIPAL = 'SINDROME_GRIPAL'
