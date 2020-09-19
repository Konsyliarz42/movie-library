from enum import Enum

#================================================================
class Genre(Enum):
    undefined = 0
    Action = 1
    Adventure = 2
    Comedy = 3
    Crime = 4
    Drama = 5
    Fantasy = 6
    Historical = 7
    Horror = 8
    Magical_realism = 9
    Mystery = 10
    Paranoid_fiction = 11
    Philosophical = 12
    Political = 13
    Romance = 14
    Saga = 15
    Satire = 16
    Science_fiction = 17
    Speculative = 18
    Thriller = 19
    Urban = 20
    Western = 21
    Animation = 22

#================================================================
class Movie:
    def __init__(self, title, year, genre):
        self.title  = title
        self.year   = int(year)
        self.genre  = genre
        self.views  = 0

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        value = value.strip()
        value = value.capitalize()
        value = value.replace(' ', '_')
        self._genre = Genre(0).name

        for gen in Genre:
            if gen.name == value:
                self._genre = gen.name

    def __repr__(self):
        return f"{self.title} ({self.year})"

    #--------------------------------
    def play(self):
        self.views += 1

#================================================================
def printed_number(number):
    if number < 10:
        number = str(number).zfill(2)
    else:
        number = str(number)

    return number

#================================================================
class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.episode    = int(episode)
        self.season     = int(season)


    def __repr__(self):
        episode = printed_number(self.episode)
        season  = printed_number(self.season)

        return f"{self.title} S{season}E{episode}"

    #--------------------------------
    def how_many_episodes(self, library):
        seasons = list()
        episodes = list()

        for obj in library:
            if obj.title == self.title:
                y = int(obj.season)

                if y not in seasons:
                    seasons.append(y)
                    episodes.append(1)

                else:
                    x = seasons.index(y)
                    episodes[x] += 1

        return seasons, episodes
