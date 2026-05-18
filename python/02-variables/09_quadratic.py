# Quadratic Equation 🧮
# Codédex solutions

a = int(input("Enter coefficient 'a': "))
b = int(input("Enter coefficient 'b': "))
c = int(input("Enter coefficient 'c': "))

root1 = (-b + (b**2 - (4*a*c)**0.5)) / 2*a
root2 = (-b - (b**2 - (4*a*c)**0.5)) / 2*a

print("The roots are : ")
print(root1)
print(root2)