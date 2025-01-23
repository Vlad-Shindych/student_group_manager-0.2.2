from models.student import Student


class StudentFactory:
    """Фабрика для создания студентов.

    Этот класс отвечает за создание экземпляров студентов с заданными именами.
    """

    @staticmethod
    def create_student(name):
        """Создает нового студента с заданным именем.

        Args:
            name (str): Имя студента.

        Returns:
            Student: Экземпляр созданного студента.
        """
        return Student(name)  # Создаем и возвращаем объект Student с заданным именем