import sys
from requests.api import get
from models import *
sys.path.insert(0, '/previa/src/webscraping/')
from webscraping import cup
from webscraping import matches
from webscraping import awards
import json
import os

#main function
def get_world_cups():

    start_year = 1991
    final_year = 2019

    page_id = 1779
    cup_list=[]
    awards_list = awards.create_awards()

    while (start_year<=final_year):
        print(start_year)

        if not os.path.isfile(f'world_cup{start_year}.json'):
            new_cup = cup.create_new_cup(start_year, page_id)
            new_cup.awards = awards.get_awards_by_year(awards_list, start_year)
            cup_list.append(new_cup)
            with open(f'world_cup{start_year}.json', 'w+', encoding="utf-8") as f:
                json.dump(
                    new_cup.dict(exclude_none=True),
                    f,
                    ensure_ascii=False,
                    indent=2
                )
        print('finished year: ',start_year)
        start_year += 4
        page_id += 1
    return cup_list

get_world_cups()

    