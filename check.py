def get_number_int(input_string: str) -> int:
    '''
    Проверка целого числа
    '''
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print('Это не то ...')


def get_number_float(input_string: str) -> float:
    '''
    Проверка числа с плавающей точкой
    '''
    while True:
        try:
            num = float(input(input_string))
            return num
        except ValueError:
            print('Это не то ...')


def get_symbol(input_string: str) -> str:
    '''
    Проверка символа для действий
    '''
    while True:
        try:
            char = input(input_string)
            if char not in '+-/*':
                print('Не правильно!')
                continue
            return char
        except ValueError:
            print('Это не то ...')


def get_selection(input_string: str) -> int:
    '''
    Проверка числа для выбора результата
    '''
    while True:
        try:
            char = input(input_string)
            if char == '1':
                return int(char)
            if char == '2':
                return int(char)
            if char == '3':
                return int(char)
            print('Не правильно!')
            continue
        except ValueError:
            print('Это не то ...')


def get_ZeroDivisionError(num1,num2):
    num1=float(num1)
    num2=float(num2)
    if num2==0.0:
     return False
    else:
        return True 
        
def complex_get_ZeroDivisionError(a_re, a_im, b_re, b_im):
    x=0
    y=0
    x = complex(a_re, a_im)
    y = complex(b_re, b_im)
    if y==0:
        return False
    else :
        return True  


