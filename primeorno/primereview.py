#take user input
number = int(input("Enter number: "))


def isPrime(number):
    is_prime = True
    if number == 1:
        return False
    else:
        for num in range(number-1,1,-1):
            if number % num == 0:
                is_prime = False
                break

        return is_prime

print(isPrime(number))
