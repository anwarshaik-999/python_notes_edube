#zeroDivisionError is spcl case in ArithmeticErro
try:
    1/0
except ZeroDivisionError:
    print('zero')
except ZeroDivisionError:
    print('zero2')
except ArithmeticError:
    print('Arithmetic')
print('first stop')
try:
    1/0

except ArithmeticError:
    print('Arithmetic')
except ZeroDivisionError:
    print('zero')
print('secondStop')
try:
    int(input())
    1/0
except (ArithmeticError,ValueError):
    print('error')
print('third stop')