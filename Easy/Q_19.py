import math
Q = int(input())

for _ in range(Q):
    N = int(input())
    sqrt_N = int(math.sqrt(N))
    if sqrt_N * sqrt_N == N:
        print("YES")
    else:
        print("NO")