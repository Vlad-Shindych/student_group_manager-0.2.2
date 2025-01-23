import json
from models.student import Student
from utils.file_manager import FileManager


class StudentController:
    """Контроллер для управления студентами.

    Этот класс позволяет создавать, удалять и загружать студентов, а также сохранять их в файл.
    """

    def __init__(self):
        """Инициализирует контроллер с пустым списком студентов."""
        self.students = []  # Список студентов

    def create_student(self, student):
        """Создает студента и добавляет его в список.

        Args:
            student (Student): Экземпляр студента для добавления.
        """
        self.students.append(student)  # Добавляем студента в список

    def delete_student(self, student):
        """Удаляет студента из списка.

        Args:
            student (Student): Экземпляр студента для удаления.
        """
        self.students.remove(student)  # Удаляем студента из списка

    def list_students(self):
        """Возвращает список имен студентов.

        Returns:
            list: Список имен студентов.
        """
        return [student.name for student in self.students]  # Возвращаем имена всех студентов

    def save_groups(self, filename):
        """Сохраняет группы в JSON файл (не используется в этом классе).

        Args:
            filename (str): Имя файла для сохранения.
        """
        # Данный метод не должен находиться в этом классе, его следует удалить или переместить в GroupController.
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([group.name for group in self.groups], f, ensure_ascii=False)

    def save_students(self, filename):
        """Сохраняет студентов в JSON файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([student.name for student in self.students], file, ensure_ascii=False)  # Сохраняем имена студентов в файл

    def load_students(self, filename):
        """Загружает студентов из JSON файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            student_names = json.load(file)  # Загружаем имена студентов из файла
            self.students = [Student(name) for name in student_names]  # Создаем экземпляры студентов по загруженным именам