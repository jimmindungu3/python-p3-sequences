def print_fibonacci(length):
    fibonacci_list = []
    
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    else:
        fibonacci_list = [0, 1]

        for n in range(2, length):
            next_term = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_term)

        print(fibonacci_list)
