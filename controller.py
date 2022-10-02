import os
import user_interface
import operation_complex
import operation_rational
import logger
from colorama import Fore, Style


'''
В контроллере собираем логику из модулей operation_complex и operation_rational и интерфейс из user_interface
'''


def button_click():
    os.system('cls||clear')
    result = 0
    while True:
        number_choise = user_interface.get_choice(
            Fore.BLUE+Style.BRIGHT + '1 - для операций с комплесными числами: \n2 - для операций с рациональными числами: \n3 - для выхода \n')
        if number_choise == 1:
            a = user_interface.get_complex(1)
            b = user_interface.get_complex(2)
            operation_complex.init(a[0], a[1], b[0], b[1])
            operation_choise = user_interface.get_oper(
                '+ - для сложения: \n- - для вычетания: \n* - для умножения: \n/ - для деления: \n')
            if operation_choise == '+':
                result = operation_complex.summ()
            if operation_choise == '-':
                result = operation_complex.sub()
            if operation_choise == '*':
                result = operation_complex.mult()
            if operation_choise == '/':
                result = operation_complex.part()
        elif number_choise == 2:
            a = user_interface.get_rational(1)
            b = user_interface.get_rational(2)
            operation_rational.init(a, b)
            operation_choise = user_interface.get_oper(
                Fore.CYAN+Style.BRIGHT + '+ - для сложения: \n- - для вычетания: \n* - для умножения: \n/ - для деления: \n')
            if operation_choise == '+':
                result = operation_rational.summ()
            if operation_choise == '-':
                result = operation_rational.sub()
            if operation_choise == '*':
                result = operation_rational.mult()
            if operation_choise == '/':
                result = operation_rational.part()
        else:
            break
        user_interface.view_data(result)
        logger.log(result, 'ValueError')
