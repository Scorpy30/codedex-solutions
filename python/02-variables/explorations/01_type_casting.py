# Type Casting
# Codédex explorations

age = int(input("Enter your age: "))
height = float(input("Enter your height(in cm): "))
marks = input("Your total marks scored on last test: ")

# printing original values:
print("=== Original Values ===")
print(age)
print(height)
print(marks)

# types before conversion
print("=== Types Before Conversion ===")
print(type(age))
print(type(height))
print(type(marks))

# conversion
age = float(age)
height = str(height)
marks = int(marks)

# printing after type casting:
print(age)
print(height)
print(marks)

# types after conversion:
print(type(age))
print(type(height))
print(type(marks))