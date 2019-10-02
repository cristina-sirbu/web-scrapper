from urllib.request import Request, urlopen
from pyquery import PyQuery

req = Request('https://www2.hm.com/ro_ro/femei/cumparaturi-sortate-dupa-produs/view-all.html', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()


# fp = urllib.request.urlopen("https://www.sinsay.com", headers={'User-Agent': 'Mozilla/5.0'})
# mybytes = fp.read()
#
# mystr = mybytes.decode("utf8")
# fp.close()

parsed_html = PyQuery(webpage)
tag = parsed_html('#main-content > div.sidebar-plus-content > div > div > div:nth-child(5) > ul > li:nth-child(1) > article > div.item-details > h3 > a')
print(tag.text())

# articles = parsed_html.body.findAll('article', attrs={'class':'hm-product-item'})
# for article in articles:
#     print(article['data-category'])
