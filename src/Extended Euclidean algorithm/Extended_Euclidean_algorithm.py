def f(a, b):
    if a == b == 0:
        return 'Не определён или (0, 0, 0)'
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while b != 0:
        q = a // b
        si = s0 - q * s1
        ti = t0 - q * t1
        a, b = b, a % b
        s0, s1 = s1, si
        t0, t1 = t1, ti
    return f'gcd = {abs(a)}, x = {s0}, y = {t0}'

a, b = int(input('Введите первое число: ')), int(input('Введите второе число: '))
print(f(a, b))