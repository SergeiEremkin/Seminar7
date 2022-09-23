from datetime import datetime as dt


def log(data, result):
    '''
    Записывает результат операций
    '''
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}: {} = {}\n'
                   .format(time, data, result))
