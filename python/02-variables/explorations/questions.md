# Exploration Questions

## [1. Type Casting](../explorations/01_type_casting.py)

Take:
- age as integer
- height as float
- marks as string

Convert them into different types and print:
- original value
- converted value
- type before conversion
- type after conversion

Example concepts:
```python
int()
float()
str()
type()
```

---

## [2. Formatted Strings](../explorations/02_formatted_strings.py)

Create a mini student profile card using formatted strings.

Expected output style:

```text
Name  : Tarush
Age   : 22
CGPA  : 9.24
```

Explore:
- f-strings
- alignment spacing
- decimal formatting

Bonus:
Print CGPA upto 2 decimal places only.

---

## [3. Input Handling](../explorations/03_input_handling.py)

Take two numbers from the user and:
- add
- subtract
- multiply
- divide

Then observe:
- what happens without type conversion
- what happens after using `int()` or `float()`

Bonus:
Try entering text instead of number.

---

## 4. Variable Swapping Tricks

Swap two variables using:

### Method 1
Temporary variable

### Method 2
Python shorthand swapping

Example:

```python
a, b = b, a
```

Then compare:
- readability
- simplicity
- number of lines

Bonus:
Try swapping 3 variables creatively.

---

## 5. Large Number Operations

Experiment with very large integers.

Examples:
- factorial-like multiplications
- powers using `**`
- very large additions

Questions:
- Does Python overflow like some languages?
- How large can integers become?

Bonus:
Print:

```python
2 ** 100
```

and observe the output size.

---

## 6. Memory / Reference Behavior

Experiment:

```python
a = 10
b = a
```

Then:

```python
a = 20
```

Check whether `b` changes.

Then repeat using lists:

```python
a = [1, 2]
b = a
```

Modify one list and observe:
- both changing together
- reference behavior

This introduces:
- mutable vs immutable objects
- references in memory

Bonus:
Use:

```python
id(variable)
```

to compare memory references.
