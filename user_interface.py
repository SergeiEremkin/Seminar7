import check as ch
from colorama import Fore, Style


def view_data(result) -> str:
    '''
    Вывод результата
    '''
    print(f'Результат = {result}\n')


def get_rational(num: int) -> float:
    '''
    Ввод рационального числа
    '''
    string_input = Fore.GREEN + Style.BRIGHT + \
        f'Ввод {ch.num_to_word(num)} числа: '
    number = ch.get_number_float(string_input)
    return number


def get_complex(num: str) -> complex:
    '''Ввод комплексного числа'''
    input_re = Fore.GREEN + Style.BRIGHT + \
        f'Ввод Re {ch.num_to_word(num)} числa: '
    input_im = Fore.GREEN + Style.BRIGHT + \
        f'Ввод Im {ch.num_to_word(num)} числa: '
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
