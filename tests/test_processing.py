from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(fixture_filter_by_state: list[dict]) -> None:
    """Тестовая параметризация для файла processing.py и функции filter_by_state"""
    assert filter_by_state(fixture_filter_by_state) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
    ]
    assert filter_by_state(fixture_filter_by_state, state_value="CANCELED") == [
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
    ]


def test_sort_by_date(fixture_filter_by_state: list[dict]) -> None:
    """Тестовая параметризация для файла processing.py и функции sort_by_date"""
    assert sort_by_date(fixture_filter_by_state) == [
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
    ]
