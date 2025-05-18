from sqlite3 import *


def creare_db():
    con = connect("users.db")
    create = con.execute(
        """
    CREATE TABLE IF NOT EXISTS user_data(
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        chat_id TEXT

    )
"""
    )



def creare_db_message():
    con = connect("message.db")
    create = con.execute(
        """
    CREATE TABLE IF NOT EXISTS message_data(
        id INTEGER PRIMARY KEY,
        text TEXT,
        message_id TEXT,
        chat_id TEXT

    )
"""
    )

























































































































































