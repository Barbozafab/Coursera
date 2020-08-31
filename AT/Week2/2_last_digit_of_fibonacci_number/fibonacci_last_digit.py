# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % 10

def get_fibonacci_last_digit(n, fib_list):
    if (n <= 1):
        return n

    for i in range(2, n+1):
        fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % 10

    return fib_list[-1]

if __name__ == '__main__':
    n = int(input()) % 60
    fib_list = [i for i in range(n+1)]
    print(get_fibonacci_last_digit(n, fib_list))