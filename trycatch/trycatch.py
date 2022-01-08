'''
Errors & Exceptions (Try Catch
'''

try:
    # x = 10 * (1 / 0)
    x = '2' + 2
    print(x)

except ZeroDivisionError as e:
    print(f'{e} : Cannot Divide by 0!')
except TypeError as e:
    print(f'{e} Type Error')
except Exception as e:
    print(f'ERROR WAS THROWN {e}')