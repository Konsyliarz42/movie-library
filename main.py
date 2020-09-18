from random import randint, randrange
from classes import Movie, Series

#--------------------------------
def get_movies(library):
    library = [movie for movie in library if isinstance(movie, Series) == False]
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
    top_list = ['']*3

    if content_type == 'movies':
        library = get_movies(library)

    elif content_type == 'series':
        library = get_series(library)
    
    elif content_type != None:
        print("'content_type' is incorrect!")
        return top_list

    top = sorted(library, key=lambda x: x.views, reverse=True)

    if len(top) < 3:
        x = len(top)
    else:
        x = 3

    for i in range(x):
        top_list[i] = top[i] 
    
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
    library = list()
    
#    library.append(Movie("x", '1999', 'thriller'))
#    library.append(Movie("A", '2000', 'thriller'))
#    library.append(Series(title='y', year=2004, genre='comedy', season=1, episode=2))

#    print(get_movies(library))
#    print(get_series(library))
#    print(search('x', library))

#    generate_views(library, 10)
#    library[0].play()
#    for x in library:
#        print(x.title, x.views)

#    print(top_titles(library))


    for episode in add_season('B', '2000', 'comedy', '1', 20):
        library.append(episode)

#    for episode in add_season('B', '2000', 'comedy', '2', 20):
#        library.append(episode)

    print(library[0].how_many_episodes(library))