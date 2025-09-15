from db.database import get_connection


def add_participant(student_name, olympiad_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO participations (student_name, olympiad_id)
            VALUES (?, ?)
        """, (student_name, olympiad_id))
        conn.commit()
        print(f"Участник '{student_name}' добавлен.")
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()


def get_participants_by_olympiad(olympiad_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, student_name FROM participations WHERE olympiad_id = ?
    """, (olympiad_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_participant(participant_id):
    """
    Удаляет участника по ID.
    :param participant_id: ID записи в таблице participations
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM participations WHERE id = ?", (participant_id,))
        
        if cursor.rowcount == 0:
            print("Участник с таким ID не найден.")
        else:
            conn.commit()
            print("Участник успешно удалён.")
            
    except Exception as e:
        print(f"Ошибка при удалении: {e}")
    finally:
        conn.close()