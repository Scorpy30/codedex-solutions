# Input Handling
# Codédex explorations


def add(num1, num2):
    return num1 + num2


def difference(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


if __name__ == "__main__":

    try:

        # taking integer input
        num1, num2 = map(int, input("Enter two numbers: ").split())

        print(f"Sum = {add(num1, num2)}")
        print(f"Difference = {difference(num1, num2)}")
        print(f"Product = {multiplication(num1, num2)}")
        print(f"Division = {division(num1, num2)}")

    except ValueError:
        print("Enter only integers")

    except ZeroDivisionError:
        print("Cannot divide by zero")

    except Exception as e:
        print("Unexpected Error:", e)