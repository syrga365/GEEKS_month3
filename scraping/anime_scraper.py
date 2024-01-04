from parsel import Selector
import requests


class AnimeScraper:
    MAIN_URL = "https://animespirit.tv/"
    LINK_XPATH = '//div[@class="custom-poster"]/a/@href'

    def parse_data(self):

        response = requests.get(url=self.MAIN_URL).text
        tree = Selector(text=response)
        links = tree.xpath(self.LINK_XPATH).extract()
        return links[:6]


if __name__ == "__main__":
    scraper = AnimeScraper()
    scraper.parse_data()
