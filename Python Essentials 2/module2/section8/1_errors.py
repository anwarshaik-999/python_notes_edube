#BaseException ← Exception ← ArithmeticError
#eg:it contains errors like zerodivision


#BaseException ← Exception ← AssertionError
#raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string

#BaseException
#it is parent of all

#BaseException ← Exception ← LookupError ← IndexError
#[1,2,3,4][5]

# BaseException ← KeyboardInterrupt
#when ctrl+c is pressed

# BaseException ← Exception ← LookupError
#caused by errors resulting from invalid references to different collections (lists, dictionaries, tuples, etc.)
def lookup():
    try:
        dic={
            'key':'value'
        }
        print(dic['asdf'])
    except LookupError as e:
        print(type(e))
#lookup() #<class 'KeyError'>

#BaseException ← Exception ← MemoryError
#raised when an operation cannot be completed due to a lack of free memory.
def memError():
    string='sfs'
    try:
        while True:
            string+=string*10000000
    except MemoryError:
        print('Memory Error')
#memError() #Memory Error

#BaseException ← Exception ← ArithmeticError ← OverflowError
#raised when an operation produces a number too big to be  stored
import math
def Overflow():
    try:
        ex=1
        while True:
            print(math.exp(ex))
            ex+=200
    except OverflowError:
        print('error')
Overflow() #error after many numbers
'''
2.718281828459045
1.964223318681796e+87
1.419342617553556e+174
1.0256132522424933e+261
error
'''

#BaseException ← Exception ← StandardError ← ImportError
#when an import operation fails
#eg:import asdfsfdsg