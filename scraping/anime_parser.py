from parsel import Selector
import requests


class AnimeParser:
    MAIN_URL = "https://animespirit.tv/"
    INFO_XPATH = '//div[@class="custom-poster"]/a/@href'
    MEDIA_XPATH = '//div[@class="custom-poster"]/a/img/@src'

    def parse_data(self):
        response = requests.get(url=self.MAIN_URL).text
        tree = Selector(text=response)
        info = tree.xpath(self.INFO_XPATH).extract()
        media = tree.xpath(self.MEDIA_XPATH).extract()
        anime = {}

        for key, value in info[-6:], media[-6:]:
            anime[key] = value

        return anime


if __name__ == "__main__":
    scraper = AnimeParser()
    scraper.parse_data()
