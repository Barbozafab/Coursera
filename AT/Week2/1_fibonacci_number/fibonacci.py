def calc_fib(n, fib_list):
    if (n <= 1):
        return n

    for i in range(2, n+1):
        fib_list[i] = fib_list[i-1] + fib_list[i-2]

    return fib_list[-1]

n = int(input())
fib_list = [i for i in range(n+1)]
print(calc_fib(n, fib_list))