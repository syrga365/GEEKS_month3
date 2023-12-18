
import config
from aiogram import Dispatcher, types
from config import bot
from const import COMMENT


async def comment_button(call: types.CallbackQuery):
    admin = config.ADMIN_ID
    if not admin:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Только админы может читать отзывы!'
        )

    else:
        await bot.send_message(
           chat_id=call.from_user.id,
           text=COMMENT.format(
               problems=['problems'],
               idea=['idea']
           )

        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(comment_button, commands=['comment'])


