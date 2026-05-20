# Input Handling
# Codédex explorations

def add(num1, num2):
    return num1+num2

def difference(num1, num2):
    return num1-num2

def multiplication(num1, num2):
    return num1*num2

def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Cannot divide by zero")

if __name__ == "__main__":

    try:
        num1, num2 = map(int, input("Enter two numbers: ").split())
    except ValueError:
        print("Enter only integers")
        exit()

    # learnt to use exit() if not num2 not declared for input [2 3.0] and thus name error

    print("Sum = ",add(num1, num2))
    print(f"Difference = {difference(num1,num2)}")
    print("Product = "+str(multiplication(num1, num2)))
    print("Division = ",division(num1,num2)) # earlier left float(division()) which resulted in error
 


