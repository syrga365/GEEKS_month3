from parsel import Selector
import requests


class AnimeScraper:
    headers = {
        "User-agent": "",
        "Accept-language": "",
        "Accept=Encoding": ""
    }
    MAIN_URL = ""
    PLUS_URL = ""

    def parse_data(self):
        response = requests.get(url=self.MAIN_URL, headers=self.headers).text
        print(response)
        selector = Selector(text=response)
        links = selector.xpath("").get()
        links_anime = []
        all_links = selector.xpath()
        return all_links


if __name__ == "__main__":
    scraper = AnimeScraper()
    print(scraper.parse_data())