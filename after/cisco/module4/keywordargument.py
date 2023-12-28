def func(first_name,seconde_name,age):
    print('hello',first_name+seconde_name,'you are',age)
func(seconde_name=' anwar',first_name='shaik',age=19)
#in python there are two types of giving arguments positional i.e func('anwar','shaik',19)
#another is func(seconde_name=' anwar',first_name='shaik',age=19)
#we can mix these two like keyword followed by positional but not __positional followed by keyword__
#eg:func(seconde_name=' anwar',first_name='shaik',19)-->throws error