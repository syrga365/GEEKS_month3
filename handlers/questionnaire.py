import sqlite3
from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons
from handlers.offenders import offenders_list_call


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="У вас раньше был ли опыт в этой сфере?",
        reply_markup=await inline_buttons.education_menu_keyboard()

    )


async def second_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Ваш возраст?",
        reply_markup=await inline_buttons.second_menu_keyboard()

    )


async def third_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какое направление вас интересует?",
        reply_markup=await inline_buttons.third_questionnaire_keyboard()

    )


async def backend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите в четверг 15:00.\n"
             "Оставьте свой номер мы с вами свяжемся!"
    )


async def frontend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите в четверг 15:00.\n"
             "Оставьте свой номер мы с вами свяжемся!"
    )


async def android_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите во втоник 15:00.\n"
             "Оставьте свой номер мы с вами свяжемся!"

    )


async def ux_ui_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите в пятницу 15:00.\n"
             "Оставьте свой номер мы с вами свяжемся!"
    )


async def ios_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите в среду 18:00.\n"
             "Оставьте свой номер мы с вами свяжемся!",
    )


async def manager_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите в субботу 15:00.\n"
             "Оставьте свой номер мы с вами свяжемся!",
    )


async def programming_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Приходите в среду 18:00.\n"
             "Оставьте свой номер мы с вами свяжемся!",
    )



def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "start_question")

    dp.register_callback_query_handler(second_questionnaire_call,
                                       lambda call: call.data == "univer")

    dp.register_callback_query_handler(second_questionnaire_call,
                                       lambda call: call.data == "course")

    dp.register_callback_query_handler(second_questionnaire_call,
                                       lambda call: call.data == "first")

    dp.register_callback_query_handler(third_questionnaire_call,
                                       lambda call: call.data == "young")

    dp.register_callback_query_handler(third_questionnaire_call,
                                       lambda call: call.data == "age")

    dp.register_callback_query_handler(third_questionnaire_call,
                                       lambda call: call.data == "old")
    #
    dp.register_callback_query_handler(backend_call,
                                       lambda call: call.data == "backend")
    #
    dp.register_callback_query_handler(frontend_call,
                                       lambda call: call.data == "frontend")
    #
    dp.register_callback_query_handler(android_call,
                                       lambda call: call.data == "android")
    dp.register_callback_query_handler(ux_ui_call,
                                       lambda call: call.data == "ux_ui")
    dp.register_callback_query_handler(ios_call,
                                       lambda call: call.data == "ios")
    dp.register_callback_query_handler(manager_call,
                                       lambda call: call.data == "manager")
    dp.register_callback_query_handler(offenders_list_call,
                                       lambda call: call.data == "offenders_list")

