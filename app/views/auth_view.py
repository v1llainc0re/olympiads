def login_view():
    """Форма входа"""
    print("\n" + "="*50)
    print("           ВХОД В СИСТЕМУ")
    print("="*50)

    login = input("Логин: ").strip()
    if not login:
        print("Логин не может быть пустым.")
        return None

    password = input("Пароль: ").strip()
    if not password:
        print("Пароль не может быть пустым.")
        return None

    # Импорт здесь, чтобы избежать циклических импортов
    from controllers.user_controller import authenticate_user
    user = authenticate_user(login, password)

    if user:
        print(f"Добро пожаловать, {user.full_name}!")
        print(f"Роль: {user.role.upper()}")
        return user
    else:
        print("Неверный логин или пароль.")
        return None