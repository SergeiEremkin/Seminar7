# Сергей
'''
Комплексное число записывается в виде: z = re + im * i, где
         re - действительная часть
         im - мнимая часть
         i - мнимая единица
'''

x = 0
y = 0




def init(a_re, a_im, b_re, b_im):
    global x
    global y
    x = complex(a_re, a_im)
    y = complex(b_re, b_im)


def sum():
    return x + y


def sub():
    return x - y


def mult():
    return x * y


def part():
    return x / y
