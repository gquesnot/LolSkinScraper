from dataclasses import dataclass, asdict
from typing import Union, Dict, Any

from dacite import from_dict

from my_enum.price_type import PriceType


@dataclass
class Price:
    type: PriceType
    value: Union[int, None]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Price":
        if isinstance(data['type'], str):
            data['type'] = getattr(PriceType, data['type'])
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)