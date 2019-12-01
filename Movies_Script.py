import pandas as pd
import random

#importing CSV file with all the movies I own
#columns in the file include "Title", "Watchabilitty", and "Genre"
my_movies = pd.read_csv('Movies_we_own.csv')

#Column of the all the movie titles
Title_Movie = movies.Title

#Python list of all the movies titles
Title_Movie_List = []
Title_Movie_List = list(movies['Title'])

#Column of the all the movie Watachability
Watchability = movies.Watchabilitty

#Python list of all the movies watchability
Watchability_List = []
Watchability_List = list(movies['Title'])

#Column of all the movies genres
Genre = movies.Genre

#Python list of all the movies genres
Genre_List = []
Genre_List = list(movies['Genre'])

def random_movie (movies):
    #picks a random movie from CSV file Movies_we_own
    return random.choice(Title_Movie)
    print(random_movie)

def add_movie (movies):
    #add newly purchased movies - Title, Watchability and Genre
    df = (Title_Movie, Watchability, Genre)
    df.append('Spider Man Homecoming', 'Medium', 'Super Hero')
    print(movies)

def add_movie(new_movie):
    #sort file after adding new movie
    for new_movie in add_movie:
        movies.sort()

def choose_by_genre (movies):
    #Random movie by genre
    return random.choice(movies)
    if Genre_List == Animated:
        print(choose_by_genre)

def movie (movie):
    #print or append movies file using codes below
    if input == 1:
      return random_movie()
    elif input == 2:
       return add_movie()
    elif input == 3:
       return choose_by_genre()

#Printing a random movie
print(random_movie(1))