# from aiogram import types, Dispatcher
# from scraping.anime_scraper import AnimeScraper
# from scraping.anime_parser import AnimeParser
# from config import bot
# from const import PARSER_TEXT
#
#
# async def scrape_anime(call: types.CallbackQuery):
#     scraper = AnimeScraper()
#     data = scraper.parse_data()
#     for url in data:
#         await call.message.answer(
#             f"{url}"
#         )
#
#
# async def parser_anime(call: types.CallbackQuery):
#     parser = AnimeParser()
#     data = parser.parse_data()
#     for anime in data:
#         await bot.send_photo(
#             chat_id=call.from_user.id,
#             photo=anime['photo'],
#             caption=PARSER_TEXT.format(
#                 title=anime['title'],
#                 link=anime['link']
#             ),
#             parse_mode=types.ParseMode.MARKDOWN,
#         )
#
#
# def register_anime_handlers(dp: Dispatcher):
#     dp.register_callback_query_handler(
#         scrape_anime, lambda call: call.data == "anime"
#     )
#     dp.register_callback_query_handler(
#         parser_anime, lambda call: call.data == "parser"
#     )
