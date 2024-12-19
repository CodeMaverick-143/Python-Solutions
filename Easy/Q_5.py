import math
D,Q = map(int,input().split())
if Q == 0:
    print(-1)
else:
    print(math.floor(D/Q))