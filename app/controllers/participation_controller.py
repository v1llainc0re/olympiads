from sqlmodel import select
from models.models import Participation
from db.database import get_session

def get_participants_by_olympiad(olympiad_id: int):
    try:
        with get_session() as session:
            statement = select(Participation).where(Participation.olympiad_id == olympiad_id)
            participants = session.exec(statement).all()
            return participants
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

def add_participant(student_name: str, olympiad_id: int):
    try:
        with get_session() as session:
            participation = Participation(student_name=student_name, olympiad_id=olympiad_id)
            session.add(participation)
            session.commit()
            session.refresh(participation)
            print(f"Участник '{student_name}' добавлен.")
            return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False