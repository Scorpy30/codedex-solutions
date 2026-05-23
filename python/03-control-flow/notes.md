# Python Quiz System Notes 📋

## Concepts Learned

---

# 0 Input Validation Using While Loop

Example:

```python
answer = 0

while answer not in [1, 2]:
    answer = int(input("Enter 1 or 2: "))
```

This prevents invalid choices.

---

# 0.1 Match-Case Statements

`match-case` is similar to switch-case in other languages.

Example:

```python
option = int(input("Enter choice: "))

match option:
    case 1:
        print("You selected 1")
    case 2:
        print("You selected 2")
    case _:
        print("Invalid choice")
```

---

# 0.2 Match-Case Observations

- Cleaner alternative to long `if-elif-else`
- Useful for menus and option handling
- `_` acts as default case
- Introduced in Python 3.10+

---

# 0.3 Input Handling Observations

We explored:

```python
input()
int(input())
```

Important realization:

```python
input()
```

always returns a string.

Example:

```python
age = input("Enter age: ")
print(type(age))
```

Output:

```python
<class 'str'>
```

Need conversion:

```python
age = int(input("Enter age: "))
```

---

# 0.4 Common Input Handling Problems

## ValueError

Occurs when invalid conversion happens.

Example:

```python
int("hello")
```

This crashes because `"hello"` is not a number.

Future improvement planned:
- `try-except`
- safer validation loops

---

# 1. Lists

A list stores multiple items in order.

Example:

```python
questions = [ ... ]
```

Access using indexes:

```python
questions[0]
questions[1]
```

Indexes start from `0`.

---

# 2. Dictionaries

A dictionary stores data in key-value pairs.

Example:

```python
student = {
    "name": "Tarush",
    "age": 21
}
```

Access using keys:

```python
student["name"]
```

---

# 3. Nested Data Structures

We created:

- list of dictionaries
- dictionary inside dictionary

Example:

```python
questions = [
    {
        "question": "Capital of India?",
        "options": {
            1: "New Delhi",
            2: "Mumbai"
        },
        "answer": 1
    }
]
```

Structure visualization:

```text
questions (list)
│
├── dictionary
│      ├── question
│      ├── options (dictionary)
│      └── answer
```

---

# 4. Difference Between Lists and Dictionaries

## Lists

Use indexes:

```python
mylist[0]
```

## Dictionaries

Use keys:

```python
mydict["name"]
```

---

# 5. Dictionary Keys Are Case-Sensitive

These are different:

```python
"Question"
"question"
```

Wrong key causes:

```python
KeyError
```

---

# 6. Duplicate Dictionary Keys

Dictionary keys must be unique.

Wrong:

```python
{
    "question": "Q1",
    "question": "Q2"
}
```

Python keeps only the latest value.

---

# 7. Looping Through Dictionaries

Using `.items()`:

```python
for number, option in q["options"].items():
    print(number, option)
```

`.items()` returns:

```python
(key, value)
```

pairs.

---

# 8. Dynamic Quiz Logic

We used:

```python
for house in score:
```

to make each house attempt the quiz.

Then:

```python
for q in questions:
```

to ask every question.

---

# 9. Score Updating

Correct:

```python
score[house] += 1
```

Meaning:

```python
score[house] = score[house] + 1
```

---

# 10. Common Errors Learned

## KeyError

Occurs when dictionary key does not exist.

Example:

```python
student["marks"]
```

if `"marks"` key is absent.

---

## IndexError

Occurs when list index does not exist.

Example:

```python
mylist[10]
```

---

## TypeError

Example:

```python
points[house]
```

when `points` is an integer.

Integers cannot use indexing.

---

# 11. Better Data Modeling

Instead of:

```python
"Q1"
"Q2"
"Q3"
```

use consistent keys:

```python
"question"
```

This makes loops scalable.

---

# 12. Realizations

This project introduced:

- data modeling
- scalable structures
- nested access
- validation logic
- dynamic looping

These concepts are foundational for:

- backend development
- APIs
- databases
- JSON structures
- object-oriented programming later