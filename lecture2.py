movies = {
    'Horror': ['Dracula', 'Texas Chainsaw Massacre'],
    'Comedy': ['Step Brothers' 'Superbad'],
    'Action': ['John Wick'],
    'Sci-Fi': ['Back to the Future', 'Star Wars'],
}

def add_genre_and_list(genre, list):
    movies[genre] = list
    return movies

print(add_genre_and_list('Western', ['The Searchers', 'The Magnificent 7']))

def add_to_list(genre, movie):
    movies[genre].append(movie)
    return movies

print(add_to_list('Action', 'Batman'))
print(add_to_list('Horror', 'Scary Movie'))