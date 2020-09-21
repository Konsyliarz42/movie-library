from random import randint, randrange
from classes import Movie, Series, Genre
from faker import Faker
import datetime

#--------------------------------
def get_movies(library):
    library = [movie for movie in library if not isinstance(movie, Series)]
    library.sort(key=lambda x: x.title)
    return library

#--------------------------------
def get_series(library):
    library = [series for series in library if isinstance(series, Series)]
    library.sort(key=lambda x: x.title)
    return library

#--------------------------------
def search(title, library):
    for x in library:
        if x.title == title:
            return x

    return False

#--------------------------------
def generate_views(library, quantity=1):
    for _ in range(quantity):
        library[randrange(len(library))].views += randint(1, 100)

#--------------------------------
def top_titles(library, *, content_type=None):
    top_list = list()

    if content_type == 'movies':
        library = get_movies(library)

    elif content_type == 'series':
        library = get_series(library)
    
    elif content_type != None:
        print("'content_type' is incorrect!")
        return False

    top     = sorted(library, key=lambda x: x.views, reverse=True)
    titles  = list()
    views   = list()

    for obj in top:
        if obj.__class__ == Series:
            top[top.index(obj)] = ' '

        if obj.title in titles:
            views[titles.index(obj.title)] += obj.views
        else:
            titles.append(obj.title)
            views.append(obj.views)
                
    top = sorted(zip(views, titles), reverse=True)

    if len(top) < 3:
        x = len(top)
    else:
        x = 3

    for i in range(x):
        top_list.append(top[i]) 
    
    return top_list

#--------------------------------
def add_season(title, year, genre, season, episodes_in_season):
    season_list         = list()
    episodes_in_season  = int(episodes_in_season)

    for i in range(1, episodes_in_season + 1):
        season_list.append( Series(title=title, year=year, genre=genre, season=season, episode=i)   )

    return season_list

#================================================================
if __name__ == "__main__":
    print("Biblioteka filmów\n")
    library     = list()
    elements    = 3

    for _ in range(elements):
        title   = Faker('pl_PL').catch_phrase()
        year    = randint(1970, 2020)
        genre   = Genre(randrange(23))

        # Movie
        if randint(0, 1) == 0:
            obj = Movie(title=title, year=year, genre=genre)
            library.append(obj)
        # Series
        else:
            for season in range(randrange(10)):
                slist = add_season(title=title, year=year, genre=genre, season=season, episodes_in_season=randrange(20))
                library.extend(slist)

    generate_views(library, elements)
    ttiles  = top_titles(library, content_type=None)
    date    = datetime.datetime.now().strftime('%x').replace('/', '.')

#    library = get_movies(library)
#    for obj in library:
#        print(obj.title, obj.views)

    if ttiles:
        print("Najpopularniejsze filmy i seriale z dnia:", date)
        for title in ttiles:
            print(str(ttiles.index(title) + 1) + '.', title[1], '(Wyświetleń:', str(title[0]) + ')')
