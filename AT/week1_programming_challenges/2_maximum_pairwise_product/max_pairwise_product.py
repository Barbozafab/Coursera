import random

def max_pairwise_product(numbers):
    n = len(numbers)
    first, second = int(), int()
    for i in range (n):
        if numbers[i] > first:
            first, second = numbers[i], first
        elif numbers[i] > second:
            second = numbers[i]
    
    return first * second


def slow_test(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


if __name__ == '__main__':
   input_n = int(input())
   input_numbers = [int(x) for x in input().split()]
   print(max_pairwise_product(input_numbers))

    # while True:
    #     n = random.randint(2, 200)
    #     input_numbers = list()
    #     for _ in range(n):
    #         input_numbers.append(random.randint(0, 200000))
    #     print(f'Testing input: {input_numbers}')

    #     fast = max_pairwise_product(input_numbers)
    #     slow = slow_test(input_numbers)
    #     assert fast == slow, f'Test failed - Fast = {fast}, Slow = {slow}'