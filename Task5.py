def factorial(number):
    if (number > 0) and (number < 2):
        return 1
    elif number >= 2:
        return number * factorial(number-1)
    else:
        return None


number = int(input("Enter a number: "))
print("Factorial of ", number, "is: ", factorial(number))