import controller

def view_data(result, expressiontitle:str)->str:
    '''
    Вывод результата
    '''
    
    print(f'{expressiontitle} = {result}')

def get_complex(string_input: int)-> complex:
    '''
    Ввод комплексного числа 
    '''
    return complex(string_input)

def get_rational(string_input: str)-> str:
    '''
    Ввод рационального
    '''
    return input(string_input)

def get_oper()-> str:
    '''
    Выбор операции
    '''
