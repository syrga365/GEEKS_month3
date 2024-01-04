from aiogram import types, Dispatcher
from scraping.anime_scraper import AnimeScraper
from scraping.anime_parser import AnimeParser
from config import bot


async def scrape_anime(call: types.CallbackQuery):
    scraper = AnimeScraper()
    data = scraper.parse_data()
    for url in data:
        await call.message.answer(
            f"{url}"
        )


async def parser_anime(call: types.CallbackQuery):
    parser = AnimeParser()
    anime = parser.parse_data()
    for key, value in anime.items():
        await bot.send_photo(
            chat_id=call.from_user.id,
            file=value,
            caption=key
        )


def register_anime_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        scrape_anime, lambda call: call.data == "anime"
    )
    dp.register_callback_query_handler(
        parser_anime, lambda call: call.data == "parser"
    )
