import json
from decorators.post_decorator import PostDecorator
from models.post import Post
from models.user import User


class UserController:
    """Контроллер для управления пользователями.

    Этот класс позволяет создавать, удалять пользователей, а также управлять их постами.
    """

    def __init__(self):
        """Инициализирует контроллер с пустым списком пользователей и словарем для постов."""
        self.users = []  # Инициализация как список
        self.posts = {}  # Словарь для хранения постов пользователей

    def create_user(self, username):
        """Создает нового пользователя и добавляет его в список.

        Args:
            username (str): Имя пользователя.
        """
        user = User(username)  # Создаем объект User
        self.users.append(user)  # Добавляем объект в список

    def delete_user(self, username):
        """Удаляет пользователя по имени.

        Args:
            username (str): Имя пользователя для удаления.
        """
        user = next((u for u in self.users if u.username == username), None)  # Находим пользователя
        if user:
            self.users.remove(user)  # Удаляем пользователя из списка

    def list_users(self):
        """Возвращает список имен пользователей.

        Returns:
            list: Список имен пользователей.
        """
        return [user.username for user in self.users]  # Возвращаем имена всех пользователей

    def clone_user(self, username):
        """Клонирует пользователя и добавляет его в список.

        Args:
            username (str): Имя пользователя для клонирования.

        Returns:
            User or None: Клонированный пользователь или None, если пользователь не найден.
        """
        user = next((u for u in self.users if u.username == username), None)  # Находим пользователя
        if user:
            cloned_user = user.clone()  # Клонируем пользователя
            self.users.append(cloned_user)  # Добавляем клонированного пользователя в список
            return cloned_user  # Возвращаем клонированного пользователя
        return None  # Если пользователь не найден, возвращаем None

    def save_users(self, filename):
        """Сохраняет пользователей в JSON файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump([user.username for user in self.users], file, ensure_ascii=False)  # Сохраняем имена пользователей в файл

    def load_users(self, filename):
        """Загружает пользователей из JSON файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            user_names = json.load(file)  # Загружаем имена пользователей из файла
            self.users = [User(name) for name in user_names]  # Создаем экземпляры пользователей по загруженным именам

    def create_post(self, username, content):
        """Создает пост для указанного пользователя.

        Args:
            username (str): Имя пользователя, которому принадлежит пост.
            content (str): Содержимое поста.
        """
        post = Post(username, content)  # Создаем экземпляр Post
        if username not in self.posts:
            self.posts[username] = []  # Если пользователя нет в словаре, создаем новый список
        self.posts[username].append(post)  # Добавляем пост в список постов пользователя

    def hide_post(self, username, post_index):
        """Скрывает пост для указанного пользователя.

        Args:
            username (str): Имя пользователя, чей пост нужно скрыть.
            post_index (int): Индекс поста в списке постов пользователя.
        """
        if username in self.posts and 0 <= post_index < len(self.posts[username]):
            post = self.posts[username][post_index]  # Получаем пост по индексу
            decorator = PostDecorator(post)  # Создаем декоратор для поста
            decorator.hide()  # Скрываем пост
            print(f"Пост скрыт для пользователя '{username}'.")  # Подтверждение скрытия поста
        else:
            print("Пост не найден.")  # Ошибка, если пост не найден