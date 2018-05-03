#take user input
user_input = int(input("Enter the number to check prime: "))

#function to check if the number is prime, wikipedia method
def primeCheck(number):
    index = 5
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    while index * index <= number:
        if number % index == 0 or number % (index + 2) == 0:
            return False
        index = index + 6
    return True

#print the answer
print("wikipedia method?")
print(primeCheck(user_input))

#alternative method for checking make sure they match!
def easierPrimeCheck(number):
    result = True
    if number == 2:
        return result
    if number > 1:
        for index in range(2,number):
            if(number % index) == 0:
                result = False
                break
            else:
                result = True
    else:
        result = False

    return result
print("easier method?")
print(easierPrimeCheck(user_input))
