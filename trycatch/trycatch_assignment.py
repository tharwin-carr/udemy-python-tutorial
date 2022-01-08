try:
    gateway = "Gateway: Opened"
    x = '2' + 2
except TypeError as e:
    print(f'ERROR: must convert string to int')
finally:
    gateway = 'Gateway: Closed'
    print(gateway)