from sqlmodel import select
from models.models import Olympiad, File
from db.database import get_session

def add_olympiad(title: str, year: int, start_date: str, end_date: str):
    if not title:
        return {"success": False, "message": "Название не может быть пустым."}
    
    try:
        with get_session() as session:
            olympiad = Olympiad(
                title=title, 
                year=year, 
                start_date=start_date, 
                end_date=end_date
            )
            session.add(olympiad)
            session.commit()
            session.refresh(olympiad)
            return {"success": True, "message": f"Олимпиада '{title}' добавлена."}
    except Exception as e:
        return {"success": False, "message": f"Ошибка БД: {e}"}

def get_all_olympiads():
    try:
        with get_session() as session:
            statement = select(Olympiad).order_by(Olympiad.year.desc(), Olympiad.start_date)
            olympiads = session.exec(statement).all()
            return olympiads
    except Exception as e:
        print(f"Ошибка загрузки олимпиад: {e}")
        return []

def get_olympiad_by_id(olympiad_id: int):
    try:
        with get_session() as session:
            statement = select(Olympiad).where(Olympiad.id == olympiad_id)
            return session.exec(statement).first()
    except Exception as e:
        print(f"Ошибка: {e}")
        return None

def delete_olympiad(olympiad_id: int):
    try:
        with get_session() as session:
            statement = select(Olympiad).where(Olympiad.id == olympiad_id)
            olympiad = session.exec(statement).first()
            if not olympiad:
                return {"success": False, "message": "Олимпиада не найдена."}
            
            session.delete(olympiad)
            session.commit()
            return {"success": True, "message": f"Олимпиада '{olympiad.title}' удалена."}
    except Exception as e:
        return {"success": False, "message": f"Ошибка: {e}"}

def show_all_files():
    try:
        with get_session() as session:
            statement = select(File, Olympiad).join(Olympiad).order_by(Olympiad.year.desc())
            results = session.exec(statement).all()
            
            if not results:
                print("Нет загруженных файлов.")
                return
            
            print("ФАЙЛЫ")
            for file, olympiad in results:
                year_info = f" ({file.year} г.)" if file.year else ""
                print(f"• {olympiad.title} — {file.file_type}{year_info}: {file.file_path}")
    except Exception as e:
        print(f"Ошибка: {e}")