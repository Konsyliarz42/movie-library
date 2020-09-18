#================================================================
class Movie:
    def __init__(self, title, year, genre):
        self.title  = title
        self.year   = int(year)
        self.genre  = genre
        self.views  = 0


    def __repr__(self):
        return f"{self.title} ({self.year})"

    #--------------------------------
    def play(self):
        self.views += 1

#================================================================
class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.episode    = str(episode)
        self.season     = str(season)


    @property
    def episode(self):
        return self._episode

    @episode.setter
    def episode(self, value):
        if len(value) < 2:
            self._episode = '0' + str(value)
        else:
            self._episode = str(value)

    @property
    def season(self):
        return self._season

    @season.setter
    def season(self, value):
        if len(value) < 2:
            self._season = '0' + str(value)
        else:
            self._season = str(value)
    

    def __repr__(self):
        return f"{self.title} S{self.season}E{self.episode}"

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
