#Денис

# 1)Проверка на число

# a(мнимая часть) + bi
# a = 2+3i

def type_checking_whole(get_number_whole):
  while type:
    try:
       get_number_whole=int(get_number_whole) 
       break
        
    except ValueError:
        return False

    except TypeError:
        return False    
        
  if isinstance (get_number_whole,int) ==True:
        return True


   
   

def type_checking_fractional(get_number_fractional):

    while type:
        try:
            get_number_fractional=float(get_number_fractional)
            break
        except ValueError:
            return False
        except TypeError:
            return False    

    if isinstance (get_number_fractional,float) ==True:
        return True
    


def input_number  ():
    get_input_number=input('Введите что нибудь') 
     
    return get_input_number
#print (type_checking_whole(input_number())==True )
print(type_checking_fractional(input_number())==True)    