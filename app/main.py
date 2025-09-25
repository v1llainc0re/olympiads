from db.database import engine, get_session
from views.auth_view import login_view
from views.menu_view import show_main_menu
from controllers.olympiad_controller import get_all_olympiads
from views.olympiad_view import show_olympiads
from controllers.action_controller import (
    view_olympiad_details,
    register_for_olympiad,
    add_regulation,
    view_participants,
    create_user,
    delete_olympiad,
    show_all_files,
)
from controllers.olympiad_controller import add_olympiad

def main():
    if not engine:
        print("Не удалось подключиться к БД.")
        return

    print("=== Система учёта олимпиад ===")

    user = login_view()
    if not user:
        print("Вход не выполнен.")
        return

    while True:
        show_main_menu(user.role)
        choice = input("\nВыберите действие: ").strip()

        if choice == "0":
            print("До новых встреч!")
            break

        elif choice == "1":
            olympiads = get_all_olympiads()
            show_olympiads(olympiads)

        # --- Студент ---
        elif user.is_student():
            if choice == "2":
                try:
                    olympiad_id = int(input("ID олимпиады: "))
                    view_olympiad_details(olympiad_id)
                except ValueError:
                    print("Введите число.")
            elif choice == "3":
                try:
                    olympiad_id = int(input("ID олимпиады: "))
                    success = register_for_olympiad(user.full_name, olympiad_id)
                    if success:
                        print("Вы успешно зарегистрированы.")
                except ValueError:
                    print("Введите число.")
            elif choice == "4":
                print("Ваши результаты пока не доступны.")
            else:
                print("Неверный выбор.")

        # --- Преподаватель ---
        elif user.role == 'teacher':
            if choice == "2":
                try:
                    olympiad_id = int(input("ID олимпиады: "))
                    view_olympiad_details(olympiad_id)
                except ValueError:
                    print("Введите число.")
            elif choice == "3":
                try:
                    olympiad_id = int(input("ID олимпиады: "))
                    file_path = input("Путь к файлу положения: ").strip()
                    if file_path:
                        success = add_regulation(olympiad_id, file_path)
                        if success:
                            print("Положение добавлено.")
                    else:
                        print("Укажите путь.")
                except ValueError:
                    print("Введите корректный ID.")
            elif choice == "4":
                print("Ввод результатов пока не реализован.")
            elif choice == "5":
                try:
                    olympiad_id = int(input("ID олимпиады: "))
                    view_participants(olympiad_id)
                except ValueError:
                    print("Введите число.")
            else:
                print("Неверный выбор.")

        # --- Администратор ---
        elif user.is_admin():
            if choice == "2":
                title = input("Название: ").strip()
                try:
                    year = int(input("Год: "))
                except ValueError:
                    print("Год должен быть числом.")
                    continue
                start_date = input("Дата начала (ГГГГ-ММ-ДД): ").strip()
                end_date = input("Дата окончания (ГГГГ-ММ-ДД): ").strip()
                result = add_olympiad(title, year, start_date, end_date)
                print(result["message"])
            elif choice == "3":
                login = input("Логин: ").strip()
                full_name = input("ФИО: ").strip()
                role = input("Роль (student/teacher/admin): ").strip().lower()
                password = input("Пароль: ").strip()
                create_user(login, full_name, role, password)
            elif choice == "4":
                try:
                    olympiad_id = int(input("ID олимпиады для удаления: "))
                    delete_olympiad(olympiad_id)
                except ValueError:
                    print("Введите число.")
            elif choice == "5":
                show_all_files()
            else:
                print("Неверный выбор.")
        else:
            print("Неизвестная роль.")

if __name__ == "__main__":
    main()