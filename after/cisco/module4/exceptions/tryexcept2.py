try:
    # value=float(input('enter a number:'))
    # value=int(value)
    # in the above two lines there will be no issue with float values
    value=int(input('enter a number:'))
    print(1/value)
except ValueError:
    print("value error")
except ZeroDivisionError:
    print('cannot perform division with zero')
except:
    print('they say default except should always at the end')