rows = 10

for i in range(1, rows + 1):

    # manual padding
    print(" " * (rows - i), end="")

    for _ in range(i):
        print(i, end=" ")

    print()

rows = 10

# Step 1: build all rows first
all_rows = []

for i in range(1, rows + 1):
    row_numbers = []

    for _ in range(i):
        row_numbers.append(str(i))

    row_str = " ".join(row_numbers)
    all_rows.append(row_str)


# Step 2: find widest row dynamically
width = len(all_rows[-1])


# Step 3: print centered rows
for row in all_rows:
    print(row.center(width))