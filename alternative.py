"""Create a program that reads in a string and makes
each alternate character an UPPERCASE character and each other
alternate character a lowercase character"""
# e.g, the string “Hello World would become “HeLlO WoRlD”

# create an empty string and list to store the new sentence
new_sentence = "" 
second_new_sentence = []

# use while loop that runs as many times as it needs to get the right output
while True:
    sentence = input('Please write the sentence you would like to transform: \n')

    if sentence.replace(" ", "").isalpha(): # check if the characters are only alphabets(to don't get an error replace empty spaces with "")
        break 
    else:
        print('Please try again, using only letters/words.')

# create a for loop that iterates through the numbers of characters       
for i in range(len(sentence)):
    if i % 2 == 0: #we transform all the index character with even number in uppercase
        new_sentence += sentence[i].upper()
    else: #odd numbers
        new_sentence += sentence[i].lower()
        
print(" ")        
print(f"You're first new transformed sentence is: \n{new_sentence}\n")  

"""Now, try starting with the same string but making each alternative word
lower and upper case."""
# e.g. the string: “I am learning to code” would become “i AM learning TO code”

word = sentence.split() # create a list with all the words

for i in range(len(word)): # iterate through the list(nr of words we got)
    if i % 2 == 1: # the list with odd index will become uppercase
        second_new_sentence.append(word[i].upper())

    else: # even index words becomes lowercase
        second_new_sentence.append(word[i].lower())

print("You're second new transformed sentence is:")
print(" ".join(second_new_sentence)) # the elements are joined together in the list
    