'''
Комплексное число записывается в виде: z = re + im * i, где
         re - действительная часть
         im - мнимая часть
         i - мнимая единица
'''
x = 1
y = 1


def init(a_re, a_im, b_re, b_im):
    global x
    global y
    x = complex(a_re, a_im)
    y = complex(b_re, b_im)


def summ():
    return f'{x} + {y} = {x + y}'


def sub():
    return f'{x} - {y} = {x - y}'


def mult():
    return f'{x} * {y} = {x * y}'


def part():
    return f'{x} / {y} = {x / y}'
    
 
