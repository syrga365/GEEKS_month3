import re
import random
import sqlite3

from aiogram import types, Dispatcher
from config import bot
from const import PROFILE_TEXT
from database.sql_commands import Database
from keyboards.inline_buttons import like_dislike_keyboard


async def my_profile_call(call: types.CallbackQuery):
    db = Database()
    profile = db.sql_select_profile_users(
        tg_id=call.from_user.id
    )
    with open(profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.from_user.id,
            photo=photo,
            caption=PROFILE_TEXT.format(
                nickname=profile['nickname'],
                biography=profile['biography'],
                age=profile['age'],
                hobby=profile['hobby'],
                number=profile['call_number'],
                email=profile['email'],
                instagram=profile['instagram']
            ),
            parse_mode=types.ParseMode.MARKDOWN,

        )


async def random_profile_call(call: types.CallbackQuery):
    db = Database()
    profiles = db.sql_select_filter_profiles(
        tg_id=call.from_user.id,

    )
    if profiles:
        random_profile = random.choice(profiles)
        with open(random_profile['photo'], 'rb') as photo:
            await bot.send_photo(
                    chat_id=call.from_user.id,
                    photo=photo,
                    caption=PROFILE_TEXT.format(
                        nickname=random_profile['nickname'],
                        biography=random_profile['biography'],
                        age=random_profile['age'],
                        hobby=random_profile['hobby'],
                        number=random_profile['call_number'],
                        email=random_profile['email'],
                        instagram=random_profile['instagram']
                    ),
                    parse_mode=types.ParseMode.MARKDOWN,
                    reply_markup=await like_dislike_keyboard(owner_tg_id=random_profile['telegram_id'])
                )
    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Нету профилей который вы не оценили!!!"
        )


async def like_detect_call(call: types.CallbackQuery):
    db = Database()
    owner = re.sub('like_', "", call.data)
    print(call.data)
    print(owner)
    try:
        db.sql_insert_like(
            owner=owner,
            liker=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Вы уже оценили этот профиль!!!"
        )
    finally:
        await random_profile_call(call=call)


async def hate_detect_call(call: types.CallbackQuery):
    db = Database()
    owner = re.sub('hater_', "", call.data)
    print(call.data)
    print(owner)
    try:
        db.sql_insert_hater(
            owner=owner,
            hater=call.from_user.id
        )
    except sqlite3.IntegrityError:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Вы уже оценили этот профиль!!!"
        )
    finally:
        await random_profile_call(call=call)


def register_profile_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        my_profile_call,
        lambda call: call.data == "my_profile"
    )
    dp.register_callback_query_handler(
        random_profile_call,
        lambda call: call.data == "random_profile"
    )
    dp.register_callback_query_handler(
        like_detect_call,
        lambda call: "like_" in call.data
    )
    dp.register_callback_query_handler(
        hate_detect_call,
        lambda call: "like_" in call.data
    )

