def fibonacci_sequence(amount):
    n1 = 0
    n2 = 1

    if amount <= 0:
        print('please change to a positive int')
    elif amount == 1:
        print('Fib Seq: ')
        print(n1)
    else:
        print('Fib Seq: ')
        count = 0
        while count < amount:
            print(n1)
            fib_sum = n1 + n2
            n1 = n2
            n2 = fib_sum
            count += 1

fibonacci_sequence(13)
