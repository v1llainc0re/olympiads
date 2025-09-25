from models.models import File, User
from utils.security import hash_password
from db.database import get_session
from controllers.olympiad_controller import get_olympiad_by_id, show_all_files as get_files
from controllers.participation_controller import get_participants_by_olympiad, add_participant
from views.olympiad_view import show_olympiad_details
from views.participation_view import show_participants

def view_olympiad_details(olympiad_id: int):
    olympiad = get_olympiad_by_id(olympiad_id)
    if olympiad:
        show_olympiad_details(olympiad)
        return True
    else:
        print("Олимпиада не найдена.")
        return False

def register_for_olympiad(student_full_name: str, olympiad_id: int):
    olympiad = get_olympiad_by_id(olympiad_id)
    if not olympiad:
        print("Олимпиада не найдена.")
        return False

    return add_participant(student_full_name, olympiad_id)

def add_regulation(olympiad_id: int, file_path: str):
    olympiad = get_olympiad_by_id(olympiad_id)
    if not olympiad:
        print("Олимпиада не найдена.")
        return False

    try:
        with get_session() as session:
            file = File(olympiad_id=olympiad_id, file_type='regulation', file_path=file_path)
            session.add(file)
            session.commit()
            print(f"Положение добавлено для олимпиады ID={olympiad_id}.")
            return True
    except Exception as e:
        print(f"Ошибка при добавлении положения: {e}")
        return False

def view_participants(olympiad_id: int):
    participants = get_participants_by_olympiad(olympiad_id)
    show_participants(olympiad_id, participants)

def create_user(login: str, full_name: str, role: str, password: str):
    if role not in ['student', 'teacher', 'admin']:
        print("Неверная роль.")
        return False
    if not password:
        print("Пароль не может быть пустым.")
        return False

    from controllers.user_controller import create_user as create_user_func
    user = create_user_func(login, password, full_name, role)
    return user is not None

def delete_olympiad(olympiad_id: int):
    olympiad = get_olympiad_by_id(olympiad_id)
    if not olympiad:
        print("Олимпиада не найдена.")
        return False

    confirm = input(f"Удалить олимпиаду '{olympiad.title}'? (да/нет): ").strip().lower()
    if confirm not in ['да', 'д', 'yes', 'y']:
        print("Отменено.")
        return False

    from controllers.olympiad_controller import delete_olympiad as delete_olympiad_func
    result = delete_olympiad_func(olympiad_id)
    print(result["message"])
    return result["success"]

def show_all_files():
    get_files()