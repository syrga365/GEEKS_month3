from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons
from handlers.offenders import offenders_list_call
from scraping.anime_scraper import AnimeScraper

async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="У вас раньше был ли опыт в этой сфере?",
        reply_markup=await inline_buttons.education_menu_keyboard()

    )


async def second_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какое направление вас интересует?",
        reply_markup=await inline_buttons.third_questionnaire_keyboard()

    )


async def backend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по backend пройдет в четверг 15:00. Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()
    )


async def frontend_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по frontend пройдет в понедельник 15:00.Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()
    )


async def android_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по android пройдет во вторник 15:00.Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()

    )


async def ux_ui_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по ux_ui дизайнер пройдет в среду 15:00.Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()
    )


async def ios_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по ios  пройдет в пятницу15:00.Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()
    )


async def manager_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по менеджер проектов пройдет в среду 15:00.Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()
    )


async def programming_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Отлично! Для того чтобы записаться на пробный урок регистрируйтесь!"
             "Пробный урок по ux_ui дизайнер пройдет в среду 15:00.Ждем вас!\n",
        reply_markup=await inline_buttons.registration_keyboard()

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
