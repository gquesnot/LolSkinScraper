from strenum import StrEnum
from enum import auto


class AvailabilityType(StrEnum):
    LIMITED = auto()
    RARE = auto()
    AVAILABLE = auto()
    LEGACY = auto()
    REMOVED = auto()
