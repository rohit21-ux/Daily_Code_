def count_vowels(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count
    
print(count_vowels("HelloWorld")) # 3

# another method
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("ROhitjAgavE")) 


