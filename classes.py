#================================================================
class Movie:
    def __init__(self, title, year, genre, views):
        self.title  = title
        self.year   = year
        self.genre  = genre
        self.views  = int(views)


    def __repr__(self):
        return f"{self.title} ({self.year})"

    #--------------------------------
    def play(self):
        self.views += 1

#================================================================
class Series(Movie):
    def __init__(self, episode, season, *args):
        super().__init__(*args)

        self.episode    = str(episode)
        self.season     = season


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
        quantity = 0

        for x in library:
            if x.title == self.title:
                if x.season == self.season:
                    quantity += 1

        return quantity

