from models.group import Group


class GroupCreator:
    """Создатель групп.

    Этот класс отвечает за создание групп с заданными именами.
    """

    @staticmethod
    def create(name):
        """Создает группу с заданным именем.

        Args:
            name (str): Имя группы.

        Returns:
            Group: Экземпляр созданной группы.
        """
        return Group(name)  # Создаем и возвращаем объект Group с заданным именем
