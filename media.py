import webbrowser


class Movie():

    """The class who define the characteristics of a movie"""

    """List of the ratings"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, ratings, duration):
        """The method which inits the object movie with a title, a story line,
           a poster image and a trailer link of the movie.
        Args:
             movie_title: It contains the title of the movie.
             movie_storyline: It contains a brief description of the movie.
             poster_image: It contains the link of the poster of the movie.
             trailer_youtube: It contains the link of the trailer of the movie.
             rating: It contains the rating of the movie
             duration: It contains the duration of the movie.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.ratings = ratings
        self.duration = duration

    def show_trailer(self):
        """ This method load the specific trailer"""
        webbrowser.open(self.trailer_youtube_url)
