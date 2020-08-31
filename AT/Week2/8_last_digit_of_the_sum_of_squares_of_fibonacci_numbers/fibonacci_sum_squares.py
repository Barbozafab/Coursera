# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

def my_fibonacci_sum_squares(n):
    if (n <= 1):
        return n

    fib_list = [i for i in range(n+2)]
    for i in range(2, n+2):
        fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % 10

    return (fib_list[-1] * fib_list[-2]) % 10

if __name__ == '__main__':
    n = int(input()) % 60
    print(my_fibonacci_sum_squares(n))