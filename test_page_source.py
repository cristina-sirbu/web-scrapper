import unittest

from db import DB
from page_source import PageSource


class PageSourceTest(unittest.TestCase):

    url = 'https://www2.hm.com/ro_ro/femei/bridge-the-seasons/now-or-never.html'
    page_source = PageSource(url)

    @classmethod
    def setUpClass(cls):
        cls.db = DB('test.db')

    @classmethod
    def tearDownClass(cls):
        cls.db.close_conn()

    '''PageSource tests'''
    def test_get_page_source(self):
        self.assertTrue('hmApp' in str(self.page_source.get_html(self.url)))

    def test_get_items(self):
        items = self.page_source.get_items()
        self.assertEqual(36, len(items), "Not enough items on a page")

    def test_get_item_info(self):
        item = self.page_source.get_items()[0]
        name, price, category, image_url = self.page_source.get_item_info(item)
        self.assertEqual("Chiloți Thong de bumbac, 7", name, "Wrong name!")
        self.assertEqual("49,99 LEI", price, "Wrong price!")
        self.assertEqual("ladies_lingerie_briefsknickers_thong", category, "Wrong category!")
        self.assertEqual("https://www2.hm.com/ro_ro/productpage.0748355002.html", image_url, "Wrong image URL!")

    '''DB tests'''
    def test_run_query(self):
        self.assertEqual('3.28.0', self.db.run_query('select sqlite_version();')[0][0], "Incorrect Sqlite version")

    def test_check_if_item_exists_in_table(self):
        self.db.create_table("A")
        self.db.insert_into_table("A", "A", "1", "A", "A")
        self.assertTrue(self.db.check_if_item_exists_in_table("A", "A", "1", "A", "A"))
        self.assertFalse(self.db.check_if_item_exists_in_table("A", "B", "2", "B", "B"))
