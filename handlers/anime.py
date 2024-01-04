from aiogram import types, Dispatcher
from scraping.anime_scraper import AnimeScraper


async def scrape_anime(call: types.CallbackQuery):
    scraper = AnimeScraper()
    data = scraper.parse_data()
    for url in data:
        await call.message.answer(
            f"{url}"
        )


def register_anime_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        scrape_anime, lambda call: call.data == "anime"
    )
