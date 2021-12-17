from strenum import StrEnum
from enum import auto

class PriceType(StrEnum):
    SPECIAL = auto()
    NONE = auto()
    RP = auto()
    EB = auto()
