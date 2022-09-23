# Сергей
x = 0
y = 0

'''
Комплексное число записывается в виде: z = re + im * i, где
         re - действительная часть
         im - мнимая часть
         i - мнимая единица
'''

def init(a_re, a_im, b_re, b_im):
    global x
    global y
    x = complex(a_re, a_im)
    y = complex(b_re, b_im)


def sum_complex():
    return x + y


def minus_complex():
    return x - y


def multiply_complex():
    return x * y


def partial_complex():
    return x / y


init(2, 3, 4, 5)
print(x)
print(y)
print(sum_complex())
