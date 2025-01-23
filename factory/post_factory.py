from models.post import Post


class PostFactory:
    """Фабрика для создания постов."""

    @staticmethod
    def create_post(content):
        """Создает новый пост с заданным содержимым."""
        return Post(content)