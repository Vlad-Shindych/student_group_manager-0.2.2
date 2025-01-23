from models.student import Student


class StudentCreator:
    """Создатель студентов."""

    @staticmethod
    def create(name):
        """Создает студента с заданным именем."""
        return Student(name)