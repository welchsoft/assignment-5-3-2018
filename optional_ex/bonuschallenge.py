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

#split input string into array of words
user_words = user_input.split()

#create empty dictionary
word_bank = {}

#populate the dictionary
for words in user_words:
    word_bank.update({words:0})

#check populated dictionary against user input and increment if found
for words in user_words:
    keys=word_bank.keys()
    if words in keys:
        word_bank[words]+=1
    else:
        word_bank[words]=1

#print result
print(word_bank)


#work in progress I need to figure out how to selelect from each
