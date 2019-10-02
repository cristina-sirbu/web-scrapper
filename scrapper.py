from bs4 import BeautifulSoup

from page_source import PageSource


class Scrapper:
    parsed_links = []

    def get_all_url_from_page(self, url):
        pg = PageSource(url)
        soup = BeautifulSoup(pg.html, "html.parser")
        links = soup.find_all('a', class_='link')
        unique_list = self.unique(links)
        for link in unique_list:
            if link.has_attr('href'):
                if link["href"].startswith("https://www2.hm.com/"):
                    self.parsed_links.append(link["href"])
                else:
                    if not link["href"].startswith("http"):
                        self.parsed_links.append("https://www2.hm.com"+link["href"])
        return self.parsed_links

    def unique(self, links):
        seen = set()
        for l in links:
            ll = l.get('href')
            if ll not in seen:
                seen.add(ll)
                yield l
        return list(seen)