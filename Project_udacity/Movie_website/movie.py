import webbrowser

class Movie(object):
	"""docstring for Movie"""
	def __init__(self, title,  storyline, poster_image_url, trailer_youtube_url):
		self.title = title
		self.storyline = storyline
		self.poster_image = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def play_trailer(self):
		play_trailer = webbrowser.open(self.trailer_youtube_url)		