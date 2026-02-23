# 📅 Day 22 – List Comprehension & Lambda Functions

## 🚀 Topics Covered
- List Comprehension
- Conditional List Comprehension
- Lambda Functions
- Lambda with Sorting

---

# 🟢 1️⃣ List Comprehension

List comprehension is a shorter and cleaner way to create lists.

### 🔹 Normal Method

```python
squares = []
for i in range(1, 6):
    squares.append(i * i)

print(squares)
```

### 🔹 Using List Comprehension

```python
squares = [i * i for i in range(1, 6)]
print(squares)
```

### 🔹 Syntax

```python
[expression for item in iterable]
```

---

# 🟢 2️⃣ List Comprehension with Condition

```python
even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)
```

---

# 🟢 3️⃣ Lambda Functions

Lambda is an anonymous (unnamed) function.

### 🔹 Normal Function

```python
def square(x):
    return x * x
```

### 🔹 Lambda Version

```python
square = lambda x: x * x
print(square(5))
```

### 🔹 Syntax

```python
lambda arguments: expression
```

---

# 🟢 4️⃣ Lambda with Sorting

```python
students = [
    ("Rohit", 85),
    ("Amit", 90),
    ("Raj", 75)
]

students.sort(key=lambda x: x[1])
print(students)
```

---

# 🎯 Practice Problems

1. Create a list from 1–20 containing only numbers divisible by 3.
2. Sort a list in descending order using lambda.
3. Convert all words in a list to uppercase using list comprehension.

---

# 🧠 Key Takeaways

- List comprehension makes code cleaner and faster.
- Lambda functions are useful for short, temporary functions.
- Commonly used in sorting and functional programming.
- Very important for DSA and interviews.

---

