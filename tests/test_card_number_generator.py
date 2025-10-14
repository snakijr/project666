import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 1, ["0000 0000 0000 0001"]),  # нижняя граница
        (9999999999999999, 9999999999999999, ["9999 9999 9999 9999"]),  # верхняя граница
    ],
)
def test_card_number_generator_edges(start, end, expected):
    """Генератор должен корректно работать на крайних значениях"""
    gen = card_number_generator(start, end)
    results = list(gen)
    assert results == expected
