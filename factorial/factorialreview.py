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
print("original method")
print(factorial(user_input))

#method that we covered in class review
def factorialReview(number):
    result = 1
    for num in range(number,0,-1):
        result *= num
    return result

#print result
print("method from the review")
print(factorialReview(user_input))

#someone asked for iterating up rather than down...what a mess range(1,number+1)
def factorialReviewForward(number):
    result = 1
    for num in range(1,number+1):
        result *= num
    return result

#print result
print("counting forward also from review")
print(factorialReviewForward(user_input))
