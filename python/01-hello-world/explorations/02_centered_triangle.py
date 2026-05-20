# Centered Triangles 🔼
# Codédex Explorations
# Exploring centered triangle patterns using nested loops,
# alignment, formatting, and decreasing stream logic.


# ============================================================
# Helper Functions
# ============================================================

def section(title):
    print()
    print("|| " + "=" * 68 + " ||")
    print(f"   {title}")
    print("|| " + "=" * 68 + " ||")


def padding(spaces):
    print(" " * spaces, end="")


# ============================================================
# Pattern Functions
# ============================================================

def pattern_1a(rows):
    section("Pattern 1a: Stars Pyramid")

    for i in range(1, rows+1):
        padding(rows - i)

        for _ in range(i):
            print("* ", end="")
        print()


def pattern_1b(rows):
    section("Pattern 1b: Reverse Stars Pyramid")

    for i in range(rows, 0, -1):
        padding(rows - i)

        for _ in range(i, 0, -1):
            print("* ", end="")
        print()


def pattern_2a(rows):
    section("Pattern 2a: Repeated Numbers Pyramid")

    for i in range(1, rows + 1):
        padding(rows - i)

        for _ in range(i):
            print(i, end=" ")
        print()


def pattern_2b(rows):
    section("Pattern 2b: Reverse Repeated Numbers Pyramid")

    for i in range(rows, 0, -1):
        padding(rows-i)

        for _ in range(i):
            print(i, end=" ")
        print()


def pattern_3a(rows):
    section("Pattern 3a: Descending Number Pyramid")

    for i in range(1, rows + 1):
        padding(rows - i)

        for j in range(1, i+1):
            print(j, end=" ")
        print()


def pattern_3b(rows):
    section("Pattern 3b: Reverse Descending Number Pyramid")

    for i in range(rows, 0, -1):
        padding(rows - i)

        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def pattern_4a(rows):
    section("Pattern 4a: Increasing Stream Logic Pyramid")

    number = 1
    for i in range(1, rows+1):
        padding(rows - i)

        for _ in range(i):
            print(number, end=" ")
            number+=1
        print()

def pattern_4b(rows):
    section("Pattern 4b: Decreasing Stream Logic Pyramid")

    number = 10
    for i in range(rows, 0, -1):
        padding(rows - i)

        for _ in range(i):
            print(number, end=" ")
            number-=1
        print()


# ============================================================
# Menu
# ============================================================

def show_menu():

    print()
    print("============== Menu : Centered Triangle Patterns : PYRAMIDS ==============")
    print("1  - Stars Pyramid")
    print("2  - Reverse Stars Pyramid")
    print("3  - Repeated Numbers Pyramid")
    print("4  - Reverse Repeated Numbers Pyramid")
    print("5  - Ascending Numbers Pyramid")
    print("6  - Descending Numbers Pyramid")
    print("7  - Increasing Stream Logic Pyramid")
    print("8  - Decreasing Stream Logic Pyramid")
    print("9  - Run All Patterns")
    print("0  - Exit")
    print("==========================================================================")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    rows = int(input("Enter number of rows: "))

    while True:
        show_menu()
        
        choice = int(input("Enter your choice: "))

        match(choice):
            case 1:
                pattern_1a(rows)

            case 2:
                pattern_1b(rows)

            case 3:
                pattern_2a(rows)

            case 4:
                pattern_2b(rows)

            case 5:
                pattern_3a(rows)
            
            case 6:
                pattern_3b(rows)

            case 7:
                pattern_4a(rows)
            
            case 8:
                pattern_4b(rows)

            case 9:
                pattern_1a(rows)
                pattern_1b(rows)
                pattern_2a(rows)
                pattern_2b(rows)
                pattern_3a(rows)
                pattern_3b(rows)
                pattern_4a(rows)
                pattern_4b(rows)

            case 0:
                print('\nExiting Program...')
                break;
            
            case _:
                print("\nInvalid Choice. Please try again.")
                break;
    