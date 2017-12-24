import requests
from bs4 import BeautifulSoup

def current_sales():
    DEALS_HOME = 'https://store.playstation.com/en-us/grid/STORE-MSF77008-WEEKLYDEALS/1'

    res = requests.get(DEALS_HOME)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')

    return list(map(get_sale_info, soup.select('.grid-cell__body')))


def get_sale_info(tag):
    link = tag.find('a')

    return {
        'name': link.select('.grid-cell__title')[0].get_text(),
        'href': 'https://store.playstation.com' + link.get('href')
    }
