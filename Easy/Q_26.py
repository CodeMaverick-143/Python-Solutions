def solve():
    T = int(input())
    for _ in range(T):
        X, Y, N, R = map(int, input().split())
        

        min_cost = X * N
        

        if min_cost > R:
            print(-1)
            continue
        

        max_cost = Y * N
        if max_cost <= R:
            print(0, N)
            continue
        
        p = (R - N * X) // (Y - X)
        

        normal_burgers = N - p
        premium_burgers = p
        
        print(normal_burgers, premium_burgers)


solve()
