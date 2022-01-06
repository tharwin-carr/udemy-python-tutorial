'''
Advanced String Methods Part 2
'''

greetings = 'Welcome to the Python World'
# Joins
# print(greetings, ','.join('abcdefg'))
# print(greetings, ':'.join(('10', '15', '23')))

#Replace Functionality
new_greetings = greetings.replace('Welcome to',
                                  'Hello there and welcome to')
print(new_greetings)


# password = ' abc123! '
#
# if password.strip() == 'abc123!':
#     print('password is successful')
# else:
#     print('password is incorrect')