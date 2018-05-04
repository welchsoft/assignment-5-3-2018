#take user inputs and set up the arrays
user_input = input("Enter a word to check if it is a palindrome ")
base_input = []
backward_output = []

#break the string into an array of characters
for char in user_input:
    base_input.append(char)

print(f"input item {base_input}")

#fill second array with the first one but backwards
index = len(base_input)
while index >= 1:
    backward_output.append(base_input[index-1])
    index -=1

print(f"backwards {backward_output}")

#compare the two arrays to see if they are equal
if base_input == backward_output:
    print(f"{user_input} is a palindrome how fancy")
else:
    print(f"{user_input} is not a palindrome how rude")
