# Variable Swapping
# Codédex explorations
def fun_print(a, b):
    print(f"1st Number : {a}")
    print(f"2nd Number : {b}")

def temp_swap(a,b):
    temp = b
    b = a
    a = temp
    fun_print(a,b)

def python_swap(a,b):
    a, b = b, a
    fun_print(a, b)

def three_swap(a, b):
    try:
        c = int(input("Enter a third integer: "))
    except ValueError:
        print("Only integers accepted")
        exit()
    
    print("Before Swap=>")
    print(f"1st number : {a}\n2nd number : {b}\n3rd number : {c}")
    a, b = b, a
    b, c = c, b
    print("After Swap=>")
    print(f"1st number : {a}\n2nd number : {b}\n3rd number : {c}")



def show_menu():
    print("1. Swap two variables using a temporary variable")
    print("2. Swap two variabbles using Python shorthand swapping")
    print("3. Swap three variables creatively")
    print("0. Exit Program")

if __name__ == "__main__":

    try:
        a, b = map(int, input("Enter two integer variables: ").split())
    except ValueError:
        print("Enter only integers")
        exit()

    fun_print(a,b)

    while True:
        show_menu()

        choice = int(input("Enter your choice: "))

        match(choice):
            case 1: temp_swap(a,b)
            case 2: python_swap(a,b)
            case 3: three_swap(a,b)
            case 0: exit()
            case _:
                print("Invalid choice")
                exit()
