CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""

СREATE_BAN_USER_TABLE_QUERY = """ 
CREATE TABLE IF NOT EXISTS ban_user
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""


СREATE_DISLIKE_TABLE_QUERY = """ 
CREATE TABLE IF NOT EXISTS dislike_profile
(
ID INTEGER PRIMARY KEY,
OWNER_TELEGRAM_ID INTEGER,
DISLIKER_TELEGRAM_ID INTEGER,
UNIQUE (OWNER_TELEGRAM_ID, DISLIKER_TELEGRAM_ID)
)
"""



CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIOGRAPHY TEXT,
AGE INTEGER,
HOBBY TEXT,
CALL_NUMBER INTEGER,
EMAIL CHAR(50),
INSTRAGAM CHAR(50),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""


CREATE_SURVEY_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS survey
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
PROBLEMS TEXT,
IDEA TEXT
)
"""


INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""


INSERT_NEW_BAN_USER_QUERY = """
INSERT INTO ban_user VALUES (?,?,?)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profile VALUES (?,?,?,?,?,?,?,?,?,?)
"""

INSERT_SURVEY_QUERY = """
INSERT OR IGNORE INTO survey VALUES (?,?,?,?)
"""



FILTER_LEFT_JOIN_PROFILE_LIKE_QUERY = """
SELECT * FROM profile
LEFT JOIN like_profile ON profile.TELEGRAM_ID = like_profile.OWNER_TELEGRAM_ID
AND like_profile.LIKER_TELEGRAM_ID = ?
WHERE like_profile.ID IS NULL
AND profile.TELEGRAM_ID != ?
"""

INSERT_DISLIKE_QUERY = """
INSERT INTO dislike_profile VALUES (?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_user WHERE TELEGRAM_ID = ?
"""


SELECT_PROFILE_QUERY = """
SELECT * FROM profile WHERE TELEGRAM_ID = ?
"""


UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_user SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""

SELECT_USER_QUERY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

