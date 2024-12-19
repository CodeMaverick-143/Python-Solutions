def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def smallest_multiple(N):
    result = 1
    for i in range(2, N + 1):
        result = lcm(result, i)
    return result


N = int(input())
print(smallest_multiple(N))