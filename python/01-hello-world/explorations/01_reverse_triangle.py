# Reverse Triangles ◀️📐
# Codédex Explorations
# Exploring reverse triangle patterns using nested loops,
# alignment, formatting, and decreasing stream logic.


# ============================================================
# Helper Functions
# ============================================================

def section(title):
    print()
    print("|| " + "=" * 68 + " ||")
    print(f"   {title}")
    print("|| " + "=" * 68 + " ||")


def left_padding(spaces):
    print("  " * spaces, end="")


# ============================================================
# Pattern Functions
# ============================================================

def pattern_1a(rows):
    section("Pattern 1a : Left Aligned Reverse Stars Triangle")

    for i in range(rows, 0, -1):
        for _ in range(i):
            print("*", end=" ")
        print()


def pattern_1b(rows):
    section("Pattern 1b : Right Aligned Reverse Stars Triangle")

    for i in range(rows, 0, -1):

        left_padding(rows - i)

        for _ in range(i):
            print("*", end=" ")
        print()


def pattern_2a(rows):
    section("Pattern 2a : Left Aligned Reverse Repeated Numbers Triangle")

    for i in range(rows, 0, -1):
        for _ in range(i):
            print(i, end=" ")
        print()


def pattern_2b(rows):
    section("Pattern 2b : Right Aligned Reverse Repeated Numbers Triangle")

    for i in range(rows, 0, -1):

        left_padding(rows - i)

        for _ in range(i):
            print(i, end=" ")
        print()


def pattern_3a(rows):
    section("Pattern 3a : Left Aligned Reverse Descending Numbers Triangle")

    for i in range(rows, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def pattern_3b(rows):
    section("Pattern 3b : Right Aligned Reverse Descending Numbers Triangle")

    for i in range(rows, 0, -1):

        left_padding(rows - i)

        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


def pattern_4a(rows, starting_num):
    section("Pattern 4a : Hardcoded Width Formatting")

    current_num = starting_num

    for i in range(rows, 0, -1):

        for _ in range(i):

            if current_num > 0:

                # Hardcoded width formatting
                print(f"{current_num:>2}", end=" ")

                current_num -= 1

        print()


def pattern_4b(rows, starting_num):
    section("Pattern 4b : Dynamic Width Formatting")

    current_num = starting_num

    # Automatically calculates required width
    width = len(str(starting_num))

    for i in range(rows, 0, -1):

        print(" " * ((width + 1) * (rows - i)), end="")

        for _ in range(i):

            if current_num > 0:

                # Dynamic width formatting
                print(f"{current_num:>{width}}", end=" ")

                current_num -= 1

        print()


# ============================================================
# Menu
# ============================================================

def show_menu():

    print()
    print("============== Menu : Reverse Triangle Patterns ==============")
    print("1  - Left Aligned Reverse Stars Triangle")
    print("2  - Right Aligned Reverse Stars Triangle")
    print("3  - Left Aligned Reverse Repeated Numbers Triangle")
    print("4  - Right Aligned Reverse Repeated Numbers Triangle")
    print("5  - Left Aligned Reverse Descending Numbers Triangle")
    print("6  - Right Aligned Reverse Descending Numbers Triangle")
    print("7  - Hardcoded Width Formatting Triangle")
    print("8  - Dynamic Width Formatting Triangle")
    print("9  - Run All Patterns")
    print("0  - Exit")
    print("=======================================================")


# ============================================================
# Main Program
# ============================================================

if __name__ == "__main__":

    rows = int(input("Enter number of rows: "))
    starting_num = int(input("Enter starting number: "))

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            pattern_1a(rows)

        elif choice == "2":
            pattern_1b(rows)

        elif choice == "3":
            pattern_2a(rows)

        elif choice == "4":
            pattern_2b(rows)

        elif choice == "5":
            pattern_3a(rows)

        elif choice == "6":
            pattern_3b(rows)

        elif choice == "7":
            pattern_4a(rows, starting_num)

        elif choice == "8":
            pattern_4b(rows, starting_num)

        elif choice == "9":

            pattern_1a(rows)
            pattern_1b(rows)

            pattern_2a(rows)
            pattern_2b(rows)

            pattern_3a(rows)
            pattern_3b(rows)

            pattern_4a(rows, starting_num)
            pattern_4b(rows, starting_num)

        elif choice == "0":

            print("\nExiting program...")
            break

        else:
            print("\nInvalid choice. Please try again.")