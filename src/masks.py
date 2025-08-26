def get_mask_card_number(card_number: str | int) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    if isinstance(card_number, str):
        masked_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        return masked_card
    raise TypeError("Неверный формат аргумента")


def get_mask_account(account_number: str | int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    if isinstance(account_number, str):
        masked_account = f"**{account_number[-4:]}"
        return masked_account
    raise TypeError("Неверный формат аргумента")
