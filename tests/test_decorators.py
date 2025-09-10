import pytest
from src.decorators import log


# --- Тесты для консоли ---
def test_success_console(capsys):
    @log()
    def add(x, y):
        return x + y

    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_error_console(capsys):
    @log()
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(1, 0)

    captured = capsys.readouterr()
    assert "div error: ZeroDivisionError" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


# --- Тесты для файла ---
def test_success_file(tmp_path):
    log_file = tmp_path / "testlog.txt"

    @log(filename=log_file)
    def mul(x, y):
        return x * y

    result = mul(3, 4)
    assert result == 12

    content = log_file.read_text(encoding="utf-8")
    assert "mul ok" in content


def test_error_file(tmp_path):
    log_file = tmp_path / "testlog.txt"

    @log(filename=log_file)
    def div(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        div(10, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "div error: ZeroDivisionError" in content
    assert "Inputs: (10, 0), {}" in content
