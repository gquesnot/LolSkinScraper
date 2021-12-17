# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import json
import os

from scrapy.crawler import CrawlerProcess

from skins.skins.skinClass import Skin
from skins.skins.spiders.skinsScrapping import SkinsscrappingSpider


def startCrawler(path):
    try:
        os.remove(crawlPath)
    except:
        pass
    process = CrawlerProcess(settings={
        "FEEDS": {
            crawlPath: {"format": "json"},
        },
    })
    process.crawl(SkinsscrappingSpider)
    process.start()


def sortSkinByDuration(skins, hint="date"):
    if hint in ("date", "year"):
        res = {}
    else:
        res = {f"20{i:02d}/{j:02d}": [] for i in range(9, 22) for j in range(1, 13)}
    for skin in sorted(skins, key=lambda x: x.date, reverse=False):
        match hint:
            case "date":
                dateStr = skin.date
            case "month":
                dateStr = skin.getDateByMonth()
            case "year":
                dateStr = skin.getDateByYear()
            case _:
                continue
        if dateStr not in res:
            res[dateStr] = []
        res[dateStr].append(skin)

    return res


def parseSkins(path, hintDate):
    with open(crawlPath, "r") as f:
        skins = [Skin.from_dict(item) for item in json.load(f)]
        res = sortSkinByDuration(skins, hintDate)

        for dbm, skins in res.items():
            allPrices = 0
            prices = 0
            all = 0
            withChroma = 0

            for skin in skins:
                if skin.hasChroma:
                    withChroma += 1
                if skin.price is not None:
                    allPrices += 1
                    prices += skin.price
                all += 1
                # print(f"{dbm}\t{len(skins)}")
            if all > 0:
                print(
                    f"{dbm}\t"
                    f"{all}\t"
                    f"{withChroma}\t"
                    f"{int((withChroma / all) * 100) if allPrices else 0}%\t"
                    f"0\t"
                    f"{prices}"
                )
    # print(nbSkins, i)


if __name__ == '__main__':
    crawlPath = "result.json"
    startCrawler(crawlPath)
    # parseSkins(crawlPath, "month")

