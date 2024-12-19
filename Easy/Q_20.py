def count_operations(n):
    operations = 0
    while n != 0:
        digit_sum = sum(int(digit) for digit in str(n))
        n -= digit_sum
        operations += 1
    return operations

n = int(input())
print(count_operations(n))