from sqlmodel import select
from models.models import User
from utils.security import verify_password, hash_password
from db.database import get_session

def create_user(login: str, password: str, full_name: str, role: str = 'student'):
    try:
        with get_session() as session:
            password_hash = hash_password(password)
            user = User(login=login, password_hash=password_hash, full_name=full_name, role=role)
            session.add(user)
            session.commit()
            session.refresh(user)
            print(f"Пользователь '{full_name}' создан.")
            return user
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def authenticate_user(login: str, password: str):
    try:
        with get_session() as session:
            statement = select(User).where(User.login == login)
            user = session.exec(statement).first()
            if user and verify_password(password, user.password_hash):
                return user
            return None
    except Exception as e:
        print(f"Ошибка при входе: {e}")
        return None