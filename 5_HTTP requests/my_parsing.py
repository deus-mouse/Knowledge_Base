import requests
from bs4 import BeautifulSoup

response = requests.get('https://yandex.ru/')

if response.status_code == 200:
    html_doc = BeautifulSoup(response.text, features='html.parser')
    list_of_names = html_doc.find_all('a', {'class': 'home-link home-link_black_yes inline-stocks__link'})
    list_of_values = html_doc.find_all('span', {'class': 'inline-stocks__value_inner'})

    for names, values in zip(list_of_names, list_of_values):
        print(names.text, values.text)


