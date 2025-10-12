import json
import os


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает данные о финансовых транзакциях из JSON-файла.

    :param file_path: Путь до JSON-файла (например: "data/operations.json")
    :return: Список словарей с транзакциями.
             Если файл не найден, пустой или содержит не список — возвращает [].
             Также исключает пустые объекты {} из результата.
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Проверяем, что это список и фильтруем пустые записи
            if isinstance(data, list):
                return [item for item in data if isinstance(item, dict) and item]
            return []
    except (json.JSONDecodeError, OSError):
        return []
