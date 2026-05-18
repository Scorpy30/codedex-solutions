# Notes — 01 Hello World

## 03_pattern_loop.py

### Keeping Output on the Same Line

```python
print(" " * (4 - i), end="")
```

We use `end=""` so the cursor stays on the same line after printing.

Normally, `print()` automatically moves to a new line.

Example:

```python
print(1)
print(2)
```

Output:

```text
1
2
```

But:

```python
print(1, end="")
print(2)
```

Output:

```text
12
```

---

### Using Spaces Between Numbers

```python
print(num, end=" ")
```

We use:

```python
end=" "
```

to:
- keep printing on the same line
- add a space after each number

This avoids numbers sticking together.

Without space:

```text
78910
```

With space:

```text
7 8 9 10
```

---

## Why We Use `_` in the Inner Loop

```python
for _ in range(i):
```

We use `_` (underscore) when:
- we need the loop to repeat
- but we do NOT need the loop variable itself

It is a common Python convention meaning:

> "I only care about repetition, not the variable value."

Example:

```python
for _ in range(3):
    print("Hello")
```

Output:

```text
Hello
Hello
Hello
```

---

# 03_pattern_advanced.py

## The Formatting Approach

This approach builds each row as a single string and aligns it neatly.

Instead of printing numbers one-by-one directly, we:
1. store numbers in a list
2. combine them into a string
3. format the alignment

---

## Step-by-Step Breakdown

### Creating an Empty List

```python
row_numbers = []
```

Stores numbers for the current row.

---

### Adding Numbers to the List

```python
row_numbers.append(str(current_num))
```

- converts number to string
- adds it to the list

Example:

```python
['4', '5', '6']
```

---

### Joining Numbers Together

```python
" ".join(row_numbers)
```

Combines list items using spaces.

Example:

```python
['4', '5', '6']
```

becomes:

```text
4 5 6
```

---

### Right Alignment Formatting

```python
f"{row_str:>11}"
```

This means:

- make total width = 11 characters
- `>` means right-align text
- Python automatically adds spaces to the left

---

## Alignment Difference

```text
          1
        2 3
      4 5 6
   7 8 9 10
```

The formatting approach gives cleaner alignment for larger numbers.

---

# Pip

`pip` is Python's package manager.

It is used to install external libraries/packages from PyPI (Python Package Index).

Install a package:

```bash
pip install package-name
```

Example:

```bash
pip install numpy
```

---

# Further Exploration Ideas

- Make spacing automatically adapt for 3-digit or larger numbers
- Center-align patterns
- Reverse the triangle direction
- Print patterns like:
  - `1 22 333 4444`
  - `a`
    `b c`
    `d e f`
  - `a`
    `a b`
    `a b c`
- Trace variable values step-by-step
- Rewrite without inner loops
- Create new pattern challenges
- Dynamically calculate alignment width instead of hardcoding `11`