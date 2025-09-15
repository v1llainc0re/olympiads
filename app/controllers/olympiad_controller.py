from db.database import get_connection


def add_olympiad(title, year, start_date, end_date):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO olympiads (title, year, start_date, end_date)
            VALUES (?, ?, ?, ?)
        """, (title, year, start_date, end_date))
        conn.commit()
        print(f"Олимпиада '{title}' добавлена.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()


def get_all_olympiads():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, year, start_date, end_date FROM olympiads ORDER BY year DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_olympiad_by_id(olympiad_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, year, start_date, end_date FROM olympiads WHERE id = ?", (olympiad_id,))
    row = cursor.fetchone()
    conn.close()
    return row


def add_regulation(olympiad_id, file_path):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO files (olympiad_id, file_type, file_path)
            VALUES (?, 'regulation', ?)
        """, (olympiad_id, file_path))
        conn.commit()
        print("Положение добавлено.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()


def add_task(olympiad_id, year, file_path):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO files (olympiad_id, file_type, file_path, year)
            VALUES (?, 'task', ?, ?)
        """, (olympiad_id, file_path, year))
        conn.commit()
        print("Задания добавлены.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()


def show_all_files():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.title, f.file_type, f.file_path, f.year
        FROM files f
        LEFT JOIN olympiads o ON f.olympiad_id = o.id
        ORDER BY o.year DESC
    """)
    files = cursor.fetchall()
    conn.close()

    if not files:
        print("Нет загруженных файлов.")
        return

    print("\nФАЙЛЫ")
    for f in files:
        year_info = f" ({f['year']} г.)" if f['year'] else ""
        print(f"• {f['title']} — {f['file_type']}{year_info}: {f['file_path']}")

def update_olympiad_title(olympiad_id, new_title):
    """
    Изменяет название олимпиады по ID.
    :param olympiad_id: ID олимпиады
    :param new_title: Новое название
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            UPDATE olympiads 
            SET title = ? 
            WHERE id = ?
        """, (new_title, olympiad_id))
        
        if cursor.rowcount == 0:
            print("Олимпиада с таким ID не найдена.")
        else:
            conn.commit()
            print(f"Название олимпиады изменено на: '{new_title}'")
            
    except Exception as e:
        print(f"Ошибка при обновлении: {e}")
    finally:
        conn.close()