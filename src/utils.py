import json

def load_json(filepath):
    """
    Загружает данные из JSON-файла.

    Args:
        filepath (str): Путь к JSON-файлу.

    Returns:
        dict | list: Содержимое JSON-файла.

    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: Если файл не удалось декодировать.
        ValueError: Если файл пустой.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            # читаем содержимое файла
            content = file.read().strip()
            # если пусто — выбрасываем ValueError
            if not content:
                raise ValueError("Файл пустой.")
            # пробуем декодировать JSON
            return json.loads(content)

    except FileNotFoundError:
        print(f"Ошибка: файл '{filepath}' не найден.")
        raise
    except json.JSONDecodeError as e:
        print(f"Ошибка: не удалось декодировать JSON ({e})")
        raise
