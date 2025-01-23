from models.group import Group


class GroupFactory:
    """Абстрактная фабрика для создания групп."""

    @staticmethod
    def create_group(name, group_type='study'):
        """Создает группу в зависимости от типа."""
        if group_type == 'study':
            return Group(name)  # Возвращаем обычную группу
        # Здесь можно добавить другие типы групп
        raise ValueError(f"Unknown group type: {group_type}")