T = int(input())  
for i in range(1, T + 1):
    A = int(input())
    B = int(input())
    C = int(input())
    
    if A > B and A > C:
        print("Alice")
    elif B > C and B > A:
        print("Bob")
    else:
        print("Charlie")