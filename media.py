import webbrowser

class Movie():

	""" The class who define the characteristics of a movie"""
	
	VALID_RATINGS = ["G", "PG", "PG-130", "R"]

	""" The method which inits the object movie with a title, a story line, a poster image and a trailer link of the movie. """
	def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	""" This method load the specific trailer"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
