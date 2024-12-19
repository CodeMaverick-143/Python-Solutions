a,b,c = map(int,input().split())
if a > b and a > c and b > c:
    print(3,1)
elif a > b and a > c and c > b:
    print(2,1)
elif b > a and b > c and a > c:
    print(3,2)
elif b > a and b > c and c > a:
    print(1,2)
elif c > a and c > b and a > b:
    print(2,3)
else:
    print(1,3)