from __future__ import annotations
from typing import Any, Dict
from unittest.mock import patch, MagicMock
import pytest
from src.external_api import convert_to_rub


@pytest.fixture
def usd_transaction() -> Dict[str, Any]:
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"},
        }
    }


@patch("src.external_api.requests.get")
@patch("src.external_api.os.getenv", return_value="fake_api_key")
def test_convert_usd_to_rub(mock_getenv: MagicMock, mock_get: MagicMock, usd_transaction: Dict[str, Any]) -> None:
    """Тестирует корректную конвертацию USD → RUB без реального API."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 9500.0}

    result = convert_to_rub(usd_transaction)

    assert result == 9500.0
    mock_get.assert_called_once()
    mock_getenv.assert_called_once_with("EXCHANGE_API_KEY")
