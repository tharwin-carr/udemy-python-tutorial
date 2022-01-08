'''
Errors & Exceptions (Finally)
'''

try:
    x = None
    if x is None:
        raise Exception

except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(f'x is None, could not find answer')