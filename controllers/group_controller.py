import json
from decorators.student_decorator import StudentDecorator
from models.group import Group


class GroupController:
    """Контроллер для управления группами.

    Этот класс позволяет создавать, удалять, клонировать группы, а также добавлять студентов в группы и переводить их между группами.
    """

    def __init__(self, student_controller):
        """Инициализирует контроллер с экземпляром StudentController.

        Args:
            student_controller (StudentController): Экземпляр контроллера студентов.
        """
        self.groups = []  # Список групп
        self.student_controller = student_controller  # Сохраняем экземпляр StudentController

    def create_group(self, name):
        """Создает новую группу с заданным именем.

        Args:
            name (str): Имя группы.
        """
        group = Group(name)  # Создаем экземпляр группы
        self.groups.append(group)  # Добавляем группу в список

    def delete_group(self, group):
        """Удаляет указанную группу.

        Args:
            group (Group): Группа для удаления.
        """
        self.groups.remove(group)  # Удаляем группу из списка

    def list_groups(self):
        """Возвращает список названий групп.

        Returns:
            list: Список имен групп.
        """
        return [group.name for group in self.groups]  # Возвращаем имена всех групп

    def get_group_by_name(self, name):
        """Находит группу по имени.

        Args:
            name (str): Имя группы.

        Returns:
            Group or None: Найденная группа или None, если группа не найдена.
        """
        return next((g for g in self.groups if g.name == name), None)  # Ищем группу по имени

    def clone_group(self, group):
        """Клонирует группу и добавляет ее в список групп.

        Args:
            group (Group): Группа для клонирования.

        Returns:
            Group: Клонированная группа.
        """
        cloned_group = group.clone()  # Клонируем группу
        self.groups.append(cloned_group)  # Добавляем клонированную группу в список
        return cloned_group  # Возвращаем клонированную группу

    def save_groups(self, filename):
        """Сохраняет группы в JSON файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([group.name for group in self.groups], f, ensure_ascii=False)  # Сохраняем имена групп в файл

    def load_groups(self, filename):
        """Загружает группы из JSON файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                group_names = json.load(f)  # Загружаем имена групп из файла
                self.groups = [Group(name) for name in group_names]  # Создаем группы по загруженным именам
        except FileNotFoundError:
            print("Файл не найден.")  # Обработка ошибки, если файл не найден

    def add_student_to_group(self, student_name, group_name):
        """Добавляет студента в группу.

        Args:
            student_name (str): Имя студента.
            group_name (str): Имя группы.
        """
        student = next((s for s in self.student_controller.students if s.name == student_name), None)  # Находим студента по имени
        group = next((g for g in self.groups if g.name == group_name), None)  # Находим группу по имени

        if student and group:
            group.add_student(student)  # Метод для добавления студента в группу
            print(f"Студент '{student_name}' добавлен в группу '{group_name}'.")  # Подтверждение добавления
        else:
            print(f"Студент '{student_name}' или группа '{group_name}' не найдены.")  # Ошибка, если не найден студент или группа

    def transfer_student(self, student_name, from_group_name, to_group_name):
        """Переводит студента из одной группы в другую.

        Args:
            student_name (str): Имя студента.
            from_group_name (str): Имя исходной группы.
            to_group_name (str): Имя целевой группы.
        """
        from_group = self.get_group_by_name(from_group_name)  # Находим исходную группу
        to_group = self.get_group_by_name(to_group_name)  # Находим целевую группу

        if from_group and to_group:
            student = next((s for s in from_group.students if s.name == student_name), None)  # Находим студента в исходной группе
            if student:
                from_group.remove_student(student)  # Удаляем студента из исходной группы
                to_group.add_student(student)  # Добавляем студента в целевую группу
                print(f"Студент '{student_name}' переведен из группы '{from_group_name}' в группу '{to_group_name}'.")
            else:
                print(f"Студент '{student_name}' не найден в группе '{from_group_name}'.")  # Ошибка, если студент не найден
        else:
            print("Одна или обе группы не найдены.")  # Ошибка, если одна из групп не найдена

    def list_students_in_group(self, group_name):
        """Возвращает список студентов в указанной группе.

        Args:
            group_name (str): Имя группы.

        Returns:
            list or None: Список студентов в группе или None, если группа не найдена.
        """
        group = self.get_group_by_name(group_name)  # Находим группу по имени
        if group:
            return group.list_students()  # Возвращаем список студентов в группе
        else:
            return None  # Если группа не найдена, возвращаем None

    def assign_monitor(self, student_name, group_name):
        """Назначает старосту в группе.

        Args:
            student_name (str): Имя студента.
            group_name (str): Имя группы.
        """
        group = self.get_group_by_name(group_name)  # Находим группу по имени
        student = next((s for s in group.students if s.name == student_name), None)  # Находим студента в группе

        if group and student:
            # Создаем декорированного студента
            decorated_student = StudentDecorator(student)  # Декорируем студента
            # Находим индекс студента в списке и заменяем его на декорированного
            student_index = group.students.index(student)  # Получаем индекс студента
            group.students[student_index] = decorated_student  # Обновляем список студентов
            print(f"Студент '{student_name}' назначен старостой в группе '{group_name}'.")
        else:
            print("Группа или студент не найдены.")  # Ошибка, если группа или студент не найдены