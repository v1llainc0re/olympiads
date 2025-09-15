import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "../olympiads.db")


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # --- Создание таблиц ---
        cursor.executescript('''
            CREATE TABLE IF NOT EXISTS olympiads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                year INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS participations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT NOT NULL,
                olympiad_id INTEGER,
                score REAL,
                result TEXT,
                FOREIGN KEY (olympiad_id) REFERENCES olympiads(id)
            );

            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                olympiad_id INTEGER,
                file_type TEXT NOT NULL,
                file_path TEXT NOT NULL,
                year INTEGER,
                FOREIGN KEY (olympiad_id) REFERENCES olympiads(id)
            );
        ''')

        # --- Проверка и добавление колонки student_name, если её нет ---
        cursor.execute("PRAGMA table_info(participations)")
        columns = [t[1] for t in cursor.fetchall()]  # Получаем список имён колонок
        if 'student_name' not in columns:
            cursor.execute("ALTER TABLE participations ADD COLUMN student_name TEXT")
            print("Колонка 'student_name' добавлена в таблицу 'participations'")

        # --- Сохранение изменений ---
        conn.commit()
        print("База данных инициализирована")

    except sqlite3.Error as e:
        print(f"Ошибка при инициализации БД: {e}")
    finally:
        conn.close()