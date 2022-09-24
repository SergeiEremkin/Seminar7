from datetime import datetime as dt


def log(data, result):
    '''
    Записывает результат операций
    '''
    time = dt.now().strftime('%H:%M:%S')
    with open('log.log', 'a') as file:
        file.write('{}: {} = {}\n'
                   .format(time, data, result))
