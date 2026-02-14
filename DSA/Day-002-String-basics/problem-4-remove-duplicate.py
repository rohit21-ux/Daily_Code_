def remove_duplicate_optimized(s):
    result = ""
    seen = set()

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result += ch    
    return result

print(remove_duplicate_optimized("missisippi"))