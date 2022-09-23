#Саша


from datetime import datetime as dt
from time import time

def complex_operation_logger(data):
    '''
    Записывает результат операции с комплексными числами в журнал логов
    '''
    time = dt.now()
    with open('mylog.log', 'a') as file: # Если сюда подставить 'w' вместо  'a', то журнал можно перезаписовать.
        file.write('{} <> result complex operation = {}\n'
                    .format(time, data))
        
def rational_operation_logger(data):
    '''
    Записывает результат операции с рациональными числами в журнал логов
    '''
    time = dt.now()
    with open('mylog.log', 'a') as file:
        file.write('{} <> result rational operation = {}\n'
                    .format(time, data))
        
# complex_operation_logger(45)
# rational_operation_logger(5)

