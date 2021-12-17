# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import argparse
import json
import os

from scrapy.crawler import CrawlerProcess

from my_dataclasses.skin import Skin
from my_enum.price_type import PriceType
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

        if hint == "date":
            dateStr = skin.date
        elif hint == "month":
            dateStr = skin.getDateByMonth()
        elif hint == "year":
            dateStr = skin.getDateByYear()
        else:
            continue
        if dateStr not in res:
            res[dateStr] = []
        res[dateStr].append(skin)

    return res


def parseSkins(path, hintDate):
    with open(crawlPath, "r") as f:
        skins = [Skin.from_dict(item) for item in json.load(f)]
        res = sortSkinByDuration(skins, hintDate)

    for dateByHint, skins in res.items():
        allPrices = 0
        prices = 0
        all = 0
        withChroma = 0

        for skin in skins:
            if skin.hasChroma:
                withChroma += 1
            if skin.price.type == PriceType.RP:
                allPrices += 1
                prices += skin.price.value
            all += 1
            # print(f"{dateByHint}\t{len(skins)}")
        if all > 0:
            print(
                f"{dateByHint}\t"
                f"{all}\t"
                f"{withChroma}\t"
                f"{int((withChroma / all) * 100) if all else 0}%\t"
                f"{prices/allPrices if allPrices else 0}\t"
                f"{prices}"
            )
    # print(nbSkins, i)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrap Lol Data')
    parser.add_argument('-ws','--without_scraping', help="run without scraping", action="store_true")
    parser.add_argument('-wp','--without_parsing', help="run without parsing", action="store_true")
    parser.add_argument('-td','--type_date', type=str, default="year", help="TYPE_DATE: year or month or day, default: year")

    args = parser.parse_args()
    print(args)
    crawlPath = "skins.json"
    if not args.without_scraping:
        startCrawler(crawlPath)
    if not args.without_parsing:
        parseSkins(crawlPath, args.date_type)

