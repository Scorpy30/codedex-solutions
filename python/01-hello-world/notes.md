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

---

# [`explorations/03_alphabetical_pattern.py`] (explorations/03_alphabetical_pattern.py)

## Using `.strip()` to Remove Extra Spaces

When building patterns like:

```python
print((char + " ") * i)
```

Python leaves an extra space at the end.

Example:

```text
a 
a a 
a a a 
```

To clean the output:

```python
print(((char + " ") * i).strip())
```

`.strip()` removes extra spaces from:

* beginning
* end

Final output becomes:

```text
a
a a
a a a
```

---

## Understanding `ord()` and `chr()`

Python characters internally map to ASCII / Unicode numbers.

### `ord()`

Converts character → number

Example:

```python
ord('a')
```

Output:

```text
97
```

---

### `chr()`

Converts number → character

Example:

```python
chr(97)
```

Output:

```text
a
```

---

## Moving Forward Through Alphabets

```python
chr(ord(current) + 1)
```

Steps:

1. convert character to number
2. add 1
3. convert back to character

Example:

```python
'a' → 97 → 98 → 'b'
```

Used for:

```text
a b c d
```

style patterns.

---

## Moving Backward Through Alphabets

```python
chr(ord(char_max) - 1)
```

Steps:

1. convert character to number
2. subtract 1
3. convert back to character

Example:

```python
'd' → 100 → 99 → 'c'
```

Used for reverse patterns like:

```text
j i h g
f e d
c b
a
```

---

## Continuous Stream Logic

Important concept learned:

### WRONG APPROACH

```python
char_max = chr(ord(char_begin) - 1)
```

This keeps resetting the character from the original value.

---

### CORRECT APPROACH

```python
char_max = chr(ord(char_max) - 1)
```

This decreases continuously from the CURRENT character.

This creates proper stream flow across rows.

---

## String Multiplication in Python

Python allows multiplying strings.

Example:

```python
"a" * 4
```

Output:

```text
aaaa
```

Used in patterns like:

```python
(char + " ") * i
```

---

## Useful Pattern-Building Concepts Learned

* nested loops
* alignment using spaces
* controlling newline behavior with `end=""`
* string multiplication
* ASCII character manipulation
* continuous stream logic
* formatting cleaner output using `.strip()`
* increasing vs decreasing alphabet streams
* resetting vs continuously updating variables
* using `_` when loop variable is unnecessary

---

## Future Exploration Ideas

* automatic pyramid centering
* mirrored alphabetical pyramids
* diamond patterns
* alternating uppercase/lowercase streams
* skipping alphabets (`a c e g`)
* wrapping after `z`
* dynamically aligned alphabet pyramids
* recursive pattern generation
* pattern generation without nested loops
