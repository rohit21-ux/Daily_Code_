# 📅 Day 23 – map(), filter(), reduce()

## 🚀 Topics Covered
- Functional Programming Basics
- map()
- filter()
- reduce()
- Lambda with Functional Programming

---

# 🟢 1️⃣ map()

`map()` applies a function to every element of an iterable.

### 🔹 Syntax

```python
map(function, iterable)
```

### 🔹 Example

```python
nums = [1, 2, 3, 4]

squares = list(map(lambda x: x * x, nums))
print(squares)
```

### 🔹 Output
```
[1, 4, 9, 16]
```

---

# 🟢 2️⃣ filter()

`filter()` selects elements based on a condition.

### 🔹 Syntax

```python
filter(function, iterable)
```

### 🔹 Example

```python
nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)
```

### 🔹 Output
```
[2, 4, 6]
```

---

# 🟢 3️⃣ reduce()

`reduce()` reduces an iterable into a single value.

⚠ Must import from `functools`

### 🔹 Syntax

```python
from functools import reduce
reduce(function, iterable)
```

### 🔹 Example

```python
from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, nums)
print(total)
```

### 🔹 Output
```
10
```

---

# 🎯 Practice Problems

1. Convert all numbers in a list into strings using `map()`.
2. Filter numbers greater than 25 using `filter()`.
3. Find product of all numbers using `reduce()`.

---

# 🧠 Key Takeaways

- `map()` → Transform data
- `filter()` → Select data
- `reduce()` → Combine data into one value
- Often used with lambda functions
- Important for interviews and functional-style coding

---

