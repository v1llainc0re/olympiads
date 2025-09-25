class User:
    def __init__(self, id, login, full_name, role):
        self.id = id
        self.login = login
        self.full_name = full_name
        self.role = role

    def is_student(self):
        return self.role == 'student'

    def is_teacher(self):
        return self.role == 'teacher'

    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return f"User(id={self.id}, login='{self.login}', full_name='{self.full_name}', role='{self.role}')"