#Денис

# 1)Проверка на число

# a(мнимая часть) + bi
# a = 2+3i

def get_number_int(input_string:str)->int:
    '''
    Проверка целого числа
    '''
    while True:
        try:
            num = int(input(input_string))
            return num
        except ValueError:
            print('Это не то ...')

def get_number_float(input_string:str)->float:
    '''
    Проверка числа с плавающей точкой
    '''
    while True:
        try:
            num = float(input(input_string))
            return num
        except ValueError:
            print('Это не то ...')

def get_symbol(input_string:str)-> str:
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

def get_selection(input_string:str)-> int:
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
            print('Не правильно!')
            continue
        except ValueError:
            print('Это не то ...')

# n = get_selection(':')
# print(n)
