# -------------- First Task ------------

"""
Create a file called semantic.py and run all the code extracts above.
"""

import spacy

#first block of code
nlp = spacy.load('en_core_web_md')

print('-----Medium Language Model Scores(en_core_web_md)-----')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(' ')

#second code block
tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print(' ')

#third block code
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare) #tokenize the sentence that we use to compare

for sentence in sentences:
    # tokenize and calculate the similarity between the current sentence and the model sentence
    similarity = nlp(sentence).similarity(model_sentence)
    
    # print the sentence along with its similarity score
    print(sentence + " - ", similarity)


# -------------- Second Task ------------

"""
Write a note about what you found interesting about the similarities
between cat, monkey and banana and think of an example of your own.
"""

# Similarity1: 
"""
the score similarity between 'cat' and 'monkey' is 0.59, not the best score but still decent,
thinking that those are 2 different mammals, possibly we got this score because they share some characteristics such as having tails, fur or they're both agile 
"""

# Similarity2:
"""
the score similarity between 'banana' and 'monkey' is 0.4, interestingly enough is that this is still a big score because we compare 
fruit with an animal, but spacy probably assimilates the fact that when people think about monkeys, they also think that most of them eat bananas.
"""

# Similarity3:
"""
out of all of them, the lowest score we got is between 'cat' and 'banana', a total of 0.22, no surprise, of course, because neither me nor
you (I hope) haven't seen a cat eating a banana; maybe we got a score of 0.22 and not smaller because you can dress a cat like a banana for a costume party
"""

# the words example I'm choosing is car, horse, bicycle and wheelchair
# let's run it and see the similarities using the Medium Size Model
print(' ')
print('----- My Example -----')
tokens = nlp('car horse bicycle wheelchair')

for token1 in tokens:
    for token2 in tokens:
        similarity = token1.similarity(token2)
        print(f"Token1: {token1.text}\tToken2: {token2.text}\tSimilarity: {similarity}")


# -------------- Third Task ------------

"""
Run the example file with the simpler language model ‘en_core_web_sm’ and
write a note on what you notice is different from the model 'en_core_web_md'.
"""

# let's run the code with the simpler language model

print(' ')
print('-----Small Language Model Scores(en_core_web_sm)-----')

#first block of code
nlp = spacy.load('en_core_web_sm')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print(' ')

#second code block
tokens = nlp('cat apple monkey banana ')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print(' ')

#third block code
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare) #tokenize the sentence that we use to compare

for sentence in sentences:
    # tokenize and calculate the similarity between the current sentence and the model sentence
    similarity = nlp(sentence).similarity(model_sentence)
    
    # print the sentence along with its similarity score
    print(sentence + " - ", similarity)

"""
the first thing that we notice is the 'UserWarning [W007]' we get when using the en_core_web_sm, which lets us know 
that we should change our model as our results might not be very accurate or not 'give useful similarity judgements', and indeed,
our similarity scores are not really good using this model; based on a score from 0 to 1, where 1 is the best, we get, for example
a similarity score of 0.7 for the word 'cat' and 'apple', but surprisingly enough, the similarity score is almost similar for 'cat' and 'banana'
scoring 0.22 on both models.
"""