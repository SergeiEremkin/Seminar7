#Саша

def complex_operation_logger(data):
    with open ('log.csv', 'a') as file:
        file.writelines(f'{data}')