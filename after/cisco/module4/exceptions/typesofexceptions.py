def getcode():
    mycode=[]
    while True:
        print('>>>' ,end='') if not mycode else print('...',end='')
        x=input()
        print(mycode)
        if x :
            mycode.append(x)
        else:
            break
    mycode='\n'.join(mycode)
    print(mycode)
    return mycode
try:
    #print(1/0)
    y=float(input('enter any number'))
    #print([1,2,3][y])
    #print([1,2,3].depend(4))
    exec(getcode())
except ZeroDivisionError:
    print('division with zero is not possible')
except ValueError:
    print('value eroor')
except TypeError:
    print('type error')
except AttributeError:
    print('attribute error')
except NameError:
    print('this is name error')
except SyntaxError:
    print('something wrong with the syntax')