import datetime
import time
from dataclasses import dataclass, asdict
from typing import Dict, Any, Union

import dacite
from dacite import from_dict

from my_dataclasses.price import Price
from my_enum.availability_type import AvailabilityType
from my_enum.price_type import PriceType


@dataclass
class Skin:
    date: Union[str, None]
    name: str
    timestamp: Union[int, None]
    hasChroma: bool
    available: AvailabilityType
    hasVoiceFilter: bool
    hasAdditonalUniqueQuotes: bool
    hasNewVoiceHover: bool
    hasNewVisualAndOrSoundEffect: bool
    hasNewAnimationAndOrRecallAnimation: bool
    hasAnimationCanBeToggleIG: bool
    isPartOfCollection: bool
    hasFeaturesLores: bool
    price: Price

    def getDateByMonth(self):
        return "/".join(self.date.split('/')[:-1])

    def getDateByYear(self):
        return self.date.split('/')[0]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Skin":
        if "timestamp" not in data and data['date'] is not None:
            data['timestamp'] = int(time.mktime(datetime.datetime.strptime(data['date'],"%Y/%m/%d").timetuple()))
        elif data['date'] is None:
            data['timestamp'] = None
        return from_dict(cls, data=data,config=dacite.Config(type_hooks={PriceType: PriceType}))

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)