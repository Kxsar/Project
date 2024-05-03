Movie Catalog
The "Movie Catalog" project is a simple console application for managing a list of movies. You can add new movies, remove them, display the list, search by various criteria, filter, and sort.
Functionality
With this application, you can:
    • Add new movies to the catalog.
    • Remove movies from the catalog by title.
    • Display a list of all movies in the catalog.
    • Search for movies by title.
    • Filter movies by genre.
    • Sort movies by duration.
    • Search for movies by director name.
    • Save the current list of movies to a file.
    • Load a list of movies from a file.

How to Use
    1 Install DependenciesMake sure you have Python installed. Then install the required dependencies: pip install -r requirements.txt
    2 Run the ApplicationRun the main file main.py: python main.py
    3 
3 Select an ActionAfter launching the application, choose an action from the menu by entering the corresponding number:
    • 1: Add a new film.
    • 2: Remove a film by title.
    • 3: Display a list of all films in the catalog.
    • 4: Search for a film by title.
    • 5: Filter films by genre.
    • 6: Sort films by duration.
    • 7: Search films by director name.
    • 8: Save the current list of films to a file.
    • 9: Load a list of films from a file.
    • 0: Exit the application.


Requirements
    • Python 3.x
Project Structure
    • main.py: Main file containing the core application logic.
    • catalog.py: Module with the FilmCatalog class representing the movie catalog.
    • film.py: Module with the Film class representing an individual movie.
    • film_data.py: Module with a function to add initial movie data to the catalog.
    • 
