# from parsel import Selector
# import requests
#
#
# class AnimeParser:
#     XPATH_TITLE = '//div[@class="custom-poster"]/a/img/@alt'
#     MAIN_URL = "https://animespirit.tv/"
#     INFO_XPATH = '//div[@class="custom-poster"]/a/@href'
#     MEDIA_XPATH = '//div[@class="custom-poster"]/a/img/@src'
#
#     def parse_data(self):
#         response = requests.get(url=self.MAIN_URL).text
#         tree = Selector(text=response)
#         title = tree.xpath(self.XPATH_TITLE).extract()
#         links = tree.xpath(self.INFO_XPATH).extract()
#         media = tree.xpath(self.MEDIA_XPATH).extract()
#         anime = []
#
#         for i in range(7):
#             anime.append({
#                 "title": title[-i],
#                 "link": links[-i],
#                 "photo": media[-i]
#             })
#
#         return anime
#
#
# if __name__ == "__main__":
#     scraper = AnimeParser()
#     scraper.parse_data()
