from db import DB
from item import Item
from page_source import PageSource
from scrapper import Scrapper

url = 'https://www2.hm.com/ro_ro/index.html'
db_name = 'HM.db'
table_name = 'HM_ITEMS'
scrapper = Scrapper()


def main():
    db = DB(db_name)
    db.create_table(table_name)
    links = scrapper.get_all_url_from_page(url)
    for link in links:
        print("**LINK: "+link)
        ps = PageSource(link)
        item = Item()
        if ps.contains_items():
            items = ps.get_items()
            for i in items:
                item.name, item.price, item.category, item.image_url = ps.get_item_info(i)
                if not db.check_if_item_exists_in_table(table_name, item):
                    db.insert_into_table(table_name, item)
        new_links = scrapper.get_all_url_from_page(link)
        for new_link in new_links:
            if new_link not in links:
                links.append(new_link)
    print(len(links))
    db.close_conn()


if __name__ == "__main__":
    main()
