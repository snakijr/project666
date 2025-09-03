def filter_by_currency(transactions: list, currency_code: str):
    """Генератор, который отдает транзакции с указанной валютой."""
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"].get("code") == currency_code
        ):
            yield transaction

usd_transactions = filter_by_currency(transactions, "USD")

for _ in range(2):
    print(next(usd_transactions))



def transaction_descriptions(transactions: list):
    """Генератор, который поочередно возвращает описания транзакций."""
    for transaction in transactions:
        if "description" in transaction:
            yield transaction["description"]


descriptions = transaction_descriptions(transactions)

for _ in range(5):
    print(next(descriptions))



def card_number_generator(start: int, end: int):
    """Генератор номеров карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, end + 1):
        # Преобразуем число в строку длиной 16 с ведущими нулями
        card_str = f"{number:016d}"
        # Форматируем блоками по 4 цифры
        formatted = " ".join(card_str[i:i+4] for i in range(0, 16, 4))
        yield formatted


cards = card_number_generator(1, 5)

for card in cards:
    print(card)

