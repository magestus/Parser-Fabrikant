import urllib.request
from bs4 import BeautifulSoup
import re


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()
cases = []


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', {"Search-list"})

    for rows in table.find_all('div', {'Search-result-item'}):
        cols = rows.find_all('div', {'Search-item-option'})
               
        cases.append({
            'title': cols[0].a.text,
            'link': cols[0].select('a'),
            'price': re.sub(r'\s+', ' ', cols[1].text)
            #[price.text for price in cols[0].div.find('span', 'Search-item-label')]
        })
       
    for case in cases:
        print(case)


def main():
    parse(get_html('https://fabrikant.ru/trades/procedure/search/?type=1&query=&procedure_stage=2&price_from=&price_to=&currency=0&date_type=date_publication&date_from=&date_to=&ensure=all&section_type%5B%5D=ds300&count_on_page=10&order_by=default&order_direction=1'))

if __name__ == "__main__":
    main()