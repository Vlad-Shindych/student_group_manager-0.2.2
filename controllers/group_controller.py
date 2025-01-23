import json
from controllers import student_controller
from decorators.student_decorator import StudentDecorator
from models.group import Group


class GroupController:
    """Контроллер для управления группами."""

    def __init__(self, student_controller):
        self.groups = []  # Список групп
        self.student_controller = student_controller  # Сохраняем экземпляр StudentController

    def create_group(self, name):
        """Создает новую группу с заданным именем."""
        group = Group(name)
        self.groups.append(group)

    def delete_group(self, group):
        """Удаляет указанную группу."""
        self.groups.remove(group)

    def list_groups(self):
        """Возвращает список названий групп."""
        return [group.name for group in self.groups]

    def get_group_by_name(self, name):
        """Находит группу по имени."""
        return next((g for g in self.groups if g.name == name), None)

    def clone_group(self, group):
        """Клонирует группу и добавляет ее в список групп."""
        cloned_group = group.clone()
        self.groups.append(cloned_group)
        return cloned_group

    def save_groups(self, filename):
        """Сохраняет группы в JSON файл."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([group.name for group in self.groups], f, ensure_ascii=False)

    def load_groups(self, filename):
        """Загружает группы из JSON файла."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                group_names = json.load(f)
                self.groups = [Group(name) for name in group_names]
        except FileNotFoundError:
            print("Файл не найден.")

    def add_student_to_group(self, student_name, group_name):
        """Добавляет студента в группу."""
        student = next((s for s in self.student_controller.students if s.name == student_name), None)
        group = next((g for g in self.groups if g.name == group_name), None)

        if student and group:
            group.add_student(student)  # Метод для добавления студента в группу
            print(f"Студент '{student_name}' добавлен в группу '{group_name}'.")
        else:
            print(f"Студент '{student_name}' или группа '{group_name}' не найдены.")

    def transfer_student(self, student_name, from_group_name, to_group_name):
        """Переводит студента из одной группы в другую."""
        from_group = self.get_group_by_name(from_group_name)
        to_group = self.get_group_by_name(to_group_name)

        if from_group and to_group:
            student = next((s for s in from_group.students if s.name == student_name), None)
            if student:
                from_group.remove_student(student)
                to_group.add_student(student)
                print(f"Студент '{student_name}' переведен из группы '{from_group_name}' в группу '{to_group_name}'.")
            else:
                print(f"Студент '{student_name}' не найден в группе '{from_group_name}'.")
        else:
            print("Одна или обе группы не найдены.")

    def list_students_in_group(self, group_name):
        """Возвращает список студентов в указанной группе."""
        group = self.get_group_by_name(group_name)
        if group:
            return group.list_students()
        else:
            return None

    def assign_monitor(self, student_name, group_name):
        """Назначает старосту в группе."""
        group = self.get_group_by_name(group_name)
        student = next((s for s in group.students if s.name == student_name), None)

        if group and student:
            # Создаем декорированного студента
            decorated_student = StudentDecorator(student)
            # Находим индекс студента в списке и заменяем его на декорированного
            student_index = group.students.index(student)
            group.students[student_index] = decorated_student  # Обновляем список студентов
            print(f"Студент '{student_name}' назначен старостой в группе '{group_name}'.")
        else:
            print("Группа или студент не найдены.")