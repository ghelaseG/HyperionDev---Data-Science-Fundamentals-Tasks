# in the following program, we are going to explore how the open-source natural language processing (NLP): spaCy works
# for more info use this link: https://spacy.io/usage/linguistic-features#named-entities

import spacy

# -------------- First Task ------------
# store the garden path sentences you have identified in a list called gardenpathSentences

gardenpathSentences = [
            "Hospitals Sued by 7 Foot Doctors.",            
            "They painted the wall with cracks.",
            "Red Tape Holds up New Bridge.",
            "The old dog the footsteps of the young.",
            "Ricky knew the answer to the question was yes, but wouldn't speak the word out loud.",
            "Mary gave the child a Band-Aid.",
            "That Jill is never here hurts.",
            "The cotton clothing is made of grows in Mississippi."
]

# load spacy using simple english model
nlp = spacy.load("en_core_web_sm") 

# we use a for loop to go through each sentence from our list
for sentence in gardenpathSentences: 
    # tokenise each sentence into individual words
    doc = nlp(sentence) 
    # perform named entity recognition for each token
    for token in doc: 
        print(f"Token: {token.text}\tGrammatical Category: {token.pos_}\tEntity Type: {token.ent_type_}")

# -------------- Second Task ------------
# use spacy.explain to look up and print the meaning of entities that you don’t understand.

print(f"Explanation for GPE: {spacy.explain('GPE')}")
print(f"Explanation for FAC: {spacy.explain('FAC')}")
print(f"Explanation for ORG: {spacy.explain('ORG')}")

# -------------- Third Task ------------
"""
write a comment about two entities that you looked up. For each entity answer the following questions:
a. What was the entity and its explanation that you looked up?
b. Did the entity make sense in terms of the word associated with it?
"""

# a.
"""
Entity 1: "GPE" (Geopolitical entity) - An entity representing countries, cities, states.
Entity 2: "ORG" (Organisation) - An entity representing companies, agencies, institutions, etc.
"""

# b.
"""
Talking about 'The cotton clothing is made of grows in Mississippi.'
According to this article: https://englishwithasmile.org/2015/01/31/garden-path-sentences-crazy-sentences-that-do-have-meaning/#:~:text=The%20cotton%20clothing%20is%20made,the%20rest%20will%20work%20out,

the easier to read version will be: ' The cotton that is grown for clothing comes from Mississippi. '

What spacy is recoginising it is as a geo political entity (Mississippi), which is correct.

"""

"""
Talking about 'Red Tape Holds up New Bridge.' 
According to this article: https://www.sjsu.edu/writingcenter/docs/handouts/Garden%20Path%20Sentences.pdf,
'The phrase “red tape” here is supposed to refer to bureaucratic obstacles, but it instead
sounds as if actual tape that it red is supporting a bridge.' 

What spacy is recognising it, an organisation (Red Tape) which is wrong. """
