import requests
from bs4 import BeautifulSoup

def func():
    url = 'https://auchan.zakaz.ua/ru/promotions/?category_id=low-price-auchan'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items_name = soup.find_all('span', class_='jsx-4147154605 ProductTile__title')
    item_discount_price = soup.find_all('span', class_='jsx-3642073353 Price__value_caption Price__value_discount')
    items = [item.text for item in items_name]
    return ''.join(
        f'{items[i]} {item_discount_price[i].text} грн.\n'
        for i in range(len(items))
    )