from models.student import Student


class StudentFactory:
    """Фабрика для создания студентов."""

    @staticmethod
    def create_student(name):
        """Создает нового студента с заданным именем."""
        return Student(name)