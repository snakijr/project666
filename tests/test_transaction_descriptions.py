import pytest

from src.generators import transaction_descriptions


def test_transaction_descriptions_all(sample_transactions_descriptions):
    """Функция должна возвращать все описания в правильном порядке"""
    gen = transaction_descriptions(sample_transactions_descriptions)
    results = list(gen)

    assert results == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
    ]


def test_transaction_descriptions_partial(sample_transactions_descriptions):
    """Можно по очереди забирать описания"""
    gen = transaction_descriptions(sample_transactions_descriptions)

    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"

    with pytest.raises(StopIteration):
        next(gen)  # генератор закончился


def test_transaction_descriptions_empty():
    """Если список пустой, генератор не должен выдавать значения"""
    gen = transaction_descriptions([])
    results = list(gen)

    assert results == []
