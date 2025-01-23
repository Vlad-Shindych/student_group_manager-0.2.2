import copy


class Group:
    """Класс для представления группы студентов."""

    def __init__(self, name):
        """Инициализирует группу с заданным именем и пустым списком студентов."""
        self.name = name
        self.students = []

    def add_student(self, student):
        """Добавляет студента в группу."""
        self.students.append(student)

    def remove_student(self, student):
        """Удаляет студента из группы."""
        self.students.remove(student)

    def list_students(self):
        """Возвращает список студентов в группе."""
        return [str(student) for student in self.students]

    def __str__(self):
        """Строковое представление группы."""
        return self.name

    def clone(self):
        """Клонирует группу с новым именем."""
        cloned_group = copy.deepcopy(self)
        cloned_group.name += " - Клон"  # Изменение имени для клона
        return cloned_group