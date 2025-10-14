from __future__ import annotations

import os
from typing import Any, Dict
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях.
    Если валюта — RUB, возвращает исходную сумму.
    Если валюта — USD или EUR, выполняет запрос к Exchange Rates Data API.

    :param transaction: Словарь с ключами:
        "operationAmount" -> {"amount": str, "currency": {"code": str}}
    :return: Сумма транзакции в рублях (float)
    """
    operation: Dict[str, Any] = transaction.get("operationAmount", {})
    amount_str: str | None = operation.get("amount")
    currency_data: Dict[str, Any] | None = operation.get("currency")

    currency_code: str | None = None
    if currency_data and isinstance(currency_data.get("code"), str):
        currency_code = currency_data["code"]

    # если данных нет — возвращаем 0.0
    if not amount_str or not currency_code:
        return 0.0

    # безопасно конвертируем строку в float
    try:
        amount: float = float(amount_str)
    except (TypeError, ValueError):
        return 0.0

    # если рубли — возвращаем сразу
    if currency_code == "RUB":
        return amount

    # получаем ключ API из .env
    api_key: str | None = os.getenv("EXCHANGE_API_KEY")
    if api_key is None:
        raise ValueError("Отсутствует токен EXCHANGE_API_KEY в .env")

    # готовим запрос
    url: str = "https://api.apilayer.com/exchangerates_data/convert"
    params: Dict[str, str | float] = {"from": currency_code, "to": "RUB", "amount": amount}
    headers: Dict[str, str] = {"apikey": api_key}

    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()

        data: Dict[str, Any] = response.json()
        result_raw: Any = data.get("result", 0.0)
        return float(result_raw)
    except (requests.RequestException, ValueError):
        return 0.0
