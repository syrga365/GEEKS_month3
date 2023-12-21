import sqlite3
from aiogram import types, Dispatcher
from config import bot, MEDIA_DESTINATION
from const import PROFILE_TEXT
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database.sql_commands import Database
from keyboards import inline_buttons


class RegistrationStates(StatesGroup):
    nickname = State()
    biography = State()
    age = State()
    hobby = State()
    number = State()
    email = State()
    instagram = State()
    photo = State()


async def registration_start(call: types.CallbackQuery):
    db = Database()
    user = db.sql_select_profile(call.from_user.id)
    if user:
        await bot.send_message(
            chat_id=call.from_user.id,
            text='Вы зарегистрированы на наш пробный урок🤗',
            reply_markup=await inline_buttons.survey_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=call.from_user.id,
            text="Отправьте свой никнейм:"
        )
        await RegistrationStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Расскажите о себе:"
    )
    await RegistrationStates.next()


async def load_biography(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['biography'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Сколько вам лет?Введите в виде число:"
    )
    await RegistrationStates.next()


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        type(int(message.text))
    except ValueError:
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Я ведь сказала введить число! Регистрерируйтесь с начала!'
        )
        await state.finish()
        return

    async with state.proxy() as data:
        data['age'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Какие ваши любимые занятие? Надеюсь вам понравиться программирование и станет вашей хобби!"
    )
    await RegistrationStates.next()


async def load_hobby(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Введите свой номер телефона:"
    )
    await RegistrationStates.next()


async def load_number(message: types.Message,
                      state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ваш email:"
    )
    await RegistrationStates.next()


async def load_email(message: types.Message,
                     state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Ваш инстаграм аккаунт:"
    )
    await RegistrationStates.next()


async def load_instagram(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as data:
        data['instagram'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="Отправьте ваше фото"
    )
    await RegistrationStates.next()


async def load_photo(message: types.Message,
                     state: FSMContext):
    db = Database()
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=MEDIA_DESTINATION
    )
    print(path.name)
    async with state.proxy() as data:
        try:
            db.sql_insert_profile(
                tg_id=message.from_user.id,
                nickname=data['nickname'],
                biography=data['biography'],
                age=data['age'],
                hobby=data['hobby'],
                number=data['number'],
                email=data['email'],
                instagram=data['instagram'],
                photo=path.name
            )
        except sqlite3.IntegrityError:
            await message.reply(
                text='Вы раньше регистрирвались!!!'
            )
            return
        with open(path.name, 'rb') as photo:
            await bot.send_photo(
                chat_id=message.from_user.id,
                photo=photo,
                caption=PROFILE_TEXT.format(
                    nickname=data['nickname'],
                    biography=data['biography'],
                    age=data['age'],
                    hobby=data['hobby'],
                    number=data['number'],
                    email=data['email'],
                    instagram=data['instagram']
                ),
                parse_mode=types.ParseMode.MARKDOWN
            )
        await bot.send_message(
            chat_id=message.from_user.id,
            text='Вы успешно зарегистретировались на пробный урок🤩Мы вас ждем!!!',
            reply_markup=await inline_buttons.survey_keyboard()
        )
        await state.finish()


def register_registration_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registration"
    )
    dp.register_callback_query_handler(
        registration_start,
        lambda call: call.data == "registr"
    )
    dp.register_message_handler(
        load_nickname,
        state=RegistrationStates.nickname,
        content_types=['text']
    )
    dp.register_message_handler(
        load_biography,
        state=RegistrationStates.biography,
        content_types=['text']
    )
    dp.register_message_handler(
        load_age,
        state=RegistrationStates.age,
        content_types=['text']
    )
    dp.register_message_handler(
        load_hobby,
        state=RegistrationStates.hobby,
        content_types=['text']
    )
    dp.register_message_handler(
        load_number,
        state=RegistrationStates.number,
        content_types=['text']
    )
    dp.register_message_handler(
        load_email,
        state=RegistrationStates.email,
        content_types=['text']
    )
    dp.register_message_handler(
        load_instagram,
        state=RegistrationStates.instagram,
        content_types=['text']
    )
    dp.register_message_handler(
        load_photo,
        state=RegistrationStates.photo,
        content_types=types.ContentTypes.PHOTO
    )


class SurveyStates(StatesGroup):
    problems = State()
    idea = State()


async def survey_start(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Какие у вас были проблемы при регистрации?\n"
             "Какие недостатки заметили в боте?"
    )
    await SurveyStates.problems.set()


async def load_problems(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['problems'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text="У вас какие идеи есть для улучшения бота:"
    )
    await SurveyStates.next()


async def load_idea(message: types.Message,
                    state: FSMContext):
    db = Database()
    async with state.proxy() as data:
        data['idea'] = message.text
        print(data)

    await bot.send_message(
        chat_id=message.from_user.id,
        text='Благодарим за ваш отзыв!!!'
    )

    async with state.proxy() as data:
        db.sql_insert_survey(
            tg_id=message.from_user.id,
            problems=data['problems'],
            idea=data['idea']
        )
    await state.finish()


def survey_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(
        survey_start,
        lambda call: call.data == "review"
    )
    dp.register_message_handler(
        load_problems,
        state=SurveyStates.problems,
        content_types=['text']
    )
    dp.register_message_handler(
        load_idea,
        state=SurveyStates.idea,
        content_types=['text']
    )
