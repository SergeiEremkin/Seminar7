# Сергей

'''
Комплексное число записывается в виде: z = re + im * i, где
         re - действительная часть
         im - мнимая часть
         i - мнимая единица
'''


def sum_complex(a_re, a_im, b_re, b_im):
    a = complex(a_re, a_im)
    b = complex(b_re, b_im)
    return a + b


def minus_complex(a_re, a_im, b_re, b_im):
    a = complex(a_re, a_im)
    b = complex(b_re, b_im)
    return a - b


def multiply_complex(a_re, a_im, b_re, b_im):
    a = complex(a_re, a_im)
    b = complex(b_re, b_im)
    return a * b


def partial_complex(a_re, a_im, b_re, b_im):
    a = complex(a_re, a_im)
    b = complex(b_re, b_im)
    return a / b

print(partial_complex(1,2,3,4))
