# Compulsory Task 2
# Print the sentence given using replace() and then upper(); in the end the sentence reversed.

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

sentence = sentence.replace("!"," ")
print(sentence)

sentence = sentence.upper()
print(sentence)

sentence = sentence.capitalize()[::-1]
print(sentence)