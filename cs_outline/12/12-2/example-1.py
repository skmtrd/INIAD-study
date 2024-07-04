import math 

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: division by zero")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
    