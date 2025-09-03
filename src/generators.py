

def filter_by_currency(transactions: list, currency_code: str):
    """
    Генератор, который отдает транзакции с указанной валютой.

    :param transactions: список словарей с транзакциями
    :param currency_code: код валюты (например, "USD")
    :yield: транзакции в нужной валюте
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"].get("code") == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions: list):
    """
    Генератор, который возвращает описания транзакций.

    :param transactions: список словарей с транзакциями
    :yield: описание каждой операции
    """
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


def card_number_generator(start: int, end: int):
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.

    :param start: начальное значение диапазона (int)
    :param end: конечное значение диапазона (int)
    :yield: номера карт от start до end включительно
    """
    for number in range(start, end + 1):
        # Преобразуем число в строку длиной 16 символов с ведущими нулями
        card_str = f"{number:016d}"
        # Разбиваем на блоки по 4 цифры
        formatted = " ".join(card_str[i:i+4] for i in range(0, 16, 4))
        yield formatted