import pytest


@pytest.fixture
def sample_transactions_descriptions():
    return [
        {
            "id": 1,
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "100",
                "currency": {"code": "USD", "name": "USD"},
            },
        },
        {
            "id": 2,
            "description": "Перевод со счета на счет",
            "operationAmount": {
                "amount": "200",
                "currency": {"code": "EUR", "name": "EUR"},
            },
        },
        {
            "id": 3,
            "description": "Перевод с карты на карту",
            "operationAmount": {
                "amount": "300",
                "currency": {"code": "RUB", "name": "RUB"},
            },
        },
    ]


@pytest.fixture
def sample_transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "EUR", "code": "EUR"},
            },
            "description": "Перевод в евро",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"name": "RUB", "code": "RUB"},
            },
            "description": "Перевод в рублях",
        },
    ]


@pytest.fixture
def card_number() -> str:
    """Тестовая фикстура для файла mask.py и функции card_number"""
    return "4400440044004400"


@pytest.fixture
def fixture_filter_by_state() -> list[dict]:
    """Тестовая фикстура для файла processing.py и функции filter_by_state"""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
