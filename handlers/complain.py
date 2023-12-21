from aiogram import types, Dispatcher
from config import bot
from database.sql_commands import Database


async def complain(message: types.Message):
    db = Database
    c_user = message.text.replace('/complain', "").replace("", "")
    c_user_id = db.sql_select_user_command(c_user)
    if c_user_id:
        await bot.send_message(chat_id=c_user_id,
                               text="На вас пожаловались")
    else:
        await message.answer('Пользователя с таким именем нету!!!')


def register_complain_handlers(dp: Dispatcher):
    dp.register_message_handler(complain, commands=['complain'])

