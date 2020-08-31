# def lcm_naive(a, b):
#     for l in range(1, a*b + 1):
#         if l % a == 0 and l % b == 0:
#             return l

#     return a*b

def my_gcd(a, b):
    if b == 0:
        return a

    gcd = my_gcd(b, (a%b))
    return gcd

def my_lcm(a, b):
    mmc = (a*b)//(my_gcd(a, b))
    return mmc

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(my_lcm(a, b))