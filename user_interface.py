def view_data(result, expressiontitle:str)->str:
    '''
    Вывод результата
    '''
    print(f'{expressiontitle} = {result}')

def get_complex(string_input: str)-> str:
    '''
    Ввод комплексного числа 
    '''
    return input(string_input)

def get_rational(string_input: str)-> str:
    '''
    Ввод рационального
    '''
    return input(string_input)

def get_oper()-> str:
    '''
    Выбор операции
    '''
