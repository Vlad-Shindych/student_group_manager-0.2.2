import json


class FileManager:
    """Класс для работы с файлами.

    Этот класс предоставляет методы для сохранения и загрузки данных в формате JSON.
    """

    @staticmethod
    def save_data(filename, data):
        """Сохраняет данные в файл в формате JSON.

        Args:
            filename (str): Имя файла, в который будут сохранены данные.
            data (any): Данные, которые нужно сохранить (могут быть любого типа, поддерживаемого JSON).
        """
        with open(filename, 'w', encoding='utf-8') as f:  # Открываем файл для записи с кодировкой utf-8
            json.dump(data, f, ensure_ascii=False, indent=4)  # Сохраняем данные в файл, форматируя их

    @staticmethod
    def load_data(filename):
        """Загружает данные из файла в формате JSON.

        Args:
            filename (str): Имя файла, из которого будут загружены данные.

        Returns:
            any: Загруженные данные (первоначальный тип данных).
        """
        with open(filename, 'r', encoding='utf-8') as f:  # Открываем файл для чтения с кодировкой utf-8
            return json.load(f)  # Загружаем и возвращаем данные из файла