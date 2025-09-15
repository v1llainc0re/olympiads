from db.database import init_db
from views.menu_view import show_main_menu
from views.olympiad_view import show_olympiads, show_olympiad_details
from views.participation_view import show_participants
from controllers import olympiad_controller, participation_controller


def main():
    init_db()

    print("=== Система учёта олимпиад ===")

    while True:
        show_main_menu()
        choice = input("\nВыберите действие: ").strip()

        # 1. Просмотр всех олимпиад
        if choice == "1":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)

        # 2. Добавить олимпиаду
        elif choice == "2":
            print("\n--- Добавление олимпиады ---")
            title = input("Название: ").strip()
            year = input("Год: ").strip()
            start_date = input("Дата начала (ГГГГ-ММ-ДД): ").strip()
            end_date = input("Дата окончания (ГГГГ-ММ-ДД): ").strip()

            if all([title, year.isdigit(), start_date, end_date]):
                olympiad_controller.add_olympiad(title, int(year), start_date, end_date)
            else:
                print("Все поля обязательны, год должен быть числом.")

        # 3. Просмотр деталей олимпиады
        elif choice == "3":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)
            try:
                olympiad_id = int(input("ID олимпиады: "))
                olympiad = olympiad_controller.get_olympiad_by_id(olympiad_id)
                if olympiad:
                    show_olympiad_details(olympiad)
                else:
                    print("Олимпиада не найдена.")
            except ValueError:
                print("Введите число.")

        # 4. Добавить участника
        elif choice == "4":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)
            try:
                olympiad_id = int(input("ID олимпиады: "))
                olympiad = olympiad_controller.get_olympiad_by_id(olympiad_id)
                if not olympiad:
                    print("Олимпиада не найдена.")
                else:
                    name = input("ФИО участника: ").strip()
                    if not name:
                        print("Имя не может быть пустым.")
                    else:
                        participation_controller.add_participant(name, olympiad_id)
            except ValueError:
                print("Введите корректный ID.")

        # 5. Просмотр участников олимпиады
        elif choice == "5":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)
            try:
                olympiad_id = int(input("ID олимпиады: "))
                participants = participation_controller.get_participants_by_olympiad(olympiad_id)
                show_participants(olympiad_id, participants)
            except ValueError:
                print("Введите число.")

        # 6. Добавить положение
        elif choice == "6":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)
            try:
                olympiad_id = int(input("ID олимпиады: "))
                path = input("Путь к файлу положения: ").strip()
                if path:
                    olympiad_controller.add_regulation(olympiad_id, path)
                else:
                    print("Укажите путь.")
            except ValueError:
                print("Введите число.")

        # 7. Добавить задания прошлых лет
        elif choice == "7":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)
            try:
                olympiad_id = int(input("ID олимпиады: "))
                year = input("Год заданий: ").strip()
                path = input("Путь к файлу: ").strip()
                if year.isdigit() and path:
                    olympiad_controller.add_task(olympiad_id, int(year), path)
                else:
                    print("Год должен быть числом, путь — не пустым.")
            except ValueError:
                print("Некорректный ввод.")

        # 8. Просмотр файлов
        elif choice == "8":
            olympiad_controller.show_all_files()

        # 9. Изменить название олимпиады
        elif choice == "9":
            olympiads = olympiad_controller.get_all_olympiads()
            show_olympiads(olympiads)
            try:
                olympiad_id = int(input("Введите ID олимпиады для изменения названия: "))
                new_title = input("Новое название: ").strip()
                if new_title:
                    olympiad_controller.update_olympiad_title(olympiad_id, new_title)
                else:
                    print("Название не может быть пустым.")
            except ValueError:
                print("Введите корректный ID.")

        # 10. Удалить участника
        elif choice == "10":
            olympiad_id = int(input("Введите ID олимпиады: "))
            participants = participation_controller.get_participants_by_olympiad(olympiad_id)
            show_participants(olympiad_id, participants)
            try:
                participant_id = int(input("Введите ID участника для удаления: "))
                confirm = input(f"Вы уверены, что хотите удалить участника ID={participant_id}? (да/нет): ")
                if confirm.lower() in ['да', 'д', 'yes', 'y']:
                    participation_controller.delete_participant(participant_id)
            except ValueError:
                print("Введите корректный ID.")

        # 0. Выход
        elif choice == "0":
            print("--- Завершение программы ---")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()