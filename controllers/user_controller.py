import json

from models.user import User


class UserController:
    """Контроллер для управления пользователями."""

    def __init__(self):
        self.users = []  # Инициализация как список

    def create_user(self, username):
        """Создает нового пользователя и добавляет его в список."""
        user = User(username)  # Создаем объект User
        self.users.append(user)  # Добавляем объект в список

    def delete_user(self, username):
        user = next((u for u in self.users if u.username == username), None)
        if user:
            self.users.remove(user)

    def list_users(self):
        return [user.username for user in self.users]

    def clone_user(self, username):
        """Клонирует пользователя и добавляет его в список."""
        user = next((u for u in self.users if u.username == username), None)
        if user:
            cloned_user = user.clone()
            self.users.append(cloned_user)
            return cloned_user
        return None

    def save_users(self, filename):
        """Сохраняет пользователей в файл."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([user.username for user in self.users], file, ensure_ascii=False)

    def load_users(self, filename):
        """Загружает пользователей из файла."""
        with open(filename, 'r', encoding='utf-8') as file:
            user_names = json.load(file)
            self.users = [User(name) for name in user_names]  # Предполагается, что есть класс User