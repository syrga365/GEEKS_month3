import sqlite3
from database import sql_queries


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('geeks.db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create_tables(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.СREATE_BAN_USER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_PROFILE_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_SURVEY_TABLE_QUERY)
        self.connection.execute(sql_queries.СREATE_LIKE_TABLE_QUERY)
        self.connection.execute(sql_queries.СREATE_HATER_TABLE_QUERY)
        self.connection.execute(sql_queries.CREATE_REFERRAL_USERS_TABLE_QUERY)
        try:
            self.connection.execute(sql_queries.ALTER_USER_TABLE)
            self.connection.execute(sql_queries.ALTER_REFERRAL_NAME_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.commit()

    def sql_insert_user(self, tg_id, username, first_name, last_name):
        self.cursor.execute(
            sql_queries.INSERT_USER_QUERY,
            (None, tg_id, username, first_name, last_name, None)
        )
        self.connection.commit()

    def sql_insert_new_ban_user(self, tg_id):
        self.cursor.execute(
            sql_queries.INSERT_NEW_BAN_USER_QUERY,
            (None, tg_id, 1)
        )
        self.connection.commit()

    def sql_select_ban_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "count": row[2]
        }
        return self.cursor.execute(
            sql_queries.SELECT_BAN_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_update_ban_user_count(self, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_BAN_USER_COUNT_QUERY,
            (tg_id,)
        )
        self.connection.commit()

    def sql_insert_profile(self, tg_id, nickname, biography, age, hobby, number, email, instagram, photo):
        self.cursor.execute(
            sql_queries.INSERT_PROFILE_QUERY,
            (None, tg_id, nickname, biography, age, hobby, number, email, instagram, photo)
        )
        self.connection.commit()

    def sql_select_profile(self, tg_id):
        query = "SELECT * FROM profile WHERE telegram_id = ?"
        self.cursor.execute(query, (tg_id,))
        user = self.cursor.fetchone()
        return user

    def sql_select_profile_users(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "hobby": row[5],
            "call_number": row[6],
            "email": row[7],
            "instagram": row[8],
            "photo": row[9]

        }
        return self.cursor.execute(
            sql_queries.SELECT_PROFILE_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_insert_survey(self, tg_id, problems, idea):
        self.cursor.execute(
            sql_queries.INSERT_SURVEY_QUERY,
            (None, tg_id, problems, idea)
        )
        self.connection.commit()

    def sql_select_filter_profiles(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "biography": row[3],
            "age": row[4],
            "hobby": row[5],
            "call_number": row[6],
            "email": row[7],
            "instagram": row[8],
            "photo": row[9]

        }
        return self.cursor.execute(
            sql_queries.FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY,
            (tg_id, tg_id,)
        ).fetchall()

    def sql_insert_like(self, owner, liker):
        self.cursor.execute(
            sql_queries.INSERT_LIKE_QUERY,
            (None, owner, liker,)
        )
        self.connection.commit()

    def sql_insert_hater(self, owner, hater):
        self.cursor.execute(
            sql_queries.INSERT_HATER_QUERY,
            (None, owner, hater,)
        )
        self.connection.commit()

    def sql_update_user_link(self, link, tg_id):
        self.cursor.execute(
            sql_queries.UPDATE_USER_LINK_QUERY,
            (link, tg_id,)
        )
        self.connection.commit()

    def sql_select_user(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "user_name": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
        }

        return self.cursor.execute(
            sql_queries.SELECT_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def reference_menu_data(self, tg_id):
        self.cursor.row_factory = lambda cursor, row: {
            "total_referral": row[0]
        }
        return self.cursor.execute(
            sql_queries.DOUBLE_SELECT_REFERRAL_USER_QUERY,
            (tg_id,)
        ).fetchone()

    def sql_select_user_by_link(self, link):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "user_name": row[2],
            "first_name": row[3],
            "last_name": row[4],
            "link": row[5],
        }

        return self.cursor.execute(
            sql_queries.SELECT_USER_BY_LINK_QUERY,
            (link,)
        ).fetchone()

    def sql_insert_referral_users(self, owner_id, referral_id, referral_name):
        self.cursor.execute(
            sql_queries.INSERT_REFERRAL_USERS_QUERY,
            (None, owner_id, referral_id, referral_name)
        )
        self.connection.commit()

    def sql_select_referral_user(self, referral_first_name):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "owner_telegram_id": row[1],
            "referral_telegram_id": row[2],
            "referral_first_name": row[3],
        }

        return self.cursor.execute(
            sql_queries.SELECT_REFERRAL_QUERY,
            (referral_first_name,)
        ).fetchall()


