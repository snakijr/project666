from src.generators import filter_by_currency


def test_filter_by_currency_usd(sample_transactions):
    """Фильтрация должна вернуть только USD транзакции"""
    gen = filter_by_currency(sample_transactions, "USD")  # ← передаем аргументы!
    results = list(gen)
    assert len(results) == 1
    assert results[0]["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_eur(sample_transactions):
    """Фильтрация должна вернуть только EUR транзакции"""
    gen = filter_by_currency(sample_transactions, "EUR")
    results = list(gen)
    assert len(results) == 1
    assert results[0]["operationAmount"]["currency"]["code"] == "EUR"


def test_filter_by_currency_absent_currency(sample_transactions):
    """Если валюты нет, должен вернуться пустой список"""
    gen = filter_by_currency(sample_transactions, "GBP")
    results = list(gen)
    assert results == []


def test_filter_by_currency_empty_list():
    """Функция должна корректно работать с пустым списком"""
    gen = filter_by_currency([], "USD")
    results = list(gen)
    assert results == []


def test_filter_by_currency_no_currency_field():
    """Если в транзакции нет currency, генератор не должен падать"""
    transactions = [
        {"id": 1, "operationAmount": {"amount": "100"}, "description": "Без валюты"},
        {"id": 2, "description": "Совсем пустая"},
    ]
    gen = filter_by_currency(transactions, "USD")
    results = list(gen)
    assert results == []
