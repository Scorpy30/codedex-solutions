num = 1
for i in range(1, 5):
    print("  " * (4 - i), end="")
    
    for _ in range(i):
        print(num, end=" ")
        num += 1
        
    print()
