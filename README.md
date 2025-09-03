# Программа, которая маскирует номера счетов и карт

## Описание:

Программа, которая маскирует номера счетов и карт, также фильтрует по дате совершенные платежи.  
Добавлен модуль **generators.py** с генераторами для работы с транзакциями и номерами карт.

## Установка:

1. Клонируйте репозиторий:
```
https://github.com/snakijr/project666.git
```
2. Установите зависимости и poetry:
```
pip install poetry
```
все необходимые зависимости лежат в файле pyproject.toml 

## Использование:

### masks.py
1. Откройте файл `masks.py` через Pycharm.
2. Вызовите функцию или добавьте к ней входящие данные, и она будет маскировать 
   данные карты звёздочками в виде `7000 79** **** 6361`
3. Файл `masks.py` может принимать данные о типе карты и её номер `Maestro 1596837868705199` или `Счет 64686473678894779589`  
   возвращает `Maestro 1596 83** **** 5199` и `Счет **9589` соответственно.

### processing.py
Файл `processing.py` отвечает за сортировку по датам последнего или первого платежа, принимает формат даты `ISO`.

### generators.py
Новый модуль, включающий генераторы:

#### 1. filter_by_currency
Фильтрует транзакции по заданной валюте.
```python
from src.generators import filter_by_currency

transactions = [
    {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Перевод"},
    {"id": 2, "operationAmount": {"amount": "200", "currency": {"code": "EUR"}}, "description": "Перевод"},
]

gen = filter_by_currency(transactions, "USD")
print(next(gen))  
# {"id": 1, "operationAmount": {"amount": "100", "currency": {"code": "USD"}}, "description": "Перевод"}
```

#### 2. transaction_descriptions
Возвращает описание каждой транзакции по очереди.
```python
from src.generators import transaction_descriptions

transactions = [
    {"id": 1, "description": "Перевод организации"},
    {"id": 2, "description": "Перевод со счета на счет"},
]

gen = transaction_descriptions(transactions)
print(next(gen))  # "Перевод организации"
print(next(gen))  # "Перевод со счета на счет"
```

#### 3. card_number_generator
Генерирует номера карт в заданном диапазоне в формате `XXXX XXXX XXXX XXXX`.
```python
from src.generators import card_number_generator

gen = card_number_generator(1, 3)
print(list(gen))
# ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']
```

#### 4. infinite_card_number_generator
Бесконечно выдаёт номера карт в формате `XXXX XXXX XXXX XXXX`, начиная с указанного значения.
```python
from src.generators import infinite_card_number_generator

gen = infinite_card_number_generator(9999999999999997)
print(next(gen))  # '9999 9999 9999 9997'
print(next(gen))  # '9999 9999 9999 9998'
print(next(gen))  # '9999 9999 9999 9999'
print(next(gen))  # '0000 0000 0000 0001' (цикл заново)
```

## Лицензия:

Этот проект лицензирован по [лицензии MIT](https://opensource.org/licenses/MIT).
