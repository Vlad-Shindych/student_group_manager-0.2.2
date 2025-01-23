from models.student import Student


class StudentCreator:
    """Создатель студентов.

    Этот класс отвечает за создание студентов с заданными именами.
    """

    @staticmethod
    def create(name):
        """Создает студента с заданным именем.

        Args:
            name (str): Имя студента.

        Returns:
            Student: Экземпляр созданного студента.
        """
        return Student(name)  # Создаем и возвращаем объект Student с заданным именем