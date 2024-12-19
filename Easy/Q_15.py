def remove_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    result = ''.join([char for char in s if char not in vowels])
    return result

s = input()
print(remove_vowels(s))