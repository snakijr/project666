import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expect",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(input_data: str, expect: str) -> None:
    """Тестовая переметризация для файла widget.py и функции mask_account_card"""
    assert mask_account_card(input_data) == expect


@pytest.mark.parametrize(
    "input_data, expect",
    [
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
    ],
)
def test_get_date(input_data: str, expect: str) -> None:
    """Тестовая переметризация для файла widget.py и функции get_date"""
    assert get_date(input_data) == expect
