import check as ch


def view_data(result, expressiontitle: str) -> str:
    '''
    Вывод результата
    '''
    print(f'{expressiontitle} = {result}')


def get_rational(string_input: str) -> float:
    '''
    Ввод рационального числа
    '''
    number = ch.get_number_float(string_input)
    return number


def get_complex(string_input: str) -> complex:
    '''Ввод комплексного числа'''
    number = ch.get_number_int(string_input)
    return (number)


def get_oper(string_input: str) -> str:
    '''
    Выбор операции
    '''
    symbol = ch.get_symbol(string_input)
    return symbol


def get_choice(string_input:str) -> int:
    '''
    Выбор действия или вида чисел
    '''
    choice = ch.get_selection(string_input)
    return choice

# num = get_choice('Введите число\n:')
# print(num)
