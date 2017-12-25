import html
import requests
from bs4 import BeautifulSoup

PSN_HOME = 'https://store.playstation.com'

def current_sales():
    DEALS_HOME = PSN_HOME + '/en-us/grid/STORE-MSF77008-WEEKLYDEALS'

    return list(map(get_sale_info, parse_grid(DEALS_HOME)))

def get_sale_info(tag):
    link = tag.find('a')

    return {
        'title': link.select('.grid-cell__title')[0].get_text(),
        'link': PSN_HOME + link.get('href')
    }

def get_deals(sale_id):
    sale_url = current_sales()[sale_id - 1]['link']

    return list(map(get_deal_info, parse_grid(sale_url)))

def get_deal_info(tag):
    original_price_elems = tag.select('.price-display__strikethrough')
    original_price = original_price_elems[0].get_text().strip() if len(original_price_elems) else ''

    sale_price_elems = tag.select('.price-display__price')
    sale_price = sale_price_elems[0].get_text() if len(sale_price_elems) else ''

    return {
        'title': html.unescape(tag.select('.grid-cell__title')[0].get_text()),
        'platform': tag.select('.grid-cell__left-detail--detail-1')[0].get_text(),
        'type': tag.select('.grid-cell__left-detail--detail-2')[0].get_text(),
        'original_price': original_price,
        'sale_price': sale_price,
        'link': 'https://store.playstation.com' + tag.find('a').get('href')
    }

def parse_grid(url):
    DISABLED_LINK_CLASS = 'paginator-control__arrow-navigation--disabled'
    grid_cells = []

    while url:
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')

        grid_cells += soup.select('.grid-cell__body')

        next_link = soup.select('.paginator-control__next')

        if len(next_link) and not DISABLED_LINK_CLASS in next_link[0].attrs['class']:
            url = PSN_HOME + next_link[0].get('href')
        else:
            url = None

    return grid_cells
