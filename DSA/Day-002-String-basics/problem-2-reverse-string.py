def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result
print(reverse_string("Rohit")) # tihor
print("Hello"[::-1])