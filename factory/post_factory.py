from models.post import Post


class PostFactory:
    """Фабрика для создания постов.

    Этот класс отвечает за создание экземпляров постов с заданным содержимым.
    """

    @staticmethod
    def create_post(content):
        """Создает новый пост с заданным содержимым.

        Args:
            content (str): Содержимое поста.

        Returns:
            Post: Экземпляр созданного поста.
        """
        return Post(content)  # Создаем и возвращаем объект Post с заданным содержимым