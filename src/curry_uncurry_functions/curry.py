def curry(func, arity):
    """Преобразует функцию от нескольких аргументов в цепочку функций от одного аргумента"""
    if not callable(func):
        raise TypeError(f"Получен невызываемый объект, его тип: {type(func)}")

    if arity < 0:
        raise ValueError(f"Арность не может быть отрицательной: {arity}")

    if arity == 0:
        return lambda: func()

    def curried(*args):
        if len(args) >= arity:
            return func(*args[:arity])

        def partial(*next_args):
            return curried(*(args + next_args))

        return partial

    return curried
