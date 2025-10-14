import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_number: str) -> None:
    """Тестовая функция для файла mask.py и функции mask_card_number"""
    assert get_mask_card_number(card_number) == "4400 44** **** 4400"


def test_mask_card_number_invalid() -> None:
    """Тестовая функция для файла mask.py и функции mask_card_number"""
    with pytest.raises(TypeError):
        get_mask_card_number(123)


@pytest.mark.parametrize("account_number, expected", [("73654108430135874305", "**4305")])
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Тестовая параметризация для файла mask.py и функции get_mask_account"""
    assert get_mask_account(account_number) == expected


def test_get_mask_account_invalid() -> None:
    """Тестовая параметризация для файла mask.py и функции get_mask_account"""
    with pytest.raises(TypeError):
        get_mask_account(123)
