# Саша
import user_interface
import operation_complex
import operation_rational
import logger
import check


def button_click():
    result = 0
    while True:
        number_choise = user_interface.get_choice(input('1 - для операций с комплесными числами: \n2 - для операций с рациональными числами: \n'))
        if number_choise == 1:
            a_re = user_interface.get_complex('Введите re первого числа: ')
            a_im = user_interface.get_complex('Введите im первого числа: ')
            b_re = user_interface.get_complex('Введите re второго числа числа: ')
            b_im = user_interface.get_complex('Введите im второго числа: ')
            operation_complex.init(a_re, a_im, b_re, b_im)
            operation_choise = user_interface.get_oper('+ - для сложения: \n- - для вычетания: \n* - для умножения: \n/ - для деления: \n')
            if operation_choise == '+':
              result = operation_complex.sum()
            if operation_choise == '-':   
              result = operation_complex.sub()
            if operation_choise =='*':
              result = operation_complex.mult()
            if operation_choise =='/':
              result = operation_complex.part()     
        
        elif number_choise == 2:
            a = user_interface.get_rational('Введите первое рациональное число: ')
            b = user_interface.get_rational('Введите второе рациональное число: ')
            operation_rational.init(a,b)
            operation_choise = user_interface.get_oper('+ - для сложения: \n- - для вычетания: \n* - для умножения: \n/ - для деления: \n')
            if operation_choise == '+':
              result = operation_complex.sum()
            if operation_choise == '-':   
              result = operation_complex.sub()
            if operation_choise =='*':
              result = operation_complex.mult()
            if operation_choise =='/':
              result = operation_complex.part()  

        user_interface.view_data(result, 'Результат')
        
       



    a_re = user_interface.get_complex(int(1))
    a_im =user_interface.get_complex(int(2))
    b_re =user_interface.get_complex(int(3))
    b_im =user_interface.get_complex(int(4))
    result = operation_complex.sum_complex(a_re, a_im, b_re, b_im)
    logger.complex_operation_logger(result)
    user_interface.view_data(result, expressiontitle='Сумма')
    
