# Notes — 02 Variables

---

# Variable Basics

Variables store values in memory.

Example:

```python
name = "Tarush"
age = 22
height = 5.8
```

Python automatically determines the variable type.

---

# Reassigning Variables

Variables can be updated later.

Example:

```python
score = 10
score = 25
```

The old value gets replaced.

---

# Arithmetic Operations

```python
+   addition
-   subtraction
*   multiplication
/   division
%   modulus
**  power
```

Example:

```python
print(2 ** 3)
```

Output:

```text
8
```

`**` means:

```text
2 raised to the power 3
```

---

# Syntax Errors

Syntax errors happen when Python cannot understand the structure of the code.

Example:

```python
print("Hello"
```

Reason:

```text
missing closing bracket
```

---

# Type Errors

Type errors happen when incompatible data types are used together.

Example:

```python
"Age: " + 21
```

Python cannot combine:
- string
- integer

directly.

---

# Observation — Java vs Python Variables

Interesting comparison noticed while learning:

## Java

```java
int b;
System.out.println(b);
```

Error:

```text
variable b might not have been initialized
```

But:

```java
static int b;
System.out.println(b);
```

Output:

```text
0
```

Reason:
- static variables get default values
- local variables do not

---

## Python

Python variables must always be assigned before use.

Example:

```python
print(b)
```

Error:

```text
NameError: name 'b' is not defined
```

---

# Key Takeaways

- Python variables are dynamically typed
- variables can be reassigned easily
- `**` performs exponent operations
- syntax and type errors are different concepts
- Python variable handling is simpler than Java in many cases
- debugging small mistakes improves understanding faster

---

# What I Already Knew

This chapter was mostly revision, but it helped reinforce:
- variable syntax
- arithmetic operators
- debugging awareness
- language behavior comparisons

---

# Additional Notes from Explorations

---

# Formatted Strings & Alignment

Used formatted strings (`f-strings`) to create cleaner console output formatting.

Example:

```python
print(f"{'Enter Name':>25}: ", end="")
```

Concepts explored:
- left alignment `<`
- right alignment `>`
- center alignment `^`
- width formatting

Observation:
- very large widths create excessive spacing
- smaller widths create cleaner console UI formatting

---

# Input Handling & Validation

Explored safe input handling using:

```python
try:
```

and:

```python
except:
```

structures.

Example:

```python
try:
    num1, num2 = map(int, input().split())

except ValueError:
    print("Enter only integers")
```

Learned:
- invalid input can crash programs
- input validation improves program safety
- `exit()` can stop execution safely after invalid input

---

# Exception Handling

Explored multiple exception types.

## ValueError

Occurs when:
- correct type expected
- invalid value provided

Example:

```python
int("hello")
```

---

## ZeroDivisionError

Occurs when dividing by zero.

Example:

```python
10 / 0
```

Handled using:

```python
except ZeroDivisionError:
```

---

## Generic Exception Handling

Explored:

```python
except Exception as e:
```

Learned:
- `e` stores the actual error object
- useful for debugging unexpected issues

Example:

```python
print(e)
```

prints actual Python error messages.

---

# Function-Based Arithmetic Programs

Created arithmetic operations using separate functions.

Example:

```python
def add(num1, num2):
    return num1 + num2
```

Concepts reinforced:
- functions
- parameters
- return values
- modular programming

---

# String Concatenation vs f-Strings

Experimented with multiple output styles:

```python
print("Sum = ", value)
```

```python
print("Sum = " + str(value))
```

```python
print(f"Sum = {value}")
```

Observation:
- f-strings are cleaner and more readable

---

# Variable Swapping Explorations

Explored multiple swapping approaches.

## Temporary Variable Swap

```python
temp = b
b = a
a = temp
```

---

## Python Shorthand Swap

```python
a, b = b, a
```

Observation:
- Python swapping is shorter and cleaner

---

## Three Variable Swapping

Experimented with creative multi-variable swapping logic.

Also practiced:
- menu-driven programs
- `match-case`
- function-based structure
- repeated execution using `while True`

---

# Important Debugging Observations

## Missing `.split()`

Incorrect:

```python
a, b = map(int, input())
```

Correct:

```python
a, b = map(int, input().split())
```

Reason:
- `.split()` separates values into multiple parts

---

## Continuing After Failed Input

Without `exit()`:
- variables may remain undeclared
- program continues and causes `NameError`

Using:

```python
exit()
```

prevents further execution after invalid input.

---

# Understanding `.split()` with Strings vs `int()`

---

# Working Version

```python
num1, num2 = input("Enter two numbers: ").split()
```

Input:

```text
10 20
```

Step-by-step:

## Step 1 — `input()`

```python
"10 20"
```

This is a STRING.

---

## Step 2 — `.split()`

```python
"10 20".split()
```

becomes:

```python
['10', '20']
```

A LIST of strings.

---

## Step 3 — List Unpacking

```python
num1, num2 = ['10', '20']
```

Python automatically assigns:

```python
num1 = '10'
num2 = '20'
```

This is called:

```text
list unpacking
```

So this works correctly.

---

# Failing Version

```python
int(input().split())
```

Suppose input is:

```text
10 20
```

Then:

```python
input().split()
```

becomes:

```python
['10', '20']
```

Now Python tries:

```python
int(['10', '20'])
```

This means:

```text
"Convert this ENTIRE LIST into one integer"
```

which is invalid.

So Python raises:

```text
TypeError
```

or:

```text
ValueError
```

depending on context.

---

# Correct Integer Version

```python
num1, num2 = map(int, input().split())
```

Flow:

```text
input()
    ↓
"10 20"

split()
    ↓
['10', '20']

map(int, ...)
    ↓
[10, 20]

unpacking
    ↓
num1 = 10
num2 = 20
```

---

# Key Difference

## This Works

```python
num1, num2 = ['10', '20']
```

because Python can unpack lists.

---

## This Fails

```python
int(['10', '20'])
```

because Python cannot convert an ENTIRE LIST into one integer.

---

# Mental Model

```text
split() → separates values into a list
map(int, ...) → converts EACH item individually
```

# Key Takeaways from Explorations

- input handling is extremely important
- debugging teaches concepts deeply
- exception handling prevents crashes
- Python provides very compact syntax for many operations
- formatted strings improve readability significantly
- functions make programs cleaner and modular
- f-strings are usually the cleanest output method
- safe programs think about invalid inputs beforehand


# Future Exploration Ideas

- type casting
- formatted strings
- input handling
- variable swapping tricks
- large number operations
- memory/reference behavior
