from Film import Film


class FilmCatalog:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def remove_film(self, title):
        for film in self.films:
            if film.title == title:
                self.films.remove(film)
                print(f"Film '{title}' removed successfully.")
                return
        print(f"Film '{title}' not found.")

    def display_catalog(self):
        print("\n=== Film Catalog ===")
        for film in self.films:
            print(film)

    def search_by_title(self, title):
        for film in self.films:
            if film.title.lower() == title.lower():
                print(film)
                return
        print(f"Film '{title}' not found.")

    def filter_by_genre(self, genre):
        filtered_films = [film for film in self.films if film.genre.lower() == genre.lower()]
        if filtered_films:
            print(f"\n=== Films in the {genre} genre ===")
            for film in filtered_films:
                print(film)
        else:
            print(f"No films found in the {genre} genre.")

    def sort_by_duration(self):
        self.films.sort(key=lambda x: x.duration_min)
        print("\n=== Films Sorted by Duration ===")
        for film in self.films:
            print(film)

    def search_by_director(self, director):
        director = director.lower()
        found = False
        for film in self.films:
            if director in film.director.lower():
                print(film)
                found = True
        if not found:
            print(f"No films found for director '{director}'.")

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for film in self.films:
                file.write(f"{film.title},{film.release_date},{film.director},{film.genre},{film.duration_min}\n")
        print(f"Catalog saved to {filename}.")

    def load_from_file(self, filename):
        self.films = []
        with open(filename, 'r') as file:
            for line in file:
                title, release_date, director, genre, duration = line.strip().split(',')
                film = Film(title, release_date, director, genre, int(duration))
                self.add_film(film)
        print(f"Catalog loaded from {filename}.")
