import string
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class PageSource(object):

    def __init__(self, url):
        self.html = self.get_html(url)

    def get_html(self, url: string) -> string:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_page = urlopen(req).read()
        return web_page

    def get_items(self):
        soup = BeautifulSoup(self.html, "html.parser")
        items = soup.find_all('li', class_='product-item')
        return items

    def contains_items(self):
        items = self.get_items()
        if items:
            return True
        else:
            return False

    def get_item_info(self, item):
        name = item.find('a', class_='item-link')['title']
        price = item.find('span', class_='price regular').getText()
        category = item.find('article', class_='hm-product-item')['data-category']
        image_url = "https://www2.hm.com"+item.find('a', class_='item-link')['href']
        return name, price, category, image_url
