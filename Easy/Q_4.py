def even_or_odd(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print("even",end = " ")
        else:
            print("odd",end = " ")


n = int(input())
even_or_odd(n)