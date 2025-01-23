from models.group import Group


class GroupCreator:
    """Создатель групп."""

    @staticmethod
    def create(name):
        """Создает группу с заданным именем."""
        return Group(name)