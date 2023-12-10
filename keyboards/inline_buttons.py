from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начнем опрос?",
        callback_data="start_question"
    )
    markup.add(questionnaire_button)
    return markup


async def education_menu_keyboard():
    markup = InlineKeyboardMarkup()
    univer_button = InlineKeyboardButton(
        "В университете",
        callback_data="univer"
    )
    course_button = InlineKeyboardButton(
        "У других курсах",
        callback_data="course"
    )
    first_button = InlineKeyboardButton(
        "В первые",
        callback_data="first"
    )
    markup.add(univer_button)
    markup.add(course_button)
    markup.add(first_button)
    return markup


async def second_menu_keyboard():
    markup = InlineKeyboardMarkup()
    young_button = InlineKeyboardButton(
        "8-18",
        callback_data="young"
    )
    age_button = InlineKeyboardButton(
        "19-45",
        callback_data="age"
    )
    old_button = InlineKeyboardButton(
        "46 и больше",
        callback_data="old"
    )
    markup.add(young_button)
    markup.add(age_button)
    markup.add(old_button)
    return markup


async def third_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    backend_button = InlineKeyboardButton(
        "Backend",
        callback_data="backend"
    )
    frontend_button = InlineKeyboardButton(
        "Frontend",
        callback_data="frontend"
    )
    android_button = InlineKeyboardButton(
        "Android-разработка",
        callback_data="android"
    )
    ux_ui_button = InlineKeyboardButton(
        "UX/UI дизайнер",
        callback_data="ux_ui"
    )
    ios_button = InlineKeyboardButton(
        "IOS-разработчик",
        callback_data="ios"
    )
    manager_button = InlineKeyboardButton(
        "Менеджер проектов",
        callback_data="manager"
    )

    markup.add(backend_button)
    markup.add(frontend_button)
    markup.add(android_button)
    markup.add(ux_ui_button)
    markup.add(ios_button)
    markup.add(manager_button)
    return markup
