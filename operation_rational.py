from operation_complex import summ, sub, mult, part
x = 1
y = 1

'''
Рациональные числа - числа с дробной частью
Иницилизация рационального числа. Операции с числами находятся в модуле operation_complex чтобы не дублировать код
'''

def init(a, b):
    global x
    global y
    x = float(a)
    y = float(b)

summ()

sub()

mult()

part()

  
