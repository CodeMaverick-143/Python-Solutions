def min_changes_to_palindrome(S):
    n = len(S)
    count = 0

    for i in range(n // 2):
        if S[i] != S[n - i - 1]:
            count += 1
    return count


S = input()
print(min_changes_to_palindrome(S))