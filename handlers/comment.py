import config
from aiogram import Dispatcher, types
from config import bot
from const import COMMENT
from database.sql_commands import Database
from aiogram.dispatcher import FSMContext


async def comment_button(message: types.Message,
                         state: FSMContext):
    db = Database
    admin = config.ADMIN_ID
    async with state.proxy() as data:
        db.sql_insert_survey(
            problems=data['problems'],
            idea=data['idea']
        )
        if admin:
            await bot.send_message(
                chat_id=message.from_user.id,
                caption=COMMENT.format(
                    problems=data['problems'],
                    idea=data['idea']
                )
            )

        else:
            await bot.send_message(
                chat_id=message.from_user.id,
                text='Только админы могут читать отзывы!!!'
            )


def register_comment_handlers(dp: Dispatcher):
    dp.register_message_handler(comment_button, commands=['comments'])


