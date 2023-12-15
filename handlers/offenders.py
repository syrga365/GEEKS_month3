from keyboards.inline_buttons import offenders_menu_keyboard
from aiogram import types, Dispatcher
from config import bot, GROUP_ID
from database.sql_commands import Database


async def offenders_button(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Нажмите на кнопку вниз чтобы узнать вы в списке нарушителей или нет",
        reply_markup=await offenders_menu_keyboard()
    )


async def offenders_list_call(message: types.Message):
    db = Database()
    user = db.sql_select_ban_user(message.from_user.id)

    if user:
        text = (f"{message.from_user.first_name}"
                f"Ты в списке правонарушителей!!! Предупреждаем, тебя может забанить!")
    else:
        text = f"Привет {message.from_user.first_name}! Тебя нету в списке правонарушителей! Так держать!"

    await bot.send_message(
        chat_id=GROUP_ID,
        text=text,
    )


def register_offenders_handlers(dp: Dispatcher):
    dp.register_message_handler(offenders_button, commands=['offenders'])






