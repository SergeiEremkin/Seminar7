#Андрей
import user_interface as ui

def sum_rational():
    x = ui.get_rational('Введите первое число: ')
    y = ui.get_rational('Введите второе число: ')
    condition = str(x) + ' + ' + str(y)
    calculating = x + y
    return calculating, condition

# x, y = sum_rational()
# ui.view_data(x, y)
