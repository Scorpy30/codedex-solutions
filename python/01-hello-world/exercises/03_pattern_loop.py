# Pattern Loop 🧩
# Codédex solutions
# In this example, we will use nested loops to print a pattern of numbers. The outer loop will control the number of rows, while the inner loop will print the numbers in each row.

num = 1
for i in range(1, 5):
    print("  " * (4 - i), end="")
    
    for _ in range(i):
        print(num, end=" ")
        num += 1
        
    print()
