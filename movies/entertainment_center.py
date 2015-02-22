import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                                        "A story of a boy and his toys that come to life.",
                                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                                     "A Marine on an alien planet.",
                                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
                     

apocalypseNow = media.Movie("Apocalypse Now",
                                     "A soldier goes deep into the heart of darkness.",
                                     "http://upload.wikimedia.org/wikipedia/en/c/c2/Apocalypse_Now_poster.jpg",
                                     "https://www.youtube.com/watch?v=IkrhkUeDCdQ")
                     
school_of_rock = media.Movie("School of Rock",
                                     "Like Schoolhouse Rock, but not.",
                                    "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
                                     "There's this rat who cooks",
                                    "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                                     "https://www.youtube.com/watch?v=c3sBBRxDAqk")

hunger_games = media.Movie("Hunger Games",
                                     "There's these kids who kill each other. Or something.",
                                    "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                                     "https://www.youtube.com/watch?v=PbA63a7H0bo")

movies = [toy_story, avatar, apocalypseNow, school_of_rock, ratatouille, hunger_games]

#print(media.Movie.VALID_RATINGS[2])

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
