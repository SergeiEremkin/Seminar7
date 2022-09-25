
'''
Рациональные числа - числа с дробной частью
Иницилизация рационального числа. Операции с числами находятся в модуле operation_complex чтобы не дублировать код
'''
x = 0
y = 1


def init(a, b):
    global x
    global y
    x = float(a)
    y = float(b)


def summ():
    return f'{x} + {y} = {x + y}'


def sub():
    return f'{x} - {y} = {x - y}'


def mult():
    return f'{x} * {y} = {x * y}'


def part():
    return f'{x} / {y} = {x / y}'
