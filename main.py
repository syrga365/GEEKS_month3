from aiogram import executor
from config import dp
from handlers import (
    start,
    offenders,
    questionnaire,
    chat_actions,
    registration,
    comment,
    profile,
    complain,
    referens,
    # anime

)
from database import sql_commands


async def on_startup(_):
    db = sql_commands.Database()
    db.sql_create_tables()


start.register_start_handlers(dp=dp)
offenders.register_offenders_handlers(dp=dp)
comment.register_comment_handlers(dp=dp)
questionnaire.register_questionnaire_handlers(dp=dp)
registration.register_registration_handlers(dp=dp)
profile.register_profile_handlers(dp=dp)
registration.survey_handlers(dp=dp)
referens.register_reference_handlers(dp=dp)
# anime.register_anime_handlers(dp=dp)
complain.register_complain_handlers(dp=dp)

# chat_actions.register_chat_actions_handlers(dp=dp)

if __name__ == "__main__":
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=on_startup
    )


