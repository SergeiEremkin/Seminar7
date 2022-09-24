import check as ch


def view_data(result) -> str:
    '''
    Вывод результата
    '''
    print(result)


def get_rational(num: int) -> float:
    '''
    Ввод рационального числа
    '''
    string_input = f'Введите {ch.num_to_word(num)} число: '
    number = ch.get_number_float(string_input)
    return number


def get_complex(num: str) -> complex:
    '''Ввод комплексного числа'''
    input_re = f'Введите Re {ch.num_to_word(num)} числa: '
    input_im = f'Введите Im {ch.num_to_word(num)} числa: '
    re = ch.get_number_int(input_re)
    im = ch.get_number_int(input_im)
    return re, im


def get_oper(string_input: str) -> str:
    '''
    Выбор операции
    '''
    symbol = ch.get_symbol(string_input)
    return symbol


def get_choice(string_input: str) -> int:
    '''
    Выбор действия или вида чисел
    '''
    choice = ch.get_selection(string_input)
    return choice
