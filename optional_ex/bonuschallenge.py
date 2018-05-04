#take user input
user_input = input("please enter a word: ")

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

#work in progress I need to figure out how to selelect from each
sorted_words = sorted(word_bank.items(), key=lambda x: x[1])
print("most used words")
print(sorted_words[len(sorted_words):len(sorted_words) - 4:-1])
