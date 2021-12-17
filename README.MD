# SCRAP LOL SKIN INFOS FROM [LOL FANDOM](https://leagueoflegends.fandom.com/wiki/List_of_champion_skins_(League_of_Legends))


Look at skins.json for Raw Data.

The parser is used to extract the data for Excel / google sheet 

### Installation and Usage

````shell
pip install requirements.txt
python main.py -wp
````
````
usage: main.py [-h] [-ws] [-wp] [-td TYPE_DATE]

Scrap Lol Data

options:
  -h, --help            show this help message and exit
  -ws, --without_scraping
                        run without scraping
  -wp, --without_parsing
                        run without parsing
  -td TYPE_DATE, --type_date TYPE_DATE
                        TYPE_DATE: year or month or day, default: year
````



### Get your Python Dataclasses with 
`````python
from my_dataclasses.skin import Skin

with open("skins.json", "r") as f:
    skins = [Skin.from_dict(item) for item in json.load(f)]
`````

