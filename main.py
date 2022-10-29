MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []


def add_movie():
    title = input("enter movie title: ")
    director = input("enter movie director: ")
    year = input("enter the movie release year: ")

    movies.append({'title': title,
                   'director': director,
                   'year': year
                   })


def find_movie(movie_name):
    if movie_name in movies[0]['title']:
        print(f"{movie_name} exists in the list")
    else:
        print(f"{movie_name} doesnt exist in the list")


def print_movies():
    for x in movies:

        print(f"movie name : {x['title']} \t director name : {x['director']} \t release year : {x['year']}")


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            print_movies()
        elif selection == 'f':
            mov = input("Enter movie name: ")
            find_movie(mov)
        else:
            print("Unknown command. Please try again.")

        selection = input(MENU_PROMPT)


menu()
