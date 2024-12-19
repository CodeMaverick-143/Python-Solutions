def lexicographically_min_string(N):
    result = []
    for i in range(N):
        if i % 2 == 0:
            result.append('a') 
        else:
            result.append('b') 
    return ''.join(result)


N = int(input())


print(lexicographically_min_string(N))