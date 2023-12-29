from parsel import Selector
import requests


class AnimeScraper:
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-language": "en-US,en;q=0.5",
        "Accept=Encoding": "gzip, deflate, br"
    }
    MAIN_URL = "https://animespirit.tv/"

    def parse_data(self):
        response = requests.get(url=self.MAIN_URL, headers=self.headers)
        if response.status_code > 400:
            return []
        selector = Selector(text=response.text)

        all_links = selector.xpath('//div[@class="<div class="custom-label-stat-full"]/a/@href')
        return all_links


if __name__ == "__main__":
    scraper = AnimeScraper()
    print(scraper.parse_data())