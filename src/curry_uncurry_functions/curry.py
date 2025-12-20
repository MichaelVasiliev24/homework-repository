import inspect


def curry(func, arity):
    """Преобразует функцию от нескольких аргументов в цепочку функций от одного аргумента"""
    if not callable(func):
        raise TypeError(f"Получен невызываемый объект, его тип: {type(func)}")

    if arity < 0:
        raise ValueError(f"Арность не может быть отрицательной: {arity}")

    # Проверяем арность через inspect
    # Получение сигнатуры в try-except
    param_count = None
    try:
        sig = inspect.signature(func)
        params = list(sig.parameters.values())
        param_count = len(params)
    except (ValueError, TypeError):
        pass
    if param_count is not None and arity != param_count:
        raise ValueError(
            f"Указанная арность ({arity}) не соответствует количеству "
            f"аргументов функции ({param_count})"
        )

    if arity == 0:
        return lambda: func()

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])

        def partial(*next_args):
            return curried(*(args + next_args))

        return partial

    return curried
