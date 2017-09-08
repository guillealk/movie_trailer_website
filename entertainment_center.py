import media
import fresh_tomatoes

""" This class contains the list of the movies. There are the series of movies of Harry Potter and Pirates of Caribbean"""

harry_potter_stone = media.Movie("Harry Potter and the Philosopher's Stone",
								"Rescued from the outrageous neglect of his aunt and uncle, a young boy with a great destiny proves his worth while attending Hogwarts School of Witchcraft and Wizardry.",
								"https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Philosopher%27s_Stone_posters.JPG",
								"https://www.youtube.com/watch?v=eKSB0gXl9dw", 
								media.Movie.VALID_RATINGS[1],
								"2h 32min")

harry_potter_chamber = media.Movie("Harry Potter and the Chamber of Secrets",
								"Harry ignores warnings not to return to Hogwarts, only to find the school plagued by a series of mysterious attacks and a strange voice haunting him.",
					 			"https://upload.wikimedia.org/wikipedia/en/c/c0/Harry_Potter_and_the_Chamber_of_Secrets_movie.jpg",
					 			"https://www.youtube.com/watch?v=1bq0qff4iF8", 
					 			media.Movie.VALID_RATINGS[1],
					 			"2h 41min")


harry_potter_azkaban = media.Movie ("Harry Potter and the Prisoner of Azkaban",
									"It's Harry's third year at Hogwarts; not only does he have a new \"Defense Against the Dark Arts\" teacher, but there is also trouble brewing. Convicted murderer Sirius Black has escaped the Wizards' Prison and is coming after Harry.",
									"https://upload.wikimedia.org/wikipedia/en/b/bc/Prisoner_of_azkaban_UK_poster.jpg",
									"https://www.youtube.com/watch?v=lAxgztbYDbs", 
									media.Movie.VALID_RATINGS[1],
									"2h 22min")

harry_potter_goblet = media.Movie ("Harry Potter and the Goblet of Fire",
								"A young wizard finds himself competing in a hazardous tournament between rival schools of magic, but he is distracted by recurring nightmares.",
								"https://upload.wikimedia.org/wikipedia/en/c/c9/Harry_Potter_and_the_Goblet_of_Fire_Poster.jpg",
								"https://www.youtube.com/watch?v=3EGojp4Hh6I", 
								media.Movie.VALID_RATINGS[2],
								"2h 37min")

harry_potter_phoenix = media.Movie ("Harry Potter and the Order of the Phoenix",
									"With their warning about Lord Voldemort's return scoffed at, Harry and Dumbledore are targeted by the Wizard authorities as an authoritarian bureaucrat slowly seizes power at Hogwarts.",
									"https://upload.wikimedia.org/wikipedia/en/e/e7/Harry_Potter_and_the_Order_of_the_Phoenix_poster.jpg",
									"https://www.youtube.com/watch?v=y6ZW7KXaXYk", 
									media.Movie.VALID_RATINGS[2],
									"2h 18min")

harry_potter_half_blood = media.Movie ("Harry Potter and the Half-Blood Prince",
									"As Harry Potter begins his sixth year at Hogwarts, he discovers an old book marked as \"the property of the Half-Blood Prince\" and begins to learn more about Lord Voldemort's dark past.",
									"https://upload.wikimedia.org/wikipedia/en/3/3f/Harry_Potter_and_the_Half-Blood_Prince_poster.jpg",
									"https://www.youtube.com/watch?v=jpCPvHJ6p90", 
									media.Movie.VALID_RATINGS[1],
									"2h 33min")

harry_potter_hallows1 = media.Movie ("Harry Potter and the Deathly Hallows - Part 1",
									"As Harry races against time and evil to destroy the Horcruxes, he uncovers the existence of three most powerful objects in the wizarding world: the Deathly Hallows.",
									"https://upload.wikimedia.org/wikipedia/en/2/2d/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_1.jpg",
									"https://www.youtube.com/watch?v=MxqsmsA8y5k", 
									media.Movie.VALID_RATINGS[2],
									"2h 26min")

harry_potter_hallows2 = media.Movie ("Harry Potter and the Deathly Hallows - Part 2",
									"Harry, Ron, and Hermione search for Voldemort's remaining Horcruxes in their effort to destroy the Dark Lord as the final battle rages on at Hogwarts.",
									"https://upload.wikimedia.org/wikipedia/en/d/df/Harry_Potter_and_the_Deathly_Hallows_%E2%80%93_Part_2.jpg",
									"https://www.youtube.com/watch?v=mObK5XD8udk", 
									media.Movie.VALID_RATINGS[2],
									"2h 10min")

pirates_caribbean_black_pearl = media.Movie ("Pirates of the Caribbean: The Curse of the Black Pearl",
											"Blacksmith Will Turner teams up with eccentric pirate \"Captain\" Jack Sparrow to save his love, the governor's daughter, from Jack's former pirate allies, who are now undead.",
											"https://upload.wikimedia.org/wikipedia/en/8/89/Pirates_of_the_Caribbean_-_The_Curse_of_the_Black_Pearl.png",
											"https://www.youtube.com/watch?v=naQr0uTrH_s", 
											media.Movie.VALID_RATINGS[2],
											"2h 23min")

pirates_caribbean_dead_man = media.Movie ("Pirates of the Caribbean: Dead Man's Chest",
										"Jack Sparrow races to recover the heart of Davy Jones to avoid enslaving his soul to Jones' service, as other friends and foes seek the heart for their own agenda as well.",
										"https://upload.wikimedia.org/wikipedia/en/2/2d/Pirates_of_the_caribbean_2_poster_b.jpg",
										"https://www.youtube.com/watch?v=ozk0-RHXtFw",
										media.Movie.VALID_RATINGS[2],
										"2h 31min")

pirates_caribbean_world_end = media.Movie ("Pirates of the Caribbean: At World's End",
											"Captain Barbossa, Will Turner and Elizabeth Swann must sail off the edge of the map,navigate treachery and betrayal, find Jack Sparrow, and make their final alliances for one last decisive battle.",
											"https://upload.wikimedia.org/wikipedia/en/5/5a/Pirates_AWE_Poster.jpg",
											"https://www.youtube.com/watch?v=HKSZtp_OGHY",
											media.Movie.VALID_RATINGS[2],
											"2h 49min")

pirates_caribbean_stranger_tides = media.Movie ("Pirates of the Caribbean: On Stranger Tides",
											"Jack Sparrow and Barbossa embark on a quest to find the elusive fountain of youth, only to discover that Blackbeard and his daughter are after it too.",
											"https://upload.wikimedia.org/wikipedia/en/c/c6/On_Stranger_Tides_Poster.jpg",
											"https://www.youtube.com/watch?v=KR_9A-cUEJc",
											media.Movie.VALID_RATINGS[2],
											"2h 16min")

pirates_caribbean_no_tales = media.Movie ("Pirates of the Caribbean: Dead Men Tell No Tales",
											"Captain Jack Sparrow searches for the trident of Poseidon while being pursued by an undead sea captain and his crew.",
											"https://upload.wikimedia.org/wikipedia/en/2/21/Pirates_of_the_Caribbean%2C_Dead_Men_Tell_No_Tales.jpg",
											"https://www.youtube.com/watch?v=6i77T6KzYxM",
											media.Movie.VALID_RATINGS[2],
											"2h 9min")

""" The list of the movie objects"""
movies = [harry_potter_stone, harry_potter_chamber, harry_potter_azkaban,harry_potter_goblet, harry_potter_phoenix, harry_potter_half_blood, harry_potter_hallows1, harry_potter_hallows2,
		  pirates_caribbean_black_pearl, pirates_caribbean_dead_man,pirates_caribbean_world_end, pirates_caribbean_stranger_tides, pirates_caribbean_no_tales]

""" Method that creates the webpage using the Fresh tomatoes library"""
fresh_tomatoes.open_movies_page(movies)
