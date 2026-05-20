# Alphabetical Triangles 🔠🔺
# Codédex Explorations
# Exploring alphabetical triangle patterns using nested loops,
# alignment, formatting, and decreasing stream logic.


# ============================================================
# Helper Functions
# ============================================================

def section(title):
    print()
    print("|| " + "=" * 68 + " ||")
    print(f"   {title}")
    print("|| " + "=" * 68 + " ||")


def right_padding(spaces):
    print("  " * spaces, end="")

def center_padding(spaces):
    print(" " * spaces, end="")


# ============================================================
# Pattern Functions
# ============================================================

def pattern_1a(rows):
    section("Left Aligned Alphabetical Triangles")

    char_begin = input("Enter a letter to start pattern: ")

    # same letter repetition
    print("=== Same Letter Repetition Pattern ===")

    for i in range(1, rows + 1):
        print(((char_begin + " ") * i).strip()) # using strip() removes the extra spacing at the end
    print()

    # successive letters
    print("=== Successive Letters Pattern ===")
    for i in range(1, rows + 1):
        current = char_begin
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) + 1)
        print()
    print()
    

    # increasing stream letters
    print("=== Increasing Stream Logic Pattern ===")

    for i in range (1, rows + 1):
        for _ in range(i):
            print(char_begin, end=" ")
            char_begin = chr(ord(char_begin) + 1)
        print()


def pattern_1b(rows):
    section("Left Aligned Reverse Alphabetical Triangles")

    char_begin = input("Enter a letter to start pattern: ")

    # same letter repetition
    print("=== Same Letter Repetition Pattern ===")

    for i in range(rows, 0, -1):
        print(((char_begin + " ") * i).strip()) # using strip() removes the extra spacing at the end
    print()

    # successive letters
    print("=== Successive Letters Pattern ===")
    for i in range(rows, 0, -1):
        current = char_begin
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) + 1)
        print()
    print()

    # increasing stream letters
    print("=== Increasing Stream Logic Pattern ===")

    for i in range (rows, 0, -1):
        for _ in range(i):
            print(char_begin, end=" ")
            char_begin = chr(ord(char_begin) + 1)
        print()

    print("===================================================================")

    char_max = input(print("For a more fun way enter a high index letter: "))

    # preceding letters
    print("=== Preceding Letters Pattern ===")

    for i in range(rows, 0, -1):
        current = char_max
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) - 1)
        print()
    print()

    
    # decreasing stream letters
    print("=== Decreasing Stream Logic Pattern ===")

    for i in range (rows, 0, -1):
        for _ in range(i):
            print(char_max, end=" ")
            char_max = chr(ord(char_max) - 1)
        print()


def pattern_2a(rows):
    section("Right Aligned Alphabetical Triangles")

    char_begin = input("Enter a letter to start pattern: ")

    # same letter repetition
    print("=== Same Letter Repetition Pattern ===")

    for i in range(1, rows + 1):
        right_padding(rows - i)
        print(((char_begin + " ") * i).strip()) # using strip() removes the extra spacing at the end
    print()

    # successive letters
    print("=== Successive Letters Pattern ===")
    for i in range(1, rows + 1):
        current = char_begin
        right_padding(rows - i)
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) + 1)
        print()
    print()
    

    # increasing stream letters
    print("=== Increasing Stream Logic Pattern ===")

    for i in range (1, rows + 1):
        right_padding(rows - i)
        for _ in range(i):
            print(char_begin, end=" ")
            char_begin = chr(ord(char_begin) + 1)
        print()


def pattern_2b(rows):
    section("Right Aligned Reverse Alphabetical Triangles")

    char_begin = input("Enter a letter to start pattern: ")

    # same letter repetition
    print("=== Same Letter Repetition Pattern ===")

    for i in range(rows, 0, -1):
        right_padding(rows - i)
        print(((char_begin + " ") * i).strip()) # using strip() removes the extra spacing at the end
    print()

    # successive letters
    print("=== Successive Letters Pattern ===")
    for i in range(rows, 0, -1):
        right_padding(rows - i)
        current = char_begin
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) + 1)
        print()
    print()

    # increasing stream letters
    print("=== Increasing Stream Logic Pattern ===")

    for i in range (rows, 0, -1):
        right_padding(rows - i)
        for _ in range(i):
            print(char_begin, end=" ")
            char_begin = chr(ord(char_begin) + 1)
        print()

    print("===================================================================")

    char_max = input(print("For a more fun way enter a high index letter: "))

    # preceding letters
    print("=== Preceding Letters Pattern ===")

    for i in range(rows, 0, -1):
        right_padding(rows - i)
        current = char_max
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) - 1)
        print()
    print()

    
    # decreasing stream letters
    print("=== Decreasing Stream Logic Pattern ===")

    for i in range (rows, 0, -1):
        right_padding(rows - i)
        for _ in range(i):
            print(char_max, end=" ")
            char_max = chr(ord(char_max) - 1)
        print()

def pattern_3a(rows):
    section("Pyramidical Alphabetical Triangles")

    char_begin = input("Enter a letter to start pattern: ")

    # same letter repetition
    print("=== Same Letter Repetition Pattern ===")

    for i in range(1, rows + 1):
        center_padding(rows - i)
        print(((char_begin + " ") * i).strip()) # using strip() removes the extra spacing at the end
    print()

    # successive letters
    print("=== Successive Letters Pattern ===")

    for i in range(1, rows + 1):
        center_padding(rows - i)
        current = char_begin
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) + 1)
        print()
    print()
    

    # increasing stream letters
    print("=== Increasing Stream Logic Pattern ===")

    for i in range (1, rows + 1):
        center_padding(rows - i)
        for _ in range(i):
            print(char_begin, end=" ")
            char_begin = chr(ord(char_begin) + 1)
        print()


def pattern_3b(rows):
    section("Right Aligned Reverse Alphabetical Triangles")

    char_begin = input("Enter a letter to start pattern: ")

    # same letter repetition
    print("=== Same Letter Repetition Pattern ===")

    for i in range(rows, 0, -1):
        center_padding(rows - i)
        print(((char_begin + " ") * i).strip()) # using strip() removes the extra spacing at the end
    print()

    # successive letters
    print("=== Successive Letters Pattern ===")
    for i in range(rows, 0, -1):
        center_padding(rows - i)
        current = char_begin
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) + 1)
        print()
    print()

    # increasing stream letters
    print("=== Increasing Stream Logic Pattern ===")

    for i in range (rows, 0, -1):
        center_padding(rows - i)
        for _ in range(i):
            print(char_begin, end=" ")
            char_begin = chr(ord(char_begin) + 1)
        print()

    print("===================================================================")

    char_max = input(print("For a more fun way enter a high index letter: "))

    # preceding letters
    print("=== Preceding Letters Pattern ===")

    for i in range(rows, 0, -1):
        center_padding(rows - i)
        current = char_max
        for _ in range(i):
            print(current, end=" ")
            current = chr(ord(current) - 1)
        print()
    print()

    
    # decreasing stream letters
    print("=== Decreasing Stream Logic Pattern ===")

    for i in range (rows, 0, -1):
        center_padding(rows - i)
        for _ in range(i):
            print(char_max, end=" ")
            char_max = chr(ord(char_max) - 1)
        print()    


# ============================================================
# Menu
# ============================================================

def show_menu():
    print()
    print("============== Menu : Alphabetical Triangle Patterns ==============")
    print("1  - Left Aligned Alphabetical Triangles")
    print("2  - Left Aligned Reverse Alphabetical Triangles")
    print("3  - Right Aligned Alphabetical Triangles")
    print("4  - Right Aligned Reverse Alphabetical Triangles")
    print("5  - Pyramidical Alphabetical Triangles")
    print("6  - Reverse Pyramidical Alphabetical Triangles")
    print("7  - Run All Patterns")
    print("0  - Exit")
    print("==========================================================================")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))

    while(True):
        show_menu()

        choice = int(input("Enter your choice: "))

        match(choice):
            case 1: pattern_1a(rows)

            case 2: pattern_1b(rows)

            case 3: pattern_2a(rows)

            case 4: pattern_2b(rows)

            case 5: pattern_3a(rows)

            case 6: pattern_3b(rows)

            case 7: 
                pattern_1a(rows)
                pattern_1b(rows)
                pattern_2a(rows)
                pattern_2b(rows)
                pattern_3a(rows)
                pattern_3b(rows)

            case 0: 
                print('\nExiting Program...')
                break

            case _ :
                print('\nInvalid choice. Please try again.')
                break
