import json

from models.student import Student
from utils.file_manager import FileManager


class StudentController:
    """Контроллер для управления студентами."""

    def __init__(self):
        """Инициализирует контроллер с пустым списком студентов."""
        self.students = []

    def create_student(self, student):
        """Создает студента и добавляет его в список."""
        self.students.append(student)

    def delete_student(self, student):
        """Удаляет студента."""
        self.students.remove(student)

    def list_students(self):
        """Возвращает список студентов."""
        return [student.name for student in self.students]

    def save_groups(self, filename):
        """Сохраняет группы в JSON файл."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([group.name for group in self.groups], f, ensure_ascii=False)

    def save_students(self, filename):
        """Сохраняет студентов в файл."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([student.name for student in self.students], file, ensure_ascii=False)

    def load_students(self, filename):
        """Загружает студентов из файла."""
        with open(filename, 'r', encoding='utf-8') as file:
            student_names = json.load(file)
            self.students = [Student(name) for name in student_names]
