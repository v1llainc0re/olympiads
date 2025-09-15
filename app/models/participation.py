class Participation:
    """
    Модель участия студента в олимпиаде.
    Содержит информацию о регистрации, результатах и статусе протокола.
    """

    def __init__(self, id, student_id, olympiad_id,
                 registered_at, score=None, result=None,
                 status='draft', submitted_by=None, submitted_at=None):
        """
        :param id: Уникальный идентификатор участия
        :param student_id: ID студента
        :param olympiad_id: ID олимпиады
        :param registered_at: Дата и время регистрации
        :param score: Набранные баллы (может быть None)
        :param result: Результат: 'участник', 'призёр', 'победитель'
        :param status: Статус записи: 'draft', 'prepared', 'published'
        :param submitted_by: ID преподавателя, внесшего результаты
        :param submitted_at: Время внесения результатов
        """
        self.id = id
        self.student_id = student_id
        self.olympiad_id = olympiad_id
        self.registered_at = registered_at
        self.score = score
        self.result = result
        self.status = status  # draft, prepared, published
        self.submitted_by = submitted_by
        self.submitted_at = submitted_at

    def __repr__(self):
        return (f"Participation(id={self.id}, "
                f"student_id={self.student_id}, "
                f"olympiad_id={self.olympiad_id}, "
                f"score={self.score}, "
                f"result='{self.result}', "
                f"status='{self.status}', "
                f"submitted_at='{self.submitted_at}')")