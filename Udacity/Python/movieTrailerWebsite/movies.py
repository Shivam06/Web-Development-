import media
import fresh_tomatoes
toy_story = media.Movie("3:00 hrs",
                        "Toy Story",
                        "Story of a boy and his toys who comes to life",
                        "http://vignette4.wikia.nocookie.net/disney/images/4/4c/Toy-story-movie-posters-4.jpg/revision/latest?cb=20140816182710",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("2:50 hrs",
                     "Avatar",
                     "Story of aliens living in different planet",
                     "https://www.movieposter.com/posters/archive/main/98/MPW-49246",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#friends = media.TvShow("Friends", "30 mins", 1, 21, "HBO")
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)

