import webbrowser

class Video():
    def __init__(self, duration, title):
        self.title = title
        self.duration = duration

class Movie(Video):
    """ This class provides a way to store movie related info. """
    VALID_RATINGS = ["G","PG","PG-13","R"]
    
    def __init__(self, duration, movie_title, movie_story_line, poster_image,trailer_youtube):
        Video.__init__(self,duration, movie_title)
        self.story_line = movie_story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, duration, title, season, episode, tv_station):
        Video.__init__(self,duration, title)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station
