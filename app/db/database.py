from sqlmodel import Session
from config import engine, create_db_and_tables

def init_db():
    try:
        create_db_and_tables()
        print("База данных инициализирована успешно!")
        return engine
    except Exception as e:
        print(f"Ошибка инициализации базы данных: {e}")
        return None

# Создание подключения
engine = init_db()

def get_session():
    return Session(engine)