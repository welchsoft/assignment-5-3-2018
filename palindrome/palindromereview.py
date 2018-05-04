#take user inputs and set up the arrays
word = input("Enter a word to check if it is a palindrome: ")

def isPalindrome(word):

    reversed_word = ""

    for index in range(len(word)-1,-1,-1):
        reversed_word += word[index]

    return word == reversed_word
#compare the two arrays to see if they are equal
if isPalindrome(word.lower()):
    print(f"{word} is a palindrome, wow cool wow!")
else:
    print(f"{word} is not a palindrome, how boring")
