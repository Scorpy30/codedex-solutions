# Quadratic Equation 🧮
# Codédex solutions
# In this example, we will solve a quadratic equation of the form ax² + bx + c = 0 using the quadratic formula. The formula for finding the roots of a quadratic equation is:
# x = (-b ± √(b² - 4ac)) / (2a)

a = int(input("Enter coefficient 'a': "))
b = int(input("Enter coefficient 'b': "))
c = int(input("Enter coefficient 'c': "))

root1 = (-b + (b**2 - (4*a*c)**0.5)) / 2*a
root2 = (-b - (b**2 - (4*a*c)**0.5)) / 2*a

print("The roots are : ")
print(root1)
print(root2)