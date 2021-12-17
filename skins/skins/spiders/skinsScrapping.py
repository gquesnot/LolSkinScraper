import scrapy

from my_dataclasses.price import Price
from my_dataclasses.skin import Skin
from my_enum.availability_type import AvailabilityType
from my_enum.price_type import PriceType


class SkinsscrappingSpider(scrapy.Spider):
    name = 'skinsScrapping'
    allowed_domains = ['https://leagueoflegends.fandom.com/wiki/List_of_champion_skins_(League_of_Legends)']
    start_urls = ['https://leagueoflegends.fandom.com/wiki/List_of_champion_skins_(League_of_Legends)']
    cssSelector = ".sortable tr"

    dateMapping = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Nov",
        "Oct",
        "Dec"

    ]

    def parse(self, response, **kwargs):
        print(len(response.css(self.cssSelector)))
        for row in response.css(self.cssSelector):
            tds = row.css("td")
            if len(tds) > 0:
                date = tds[3].xpath("text()").get().split('-')
                price = tds[4].xpath('span/text()').get()
                try:
                    price = int(price)
                    priceDict = {
                        "type" : PriceType.EB if price in (5000, 150000) else PriceType.RP,
                        "value": price
                    }
                except:
                    price= None
                    priceDict = {
                        "type": PriceType.SPECIAL,
                        "value": None
                    }

                if date[0] == "N/A":
                    date = None
                else:
                    date = f"{date[2]}/{self.dateMapping.index(date[1]) + 1:02d}/{date[0]}"
                    available = tds[2].css("span").get()
                    if "Available" in available:
                        available = AvailabilityType.AVAILABLE
                    elif "Legacy" in available:
                        available = AvailabilityType.LEGACY
                    elif "Rare" in available:
                        available=  AvailabilityType.RARE
                    elif "Limited" in available:
                        available = AvailabilityType.LIMITED
                    elif "Removed" in available:
                        available = AvailabilityType.REMOVED
                    yield Skin.from_dict({
                        "name": tds[1].xpath("text()").get(),
                        "date": date,
                        "hasChroma": tds[13].css('span').get() is not None,
                        "price": Price.from_dict(priceDict).to_dict(),
                        "available": available,
                        "hasVoiceFilter": tds[5].css("span").get() is not None,
                        "hasAdditonalUniqueQuotes": tds[6].css("span").get() is not None,
                        "hasNewVoiceHover": tds[7].css("span").get() is not None,
                        "hasNewVisualAndOrSoundEffect": tds[8].css("span").get() is not None,
                        "hasNewAnimationAndOrRecallAnimation": tds[9].css("span").get() is not None,
                        "hasAnimationCanBeToggleIG": tds[10].css("span").get() is not None,
                        "isPartOfCollection": tds[11].css("span").get() is not None,
                        "hasFeaturesLores": tds[12].css("span").get() is not None,
                    })
