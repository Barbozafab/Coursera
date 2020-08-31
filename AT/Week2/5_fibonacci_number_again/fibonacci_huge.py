# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current

#     return current % m

# def my_get_fibonacci_huge(n, m, fib_list):
#     if (n <= 1):
#         return n

#     for i in range(2, n+1):
#         fib_list[i] = fib_list[i-1] + fib_list[i-2]

#     return fib_list[-1] % m

def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m**2):
        previous, current = current, (previous + current) % m

        if previous == 0 and current == 1:
            return i+1

def my_get_fibonacci_huge(n, m):
    pisano_period = get_pisano_period(m)
    n = n % pisano_period

    if n in [0, 1]:
        return n
    
    previous, current = 0, 1
    for _ in range(n-1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(my_get_fibonacci_huge(n, m))