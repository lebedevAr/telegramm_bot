from db_map import get_names
import requests
import random


def to_db():
    res = get_names("test.db")
    print(res)


def get_cat_picture():
    api_url = 'https://aws.random.cat/meow'
    try:
        response = requests.get(api_url)
        cat_link = response.json()['file']
        return cat_link
    except:
        return None


def get_bear_picture():
    fr = random.randint(300, 700)
    sr = random.randint(300, 700)
    bear_api_url = f"https://placebear.com/g/{fr}/{sr}"
    try:
        name_responce = requests.get(bear_api_url)
        return name_responce.url
    except:
        return None


def get_random_num():
    return random.randint(1, 100)