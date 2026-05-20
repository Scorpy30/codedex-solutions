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

# Future Exploration Ideas

- type casting
- formatted strings
- input handling
- variable swapping tricks
- large number operations
- memory/reference behavior
