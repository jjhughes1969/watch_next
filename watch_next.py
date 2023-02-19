
# Importing spaCy and appropriate language model.

import spacy
nlp = spacy.load('en_core_web_md')

# Read in movies.txt.

with open("Task_2/movies.txt", "r") as movie_library:
    movie_library = movie_library.readlines()

# Define function to compare the last_watched_move with movies.txt and select the one with the highest level of similarity.

def recommendation(last_watched_movie, library):
    value = 0
    movie = ""
    for token in library:
        token = nlp(token)
        last_watched_movie = nlp(last_watched_movie)
        if token.similarity(last_watched_movie) > value:
            value = token.similarity(last_watched_movie)
            movie = token.text
    print(f"\nBased on your last watched movie, we recommend the next movie you watch is:\n\n{movie}\n")

# Define planet_hulk.

planet_hulk = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Run the recommendation function with planet_hulk as the last_watched_movie and output recommendation.

recommendation(planet_hulk, movie_library)

# I'm not sure this is the recommendation that I would make!
# The similarity seems to be driven by words like 'darkness' and 'nightmare' - stripping these out of the input, returns a different result.
# Ideally, I'd like it to recommend Movie B, about another superhero, Superman, but not sure how to get it to overindex particular words or concepts.
