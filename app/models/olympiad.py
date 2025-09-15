class Olympiad:
    """
    Модель олимпиады или конкурса профессионального мастерства.
    """

    def __init__(self, id, title, year, start_date, end_date,
                 description=None, responsible_teacher_id=None, status='draft'):
        """
        :param id: Уникальный идентификатор олимпиады (None для новой)
        :param title: Название олимпиады
        :param year: Год проведения
        :param start_date: Дата начала (в формате 'YYYY-MM-DD')
        :param end_date: Дата окончания
        :param description: Описание олимпиады (опционально)
        :param responsible_teacher_id: ID преподавателя, ответственного за олимпиаду
        :param status: Статус: 'draft', 'prepared', 'published'
        """
        self.id = id
        self.title = title
        self.year = year
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.responsible_teacher_id = responsible_teacher_id
        self.status = status  # draft, prepared, published

    def __repr__(self):
        return (f"Olympiad(id={self.id}, "
                f"title='{self.title}', "
                f"year={self.year}, "
                f"period='{self.start_date}' — '{self.end_date}', "
                f"teacher_id={self.responsible_teacher_id}, "
                f"status='{self.status}')")