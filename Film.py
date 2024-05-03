class Film:
    def __init__(self, title, release_date, director, genre="Unknown", duration_min=0):
        self.title = title
        self.release_date = release_date
        self.director = director
        self.genre = genre
        self.duration_min = duration_min
        self.id = None

    def set_id(self, film_id):
        self.id = film_id

    def __str__(self):
        return f"{self.title} ({self.release_date}), directed by {self.director}"

    def get_details(self):
        return f"{self.title} ({self.release_date}) - {self.genre} - {self.duration_min} min"

    def additional_details(self):
        return f"ID: {self.id}"