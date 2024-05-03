from Film import Film
from FilmCatalog import FilmCatalog
from film_data import add_films_to_catalog


def main():
    catalog = FilmCatalog()

    add_films_to_catalog(catalog)

    while True:
        print("\n=== Film Catalog Menu ===")
        print("1. Add a Film")
        print("2. Remove a Film")
        print("3. Display Catalog")
        print("4. Search Film by Title")
        print("5. Filter Films by Genre")
        print("6. Sort Films by Duration")
        print("7. Search Films by Director")
        print("8. Save Catalog to File")
        print("9. Load Catalog from File")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter film title: ")
            release_date = input("Enter release year: ")
            director = input("Enter director's name: ")
            genre = input("Enter genre: ")
            duration = int(input("Enter duration in minutes: "))
            film = Film(title, release_date, director, genre, duration)
            catalog.add_film(film)

        elif choice == '2':
            title = input("Enter title of film to remove: ")
            catalog.remove_film(title)

        elif choice == '3':
            catalog.display_catalog()

        elif choice == '4':
            title = input("Enter title of film to search: ")
            catalog.search_by_title(title)

        elif choice == '5':
            genre = input("Enter genre to filter films: ")
            catalog.filter_by_genre(genre)

        elif choice == '6':
            catalog.sort_by_duration()

        elif choice == '7':
            director = input("Enter director's name to search films: ")
            catalog.search_by_director(director)

        elif choice == '8':
            filename = input("Enter filename to save catalog: ")
            catalog.save_to_file(filename)

        elif choice == '9':
            filename = input("Enter filename to load catalog from: ")
            catalog.load_from_file(filename)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()