import requests
from bs4 import BeautifulSoup
from config import auchanUrl, metroUrl

language = 'ru'

def getResult(shopUrl):
    response = requests.get(f'{shopUrl}/{language}/promotions')
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find_all('a', class_='jsx-631741978 NestedList__itemTitle NestedList__itemTitle_bold')
    global category_urls
    category_urls = {category.text:category.get('href') for category in categories}
    return [category.text for category in categories]


def getShopCategories(shopName):
    if shopName == 'Ашан':
        return getResult(auchanUrl)
    elif shopName == 'Метро':
        return getResult(metroUrl)

           
def categoryPrice(category):
    categoryUrl = category_urls.get(category)
    response = requests.get(f'{auchanUrl}{categoryUrl}')
    soup = BeautifulSoup(response.text, 'lxml')
    items_name = soup.find_all('span', class_='jsx-4147154605 ProductTile__title')
    item_discount_price = soup.find_all('span', class_='jsx-3642073353 Price__value_caption Price__value_discount')
    items = [item.text for item in items_name]
    return ''.join(
            f'{items[i]} {item_discount_price[i].text} грн.\n'
            for i in range(len(items))
        )