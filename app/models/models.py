from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date

class User(SQLModel, table=True):
    __tablename__ = "user"  # Таблица теперь называется "user" (единственное число)
    
    id: Optional[int] = Field(default=None, primary_key=True)
    login: str = Field(index=True, unique=True)
    password_hash: str
    full_name: str
    role: str  # 'student', 'teacher', 'admin'

    def is_student(self):
        return self.role == 'student'

    def is_teacher(self):
        return self.role == 'teacher'

    def is_admin(self):
        return self.role == 'admin'

class Olympiad(SQLModel, table=True):
    __tablename__ = "olympiad"  # Таблица теперь называется "olympiad"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    year: int
    start_date: date
    end_date: date

class Participation(SQLModel, table=True):
    __tablename__ = "participation"  # Таблица теперь называется "participation"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    student_name: str
    olympiad_id: int = Field(foreign_key="olympiad.id")  # Исправлено на "olympiad.id"

class File(SQLModel, table=True):
    __tablename__ = "file"  # Таблица теперь называется "file"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    olympiad_id: int = Field(foreign_key="olympiad.id")  # Исправлено на "olympiad.id"
    file_type: str  # 'regulation', 'task'
    file_path: str
    year: Optional[int] = None