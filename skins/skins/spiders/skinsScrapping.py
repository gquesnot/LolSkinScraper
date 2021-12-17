import scrapy

from my_dataclasses.price import Price
from my_dataclasses.skin import Skin
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

                skinName = tds[1].xpath("text()").get()
                date = tds[3].xpath("text()").get().split('-')
                hasChroma = tds[13].css('span').get() is not None
                price = tds[4].xpath('span/text()').get()
                isAvailable = tds[2].css("span").get() is not None
                hasVoiceFilter = tds[5].css("span").get() is not None
                hasAdditonalUniqueQuotes = tds[6].css("span").get() is not None
                hasNewVoiceHover = tds[7].css("span").get() is not None
                hasNewVisualAndOrSoundEffect = tds[8].css("span").get() is not None
                hasNewAnimationAndOrRecallAnimation = tds[9].css("span").get() is not None
                hasAnimationCanBeToggleIG = tds[10].css("span").get() is not None
                isPartOfCollection = tds[11].css("span").get() is not None
                hasFeaturesLores = tds[12].css("span").get() is not None
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
                price = Price.from_dict(priceDict)
                # if price in ("5000", "150000", "special", "", "None"):
                #     price= None
                # else:
                #     price = int(price)

                if date[0] == "N/A":
                    date = None
                else:
                    date = f"{date[2]}/{self.dateMapping.index(date[1]) + 1:02d}/{date[0]}"

                    yield Skin.from_dict({
                        "name": skinName,
                        "date": date,
                        "hasChroma": hasChroma,
                        "price": price.to_dict(),
                        "isAvailable": isAvailable,
                        "hasVoiceFilter": hasVoiceFilter,
                        "hasAdditonalUniqueQuotes": hasAdditonalUniqueQuotes,
                        "hasNewVoiceHover": hasNewVoiceHover,
                        "hasNewVisualAndOrSoundEffect": hasNewVisualAndOrSoundEffect,
                        "hasNewAnimationAndOrRecallAnimation": hasNewAnimationAndOrRecallAnimation,
                        "hasAnimationCanBeToggleIG": hasAnimationCanBeToggleIG,
                        "isPartOfCollection": isPartOfCollection,
                        "hasFeaturesLores": hasFeaturesLores,
                    })
