# def fibonacci_sum_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current

#     return sum % 10

def my_fibonacci_sum(n):
    previous, current = 0, 1

    if n in [0, 1]:
        return n

    rem = n % 60
    if rem == 0:
        return rem

    for _ in range(2, rem + 3):
        previous, current = current, (previous + current) % 60

    return (current - 1) % 10

if __name__ == '__main__':
    n = int(input())
    print(my_fibonacci_sum(n))