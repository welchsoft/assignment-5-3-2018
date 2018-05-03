#take user input
user_input = input("please enter a word: ")

#create empty dictionary
alphabet = {}

#populate the dictionary
for key in user_input:
    alphabet.update({key:0})

#check populated dictionary against user input and increment if found
for letter in user_input:
    keys=alphabet.keys()
    if letter in keys:
        alphabet[letter]+=1
    else:
        alphabet[letter]=1

#print result
print(alphabet)
