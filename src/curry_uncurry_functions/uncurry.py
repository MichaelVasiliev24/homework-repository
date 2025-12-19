def uncurry(curried_func, arity):
    """Преобразует каррированную функцию обратно в одну функцию от нескольких аргументов"""
    if not callable(curried_func):
        raise TypeError(f"Поллучен не вызываемый объект, его тип: {type(curried_func)}")

    if arity < 0:
        raise ValueError(f"Арность не может быть отрицательной: {arity}")

    def uncurried(*args):
        if len(args) != arity:
            raise TypeError(f"Должно быть {arity} аргументов, получено: {len(args)}")

        result = curried_func
        for arg in args:
            result = result(arg)
        return result

    return uncurried
