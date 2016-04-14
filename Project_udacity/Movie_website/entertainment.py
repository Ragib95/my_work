import movie

Avatar = movie.Movie('Avatar',
	                'A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.',
	                'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
	                'https://youtu.be/5PSNL1qE6VY')

#Avatar.play_trailer()

X_Men_Apocalypse = movie.Movie('X-Men: Apocalypse',
	                            "With the emergence of the world's first mutant, Apocalypse, the X-Men must unite to defeat his extinction level plan.",
	                            'http://screenrant.com/wp-content/uploads/x-men-apocalypse-poster.jpg',
	                            'https://youtu.be/COvnHv42T-A')

X_Men_Apocalypse.play_trailer()

print X_Men_Apocalypse.title
print X_Men_Apocalypse.storyline