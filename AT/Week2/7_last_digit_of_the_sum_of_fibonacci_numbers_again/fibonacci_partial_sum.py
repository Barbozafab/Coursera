# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

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

def my_fibonacci_partial_sum(m, n):
    s = my_fibonacci_sum(n) - my_fibonacci_sum(m-1)

    return s % 10

if __name__ == '__main__':
    m, n = map(int, input().split())
    print(my_fibonacci_partial_sum(m, n))