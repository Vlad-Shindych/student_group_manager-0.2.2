class PostDecorator:
    """Декоратор для скрытия поста."""

    def __init__(self, post):
        self.post = post

    def __str__(self):
        return f"{self.post.content} (пост закрыт для просмотра)"