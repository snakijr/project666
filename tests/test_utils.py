import json
import pytest
from src.utils import load_json


def test_load_json_success(tmp_path):
    """Проверка успешного чтения корректного JSON-файла."""
    file_path = tmp_path / "data.json"
    data = {"name": "Dmitriy", "age": 30}
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_json(str(file_path))
    assert result == data


def test_load_json_file_not_found():
    """Проверка обработки ошибки FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        load_json("nonexistent.json")


def test_load_json_decode_error(tmp_path):
    """Проверка обработки ошибки json.JSONDecodeError."""
    file_path = tmp_path / "bad.json"
    file_path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_json(str(file_path))


def test_load_json_empty_file(tmp_path):
    """Проверка обработки пустого файла."""
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="Файл пустой."):
        load_json(str(file_path))


def test_load_json_whitespace_only(tmp_path):
    """Проверка обработки файла, содержащего только пробелы и переносы строк."""
