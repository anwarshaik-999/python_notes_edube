try:
    value=int(input('enter a number:'))
    print(1/value)
except:
    print('they say default except should always at the end')
except ValueError:
    print("value error")
except ZeroDivisionError:
    print('cannot perform division with zero')
#this shoots error as it is not the order to follow