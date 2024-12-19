n = int(input())
def LeapYear(n):
    if n % 400 == 0:
        print("YES")
    elif n %100 == 0:
        print("NO")
    elif n % 4 == 0:
        print("YES")
    else:
        print("NO")


LeapYear(n)