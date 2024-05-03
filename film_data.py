from Film import Film


def add_films_to_catalog(catalog):
    films_data = [
        {
            "title": "Inception",
            "release_date": "2010",
            "director": "Christopher Nolan",
            "genre": "Science Fiction",
            "duration_min": 148
        },
        {
            "title": "The Godfather",
            "release_date": "1972",
            "director": "Francis Ford Coppola",
            "genre": "Crime",
            "duration_min": 175
        },
        {
            "title": "Pulp Fiction",
            "release_date": "1994",
            "director": "Quentin Tarantino",
            "genre": "Crime",
            "duration_min": 154
        },
        {
            "title": "The Shawshank Redemption",
            "release_date": "1994",
            "director": "Frank Darabont",
            "genre": "Drama",
            "duration_min": 142
        },
        {
            "title": "Forrest Gump",
            "release_date": "1994",
            "director": "Robert Zemeckis",
            "genre": "Drama",
            "duration_min": 142
        },
        {
            "title": "The Matrix",
            "release_date": "1999",
            "director": "The Wachowskis",
            "genre": "Science Fiction",
            "duration_min": 136
        },
        {
            "title": "Interstellar",
            "release_date": "2014",
            "director": "Christopher Nolan",
            "genre": "Science Fiction",
            "duration_min": 169
        },
        {
            "title": "Gladiator",
            "release_date": "2000",
            "director": "Ridley Scott",
            "genre": "Action",
            "duration_min": 155
        },
        {
            "title": "The Dark Knight",
            "release_date": "2008",
            "director": "Christopher Nolan",
            "genre": "Action",
            "duration_min": 152
        },
        {
            "title": "The Silence of the Lambs",
            "release_date": "1991",
            "director": "Jonathan Demme",
            "genre": "Thriller",
            "duration_min": 118
        },
        {
            "title": "Inglourious Basterds",
            "release_date": "2009",
            "director": "Quentin Tarantino",
            "genre": "War",
            "duration_min": 153
        },
        {
            "title": "The Departed",
            "release_date": "2006",
            "director": "Martin Scorsese",
            "genre": "Crime",
            "duration_min": 151
        },
        {
            "title": "Saving Private Ryan",
            "release_date": "1998",
            "director": "Steven Spielberg",
            "genre": "War",
            "duration_min": 169
        },
        {
            "title": "Fight Club",
            "release_date": "1999",
            "director": "David Fincher",
            "genre": "Drama",
            "duration_min": 139
        },
        {
            "title": "Schindler's List",
            "release_date": "1993",
            "director": "Steven Spielberg",
            "genre": "Biography",
            "duration_min": 195
        },
        {
            "title": "The Prestige",
            "release_date": "2006",
            "director": "Christopher Nolan",
            "genre": "Drama",
            "duration_min": 130
        },
        {
            "title": "The Green Mile",
            "release_date": "1999",
            "director": "Frank Darabont",
            "genre": "Drama",
            "duration_min": 189
        },
        {
            "title": "The Usual Suspects",
            "release_date": "1995",
            "director": "Bryan Singer",
            "genre": "Crime",
            "duration_min": 106
        },
        {
            "title": "The Lion King",
            "release_date": "1994",
            "director": "Roger Allers, Rob Minkoff",
            "genre": "Animation",
            "duration_min": 88
        },
        {
            "title": "Titanic",
            "release_date": "1997",
            "director": "James Cameron",
            "genre": "Romance",
            "duration_min": 195
        },
        {
            "title": "Jurassic Park",
            "release_date": "1993",
            "director": "Steven Spielberg",
            "genre": "Science Fiction",
            "duration_min": 127
        },
        {
            "title": "Avatar",
            "release_date": "2009",
            "director": "James Cameron",
            "genre": "Science Fiction",
            "duration_min": 162
        },
        {
            "title": "The Avengers",
            "release_date": "2012",
            "director": "Joss Whedon",
            "genre": "Action",
            "duration_min": 143
        },
        {
            "title": "Goodfellas",
            "release_date": "1990",
            "director": "Martin Scorsese",
            "genre": "Crime",
            "duration_min": 146
        },
        {
            "title": "The Sixth Sense",
            "release_date": "1999",
            "director": "M. Night Shyamalan",
            "genre": "Thriller",
            "duration_min": 107
        },
        {
            "title": "Eternal Sunshine of the Spotless Mind",
            "release_date": "2004",
            "director": "Michel Gondry",
            "genre": "Romance",
            "duration_min": 108
        },
        {
            "title": "The Social Network",
            "release_date": "2010",
            "director": "David Fincher",
            "genre": "Biography",
            "duration_min": 120
        },
        {
            "title": "Amélie",
            "release_date": "2001",
            "director": "Jean-Pierre Jeunet",
            "genre": "Romance",
            "duration_min": 122
        },
        {
            "title": "Shutter Island",
            "release_date": "2010",
            "director": "Martin Scorsese",
            "genre": "Mystery",
            "duration_min": 138
        },
        {
            "title": "Casino Royale",
            "release_date": "2006",
            "director": "Martin Campbell",
            "genre": "Action",
            "duration_min": 144
        },
        {
            "title": "City of God",
            "release_date": "2002",
            "director": "Fernando Meirelles, Kátia Lund",
            "genre": "Crime",
            "duration_min": 130
        },
        {
            "title": "No Country for Old Men",
            "release_date": "2007",
            "director": "Joel Coen, Ethan Coen",
            "genre": "Crime",
            "duration_min": 122
        },
        {
            "title": "Requiem for a Dream",
            "release_date": "2000",
            "director": "Darren Aronofsky",
            "genre": "Drama",
            "duration_min": 102
        },
        {
            "title": "Memento",
            "release_date": "2000",
            "director": "Christopher Nolan",
            "genre": "Mystery",
            "duration_min": 113

        },
    ]

    for film_data in films_data:
        title = film_data["title"]
        release_date = film_data["release_date"]
        director = film_data["director"]
        genre = film_data["genre"]
        duration = film_data["duration_min"]
        film = Film(title, release_date, director, genre, duration)
        catalog.add_film(film)
