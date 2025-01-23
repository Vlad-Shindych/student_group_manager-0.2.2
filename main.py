from controllers.group_controller import GroupController
from controllers.student_controller import StudentController
from controllers.user_controller import UserController
from factory.student_factory import StudentFactory
from models.student import Student
from decorators.student_decorator import StudentDecorator  # Импортируйте декоратор
from decorators.post_decorator import PostDecorator  # Импортируйте декоратор постов

def main():
    """Основная функция приложения.

    Эта функция управляет взаимодействием с пользователем и координирует
    работу контроллеров для управления группами, студентами и пользователями.
    """
    student_controller = StudentController()
    group_controller = GroupController(student_controller)
    user_controller = UserController()

    while True:
        print("\n1. Управление группами")
        print("2. Управление студентами")
        print("3. Управление пользователями и постами")
        print("4. Сохранить данные")
        print("5. Загрузить данные")
        print("6. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            # Управление группами
            while True:
                print("\n1. Создать группу")
                print("2. Удалить группу")
                print("3. Просмотреть группы")
                print("4. Просмотреть студентов в группе")
                print("5. Клонировать группу")
                print("6. Назначить старосту в группе")  # Новый пункт
                print("7. Вернуться в главное меню")

                group_choice = input("Ваш выбор: ")

                if group_choice == "1":
                    name = input("Введите имя группы: ")
                    group_controller.create_group(name)
                    print(f"Группа '{name}' создана.")
                elif group_choice == "2":
                    name = input("Введите имя группы для удаления: ")
                    group = group_controller.get_group_by_name(name)
                    if group:
                        group_controller.delete_group(group)
                        print(f"Группа '{name}' удалена.")
                    else:
                        print("Группа не найдена.")
                elif group_choice == "3":
                    print("Группы:", group_controller.list_groups())
                elif group_choice == "4":
                    group_name = input("Введите имя группы для просмотра студентов: ")
                    students = group_controller.list_students_in_group(group_name)
                    if students is not None:
                        if students:
                            output_students = [str(student) for student in students]  # Используем строковое представление
                            print(f"Студенты в группе '{group_name}': {', '.join(output_students)}")
                        else:
                            print(f"В группе '{group_name}' нет студентов.")
                    else:
                        print("Группа не найдена.")
                elif group_choice == "5":
                    name = input("Введите имя группы для клонирования: ")
                    group = group_controller.get_group_by_name(name)
                    if group:
                        cloned_group = group_controller.clone_group(group)
                        print(f"Клонированная группа: '{cloned_group.name}'")
                    else:
                        print("Группа не найдена.")
                elif group_choice == "6":
                    student_name = input("Введите имя студента для назначения старостой: ")
                    group_name = input("Введите имя группы, в которой назначаете старосту: ")
                    group_controller.assign_monitor(student_name, group_name)  # Вызов метода назначения старосты
                elif group_choice == "7":
                    break  # Возврат в главное меню
                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif choice == "2":
            # Управление студентами
            while True:
                print("\n1. Создать студента")
                print("2. Удалить студента")
                print("3. Просмотреть студентов")
                print("4. Перевести студента")
                print("5. Вернуться в главное меню")

                student_choice = input("Ваш выбор: ")

                if student_choice == "1":
                    name = input("Введите имя студента: ")
                    student = StudentFactory.create_student(name)
                    student_controller.create_student(student)
                    print(f"Студент '{name}' создан.")

                    # Запрос группы для добавления студента
                    group_name = input("Введите имя группы для добавления студента: ")
                    group_controller.add_student_to_group(student.name, group_name)
                elif student_choice == "2":
                    name = input("Введите имя студента для удаления: ")
                    student = next((s for s in student_controller.students if s.name == name), None)
                    if student:
                        student_controller.delete_student(student)
                        print(f"Студент '{name}' удален.")
                    else:
                        print("Студент не найден.")
                elif student_choice == "3":
                    print("Студенты:", student_controller.list_students())
                elif student_choice == "4":
                    student_name = input("Введите имя студента для перевода: ")
                    from_group_name = input("Введите имя группы, из которой переводите: ")
                    to_group_name = input("Введите имя группы, в которую переводите: ")
                    group_controller.transfer_student(student_name, from_group_name, to_group_name)
                elif student_choice == "5":
                    break  # Возврат в главное меню
                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif choice == "3":
            # Управление пользователями и постами
            while True:
                print("\n1. Создать пользователя")
                print("2. Удалить пользователя")
                print("3. Создать пост")
                print("4. Просмотреть пользователей")
                print("5. Просмотреть посты всех пользователей")  # Новый пункт
                print("6. Скрыть пост")  # Новый пункт
                print("7. Клонировать пользователя")
                print("8. Вернуться в главное меню")

                user_choice = input("Ваш выбор: ")

                if user_choice == "1":
                    username = input("Введите имя пользователя: ")
                    user_controller.create_user(username)
                    print(f"Пользователь '{username}' создан.")
                elif user_choice == "2":
                    username = input("Введите имя пользователя для удаления: ")
                    user_controller.delete_user(username)
                    print(f"Пользователь '{username}' удален.")
                elif user_choice == "3":
                    username = input("Введите имя пользователя для создания поста: ")
                    content = input("Введите содержимое поста: ")
                    user_controller.create_post(username, content)
                    print("Пост создан.")
                elif user_choice == "4":
                    print("Пользователи:", user_controller.list_users())
                elif user_choice == "5":
                    for username, posts in user_controller.posts.items():
                        print(f"Пользователь: {username}")
                        for i, post in enumerate(posts):
                            print(f"  Пост {i + 1}: {post}")
                elif user_choice == "6":
                    username = input("Введите имя пользователя, чей пост хотите скрыть: ")
                    post_index = int(input("Введите индекс поста для скрытия: "))  # Например, 0 для первого поста
                    user_controller.hide_post(username, post_index)
                elif user_choice == "7":
                    username = input("Введите имя пользователя для клонирования: ")
                    cloned_user = user_controller.clone_user(username)
                    if cloned_user:
                        print(f"Клонированный пользователь: '{cloned_user.username}'")
                    else:
                        print("Пользователь не найден.")
                elif user_choice == "8":
                    break  # Возврат в главное меню
                else:
                    print("Неверный выбор. Попробуйте снова.")

        elif choice == "4":
            # Сохранение данных
            group_file = input("Введите имя файла для сохранения групп: ")
            student_file = input("Введите имя файла для сохранения студентов: ")
            user_file = input("Введите имя файла для сохранения пользователей: ")

            group_controller.save_groups(group_file)
            student_controller.save_students(student_file)
            user_controller.save_users(user_file)

            print("Данные сохранены.")

        elif choice == "5":
            # Загрузка данных
            group_file = input("Введите имя файла для загрузки групп: ")
            student_file = input("Введите имя файла для загрузки студентов: ")
            user_file = input("Введите имя файла для загрузки пользователей: ")

            group_controller.load_groups(group_file)
            student_controller.load_students(student_file)
            user_controller.load_users(user_file)

            print("Данные загружены.")

        elif choice == "6":
            print("Выход из программы.")
            break  # Завершение программы
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()