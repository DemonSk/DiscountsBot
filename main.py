import requests
from bs4 import BeautifulSoup
from config import auchanUrl, metroUrl, novusUrl

language = 'ru'

def getResult(url):
    response = requests.get(f'{url}/{language}/promotions')
    soup = BeautifulSoup(response.text, 'lxml')
    categories = soup.find_all('a', {'class' : ['jsx-631741978 NestedList__itemTitle NestedList__itemTitle_bold']})
    global category_urls
    category_urls = {category.text:category.get('href') for category in categories}
    return [category.text for category in categories]


def getShopCategories(shopName):
    global shopUrl
    if shopName == 'Ашан':
        shopUrl = auchanUrl
    elif shopName == 'Метро':
        shopUrl = metroUrl
    elif shopName == 'Novus':
        shopUrl = novusUrl
    return getResult(shopUrl)

           
def categoryPrice(category):
    categoryUrl = category_urls.get(category)
    response = requests.get(f'{shopUrl}{categoryUrl}')
    soup = BeautifulSoup(response.text, 'lxml')
    items_name = soup.find_all('span', {'data-testid':["product_tile_title"]})
    item_original_price = soup.find_all('span', class_='jsx-3642073353 Price__value_body Price__value_minor')
    item_discount_price = soup.find_all('span', class_='jsx-3642073353 Price__value_caption Price__value_discount')
    items = [item.text for item in items_name]
    return ''.join(
            f'{items[i]} {item_discount_price[i].text} грн.\n'
            for i in range(len(items))
        )
    