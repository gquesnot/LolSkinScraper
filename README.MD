# SCRAP LOL SKIN INFOS FROM [LOL FANDOM](https://leagueoflegends.fandom.com/wiki/List_of_champion_skins_(League_of_Legends))


for python 3.10.

Look at skins.json for Raw Data

### Installation and Usage

````shell
pip install requirements.txt
python main.py -wp
````
````
usage: main.py [-h] [-ws] [-wp] [-dt DATE_TYPE]

Scrap Lol Data

options:
  -h, --help            show this help message and exit
  -ws, --without_scraping
                        run without scraping
  -wp, --without_parsing
                        run without parsing
  -dt DATE_TYPE, --date_type DATE_TYPE
                        type de date : year or month or day
````



### Get your Python Dataclasses with 
`````python
from my_dataclasses.skin import Skin

with open("skins.json", "r") as f:
    skins = [Skin.from_dict(item) for item in json.load(f)]
`````

