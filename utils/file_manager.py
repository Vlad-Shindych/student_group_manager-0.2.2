import json


class FileManager:
    """Класс для работы с файлами."""

    @staticmethod
    def save_data(filename, data):
        """Сохраняет данные в файл."""
        with open(filename, 'w', encoding='utf-8') as f:  # Используем кодировку utf-8
            json.dump(data, f, ensure_ascii=False, indent=4)  # Добавляем ensure_ascii=False

    @staticmethod
    def load_data(filename):
        """Загружает данные из файла."""
        with open(filename, 'r', encoding='utf-8') as f:  # Используем кодировку utf-8
            return json.load(f)