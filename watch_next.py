# Let's build a system that will tell you what to watch next based on the word 
#vector similarity of the description of movies

#we are going to make use of spaCy library with the Medium Language Module Scorer for this program
import spacy
nlp = spacy.load('en_core_web_md')

"""
Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the following description 
"""

planet_hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk lands on the
planet Sakaar where he is sold into slavery and trained as a gladiator.
"""

def find_similar_movie(planet_hulk_description):
    """
    Find the title of the most similar movie based on the given description.
    
    Parameters:
    - planet_hulk_description (str): The description of the movie "Planet Hulk".
    
    Returns:
    - string value: The title of the most similar movie.
    """

    # we first read our movie file
    with open("movies.txt", "r") as file:
        movie_lines = file.readlines()

    # we then store the movie descriptions in our list called movies without the titles (not that it will make any difference)
    movies = []
    for line in movie_lines:
        description = line.split(":")[1] #we get the second element from our list (the description :)
        movies.append(description)

    # before we go ahead, let's tokenize our watched movie description
    planet_hulk_tokens = nlp(planet_hulk_description)

    # let's calculate the similarity for each description from our list
    similarities = []
    for movie in movies:
        movie_tokens = nlp(movie) #here we tokenize the text from our movies file
        similarity = planet_hulk_tokens.similarity(movie_tokens) #here we calculate the similiarity between the tokens of the watched description and movies text file
        similarities.append(similarity)

    # we use the built-in function 'max' to get the highest matching similarity score movie
    max_similarity_index = similarities.index(max(similarities))

    # now let's find out the title for the next movie
    most_similar_movie = movie_lines[max_similarity_index].split(":")[0].strip()
    
    return most_similar_movie

#let's see what movie our program recommends
next_movie = find_similar_movie(planet_hulk_description)
print(f"Next movie we recommend to watch is: {next_movie}")