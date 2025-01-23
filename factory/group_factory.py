from models.group import Group


class GroupFactory:
    """Абстрактная фабрика для создания групп.

    Этот класс предоставляет методы для создания различных типов групп.
    """

    @staticmethod
    def create_group(name, group_type='study'):
        """Создает группу в зависимости от типа.

        Args:
            name (str): Имя группы.
            group_type (str): Тип группы (по умолчанию 'study').

        Returns:
            Group: Экземпляр созданной группы.

        Raises:
            ValueError: Если указан неизвестный тип группы.
        """
        if group_type == 'study':
            return Group(name)  # Возвращаем обычную учебную группу
        # Здесь можно добавить другие типы групп
        raise ValueError(f"Unknown group type: {group_type}")  # Исключение для неизвестного типа группы