from datetime import datetime

def filter_by_state(list_dict: list, state_value: str = "EXECUTED") -> list:
    '''Фильтрует список словарей по значению ключа state'''
    result = []

    for item in list_dict:
        if item.get("state") == state_value:
            result.append(item)

    return result




def sort_by_date(list_dict: list, date_key: str = "date", reverse: bool = False) -> list:
    """
    Функция возвращает новый список, отсортированный по дате.
    Поддерживает ISO-форматы: 'YYYY-MM-DD', 'YYYY-MM-DDTHH:MM:SS', 'YYYY-MM-DDTHH:MM:SS.ssssss'
    """
    return sorted(
        list_dict,
        key=lambda item: datetime.fromisoformat(item[date_key]),
        reverse=reverse
    )

