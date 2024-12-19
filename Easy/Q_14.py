import math

def sum_of_products(n):
    total_sum = 0
    for x in range(1, n + 1):
        y = math.floor(n / x)
        total_sum += x * y
    return total_sum

def main():
    T = int(input()) 
    for _ in range(T):
        N = int(input())
        print(sum_of_products(N))