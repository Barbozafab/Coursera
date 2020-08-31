# def gcd_naive(a, b):
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

def my_gcd(a, b):
    if b == 0:
        return a

    gcd = my_gcd(b, (a%b))
    return gcd

if __name__ == "__main__":
    a, b = map(int, input().split())
    if a < b:
        a, b = b, a
    print(my_gcd(a, b))