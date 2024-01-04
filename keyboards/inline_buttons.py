from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Начнем опрос?👀",
        callback_data="start_question"
    )
    registration_button = InlineKeyboardButton(
        "Регистрация 🤩",
        callback_data="registration"
    )
    profile_button = InlineKeyboardButton(
        "Мой профиль 🔥",
        callback_data="my_profile"
    )
    view_profile_button = InlineKeyboardButton(
        "Виды профилей",
        callback_data='random_profile'
    )
    reference_menu_button = InlineKeyboardButton(
        "Реферальное меню",
        callback_data='reference_menu'
    )
    scraper_anime_button = InlineKeyboardButton(
        "Ссылки аниме",
        callback_data='anime'
    )
    parser_anime_button = InlineKeyboardButton(
        "Парсер аниме",
        callback_data='parser'
    )

    markup.add(registration_button)
    markup.add(questionnaire_button)
    markup.add(profile_button)
    markup.add(view_profile_button)
    markup.add(reference_menu_button)
    markup.add(scraper_anime_button)
    markup.add(parser_anime_button)
    return markup


async def registration_keyboard():
    markup = InlineKeyboardMarkup()
    registr_button = InlineKeyboardButton(
        'РЕГИСТРАЦИЯ',
        callback_data="registr"
    )

    markup.add(registr_button)
    return markup


async def survey_keyboard():
    markup = InlineKeyboardMarkup()
    survey_button = InlineKeyboardButton(
        'ОТЗЫВ',
        callback_data="review"
    )
    markup.add(survey_button)
    return markup

#
# async def complain_keyboard():
#     markup = InlineKeyboardMarkup()
#     complain_button = InlineKeyboardButton(
#         'ЖАЛОБ',
#         callback_data="complain"
#     )
#     markup.add(complain_button)
#     return markup


async def offenders_menu_keyboard():
    markup = InlineKeyboardMarkup()
    ban_users_button = InlineKeyboardButton(
        "Правонарушители",
        callback_data="offenders_list"
    )
    markup.add(ban_users_button)
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


async def like_dislike_keyboard(owner_tg_id):
    markup = InlineKeyboardMarkup()
    good_button = InlineKeyboardButton(
        "НРАВИТЬСЯ🔥",
        callback_data=f"like_{owner_tg_id}"
    )
    bad_button = InlineKeyboardButton(
        "НЕ НРАВИТЬСЯ👎",
        callback_data=f"hater_{owner_tg_id}"
    )
    markup.add(good_button)
    markup.add(bad_button)
    return markup


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
    "Ссылка",
        callback_data="link_reference"
    )
    list_reference_button = InlineKeyboardButton(
    "Список рефералов",
        callback_data="list_reference"
    )
    markup.add(link_button)
    markup.add(list_reference_button)
    return markup

