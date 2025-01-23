import copy


class User:
    """Класс, представляющий пользователя."""

    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        """Добавляет пост пользователю."""
        self.posts.append(post)

    def remove_post(self, post):
        """Удаляет пост у пользователя."""
        self.posts.remove(post)

    def clone(self):
        """Клонирует пользователя."""
        return copy.deepcopy(self)  # Используем deepcopy для глубокого копирования
