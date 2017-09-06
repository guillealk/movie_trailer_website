import media
import fresh_tomatoes

""" This class contains the list of the movies. There are the series of movies of Harry Potter and Pirates of Caribbean"""

harry_potter_stone = media.Movie("Harry Potter and the Philosopher's Stone",
						"A story of a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
						"https://www.youtube.com/watch?v=eKSB0gXl9dw")

harry_potter_chamber = media.Movie("Harry Potter and the Chamber of Secrets",
					 "A second year of wizard",
					 "https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
					 "https://www.youtube.com/watch?v=1bq0qff4iF8")


harry_potter_azkaban = media.Movie ("Harry Potter and the Prisoner of Azkaban",
							"Harry Potter and the Prisoner of Azkaban",
							"https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
							"https://www.youtube.com/watch?v=lAxgztbYDbs")

harry_potter_goblet = media.Movie ("Harry Potter and the Goblet of Fire",
							"Harry Potter and the Goblet of Fire",
							"https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
							"https://www.youtube.com/watch?v=3EGojp4Hh6I")

harry_potter_phoenix = media.Movie ("Harry Potter and the Order of the Phoenix",
							"Harry Potter and the Order of the Phoenix",
							"https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg",
							"https://www.youtube.com/watch?v=y6ZW7KXaXYk")


harry_potter_half_blood = media.Movie ("Harry Potter and the Half-Blood Prince",
							"Harry Potter and the Half-Blood Prince",
							"https://upload.wikimedia.org/wikipedia/en/3/3f/Harry_Potter_and_the_Half-Blood_Prince_poster.jpg",
							"https://www.youtube.com/watch?v=jpCPvHJ6p90")

harry_potter_hallows1 = media.Movie ("Harry Potter and the Deathly Hallows - Part 1",
							"Harry Potter and the Deathly Hallows - Part 1",
							"https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",
							"https://www.youtube.com/watch?v=MxqsmsA8y5k")

harry_potter_hallows2 = media.Movie ("Harry Potter and the Deathly Hallows - Part 2",
							"Harry Potter and the Deathly Hallows - Part 2",
							"https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
							"https://www.youtube.com/watch?v=mObK5XD8udk")

pirates_caribbean_black_pearl = media.Movie ("Pirates of the Caribbean: The Curse of the Black Pearl",
											"Blacksmith Will Turner teams up with eccentric pirate \"Captain\" "
											"Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
											"https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
											"https://www.youtube.com/watch?v=naQr0uTrH_s")
pirates_caribbean_dead_man = media.Movie ("Pirates of the Caribbean: Dead Man's Chest",
											"Jack Sparrow races to recover the heart of Davy Jones to avoid enslaving his soul to Jones' service,"
											" as other friends and foes seek the heart for their own agenda as well.",
											"https://upload.wikimedia.org/wikipedia/en/2/2d/Pirates_of_the_caribbean_2_poster_b.jpg",
											"https://www.youtube.com/watch?v=ozk0-RHXtFw")

pirates_caribbean_world_end = media.Movie ("Pirates of the Caribbean: At World's End",
											"Captain Barbossa, Will Turner and Elizabeth Swann must sail off the edge of the map,"
											" navigate treachery and betrayal, find Jack Sparrow, and make their final alliances for one last decisive battle.",
											"https://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg",
											"https://www.youtube.com/watch?v=HKSZtp_OGHY")

pirates_caribbean_stranger_tides = media.Movie ("Pirates of the Caribbean: On Stranger Tides",
											"Jack Sparrow and Barbossa embark on a quest to find the elusive fountain of youth,"
											" only to discover that Blackbeard and his daughter are after it too.",
											"https://upload.wikimedia.org/wikipedia/en/c/c6/On_Stranger_Tides_Poster.jpg",
											"https://www.youtube.com/watch?v=KR_9A-cUEJc")

pirates_caribbean_no_tales = media.Movie ("Pirates of the Caribbean: Dead Men Tell No Tales",
											"Captain Jack Sparrow searches for the trident of Poseidon while being pursued by an"
											" undead sea captain and his crew.",
											"https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
											"https://www.youtube.com/watch?v=6i77T6KzYxM")

""" The list of the movie objects"""
movies = [harry_potter_stone, harry_potter_chamber, harry_potter_azkaban,harry_potter_goblet, harry_potter_phoenix, harry_potter_half_blood, harry_potter_hallows1, harry_potter_hallows2,
		  pirates_caribbean_black_pearl, pirates_caribbean_dead_man,pirates_caribbean_world_end, pirates_caribbean_stranger_tides, pirates_caribbean_no_tales]

""" Method that creates the webpage using the Fresh tomatoes library"""
fresh_tomatoes.open_movies_page(movies)
