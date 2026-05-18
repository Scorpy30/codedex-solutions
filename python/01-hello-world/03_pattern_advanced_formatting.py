# Pattern Advanced 🔢
# Codédex solutions
# In this example, we will print a pattern of numbers using nested loops. The pattern will consist of 4 rows, with each row containing an increasing number of sequential numbers. The numbers will be right-aligned to create a visually appealing pattern.

current_num = 1
rows = 4

for i in range(1, rows + 1):
    # Create the string of numbers for the current row
    row_numbers = []
    for _ in range(i):
        row_numbers.append(str(current_num))
        current_num += 1
    row_str = " ".join(row_numbers)
    
    # Calculate padding based on the longest row (the last one)
    # The last row length approximation handles alignment for double digits
    print(f"{row_str:>11}")