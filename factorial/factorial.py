#take user input
user_input = int(input("enter a number to factorial: "))

#define function to calculate factorial
def factorial(number):
    result = 1
    while number >= 1:
        result *= number
        number -= 1
    return result

#print result
print(factorial(user_input))
