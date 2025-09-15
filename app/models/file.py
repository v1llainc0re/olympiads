class File:
    """
    Модель файла: положение, задание, шаблон сертификата и т.п.
    """

    def __init__(self, id, olympiad_id, file_type, file_path, year=None, uploaded_at=None):
        """
        :param id: Уникальный идентификатор файла
        :param olympiad_id: ID олимпиады (может быть None для общих шаблонов)
        :param file_type: Тип файла: 'regulation', 'task', 'certificate', 'diploma'
        :param file_path: Путь к файлу на диске
        :param year: Год (актуально для заданий прошлых лет)
        :param uploaded_at: Дата загрузки
        """
        self.id = id
        self.olympiad_id = olympiad_id
        self.file_type = file_type
        self.file_path = file_path
        self.year = year
        self.uploaded_at = uploaded_at

    def __repr__(self):
        return (f"File(id={self.id}, "
                f"olympiad_id={self.olympiad_id}, "
                f"type='{self.file_type}', "
                f"path='{self.file_path}', "
                f"year={self.year}, "
                f"uploaded_at='{self.uploaded_at}')")