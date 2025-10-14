from functools import wraps

def log(filename=None):
    """
    Декоратор для логирования выполнения функций.

    Если указан параметр `filename`, то логи записываются в файл (добавляются в конец).
    Если параметр не указан, то сообщения выводятся в консоль.

    Поведение:
    - При успешном выполнении функции записывается сообщение: "<имя_функции> ok".
    - При возникновении ошибки записывается сообщение:
      "<имя_функции> error: <ТипОшибки>. Inputs: (args), {kwargs}".
    - После завершения работы файл закрывается (если использовался).

    Аргументы:
        filename (str | None): путь к файлу для логов или None для вывода в консоль.

    Возвращает:
        function: обёрнутую функцию с логированием.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_target = open(filename, "a", encoding="utf-8") if filename else None
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if log_target:
                    print(message, file=log_target)
                else:
                    print(message)
                return result
            except Exception as e:
                error_type = type(e).__name__
                message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}"
                if log_target:
                    print(message, file=log_target)
                else:
                    print(message)
                raise
            finally:
                if log_target:
                    log_target.close()
        return wrapper
    return decorator
