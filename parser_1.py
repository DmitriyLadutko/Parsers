import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.mebelshara.ru/contacts'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 '
                  'Safari/537.36 '
}


def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='shop-list-item')
    print(items)

    contact = []

    for item in items:
        address = item.get('data-shop-address')
        phone = sorted(item.get('data-shop-phone').split(", "))
        hours = ''.join(item.get('data-shop-mode1')) + ''.join(item.get('data-shop-mode2'))
        name = item.get('data-shop-name')
        latitude = float(item.get('data-shop-latitude'))
        longitude = float(item.get('data-shop-longitude'))

        contact.append({
            'address': address,
            'location:': (latitude, longitude),
            'name': name,
            'phone': phone,
            'working_hours': hours,
        })
    with open('some_file.json', 'w') as file:
        json.dump(contact, file, indent=4, ensure_ascii=False)
    return contact


html = get_html(URL)
print(get_content(html.text))
