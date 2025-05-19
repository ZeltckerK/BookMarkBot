'''
Здесь будет основная логика работы базы данных - остальная(локальная) в хэндлерах
'''

import aiosqlite

DB_NAME = 'libraryBot.db'

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db: # подключается или создает новую
        await db.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        joined_at TEXT
        )
    ''')

        await db.execute('''
        CREATE TEBLE IF NOT EXISTS bookmark (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        title TEXT,
        url TEXT,
        created_at TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''') # FOREIGN KEY(user_id) REFERENCES users(id) - связывает id конкретного пользователя из bookmark с users
         # (то есть пользователь должен быть зарегестиррован)

        await db.commit() 