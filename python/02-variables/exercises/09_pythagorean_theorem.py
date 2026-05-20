# Pythagorean Theorem 📐
# Codédex solutions
# In this example, we will calculate the length of the hypotenuse of a right triangle using the Pythagorean theorem. The formula can be expressed as:
# c = √(a² + b²)

a = int(input("Enter length of a short side: "))
b = int(input("Enter length of another short side: "))

c = (a ** 2 + b ** 2) ** 0.5

print("Length of Hypotenuse is : ", c)