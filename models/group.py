import copy


class Group:
    """Класс для представления группы студентов.

    Этот класс позволяет управлять группой студентов, добавлять и удалять студентов,
    а также клонировать группу.
    """

    def __init__(self, name):
        """Инициализирует группу с заданным именем и пустым списком студентов.

        Args:
            name (str): Имя группы студентов.
        """
        self.name = name  # Имя группы
        self.students = []  # Список студентов в группе

    def add_student(self, student):
        """Добавляет студента в группу.

        Args:
            student (Student): Экземпляр студента, который нужно добавить.
        """
        self.students.append(student)  # Добавляем студента в список

    def remove_student(self, student):
        """Удаляет студента из группы.

        Args:
            student (Student): Экземпляр студента, который нужно удалить.
        """
        self.students.remove(student)  # Удаляем студента из списка

    def list_students(self):
        """Возвращает список студентов в группе.

        Returns:
            list: Список строковых представлений студентов в группе.
        """
        return [str(student) for student in self.students]  # Возвращаем список студентов

    def __str__(self):
        """Строковое представление группы.

        Returns:
            str: Имя группы.
        """
        return self.name  # Возвращаем имя группы

    def clone(self):
        """Клонирует группу с новым именем.

        Returns:
            Group: Новый экземпляр группы, клонированный из существующей.
        """
        cloned_group = copy.deepcopy(self)  # Создаем глубокую копию группы
        cloned_group.name += " - Клон"  # Изменяем имя для клона
        return cloned_group  # Возвращаем клонированную группу