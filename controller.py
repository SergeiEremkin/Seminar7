# Саша
import user_interface
import operation_complex
import operation_rational
import logger



def button_click():
    a_re = user_interface.get_complex(int(1))
    a_im =user_interface.get_complex(int(2))
    b_re =user_interface.get_complex(int(3))
    b_im =user_interface.get_complex(int(4))
    result = operation_complex.sum_complex(a_re, a_im, b_re, b_im)
    logger.complex_operation_logger(result)
    user_interface.view_data(result, expressiontitle='Сумма')
    
