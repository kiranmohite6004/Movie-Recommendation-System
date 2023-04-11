import pandas as pd

movies = pd.DataFrame(columns=["title", "director", "genre", "ratings", "keywords"])
START = "\nEnter\n 'a' to add a movie, \n 'l' to see your movies, \n 'f' to find a movie by title, \n or 'q' to quit: "


def add_movie():
    global movies
    option = input("You can add multiple movies using valid csv/tsv file as well. if you have so press y.").lower()
    if option == 'y':
        print("Reading input file adding into dataset")
        df = pd.read_csv('Movies.csv')
        movies = pd.concat([df, movies]).reset_index(drop=True)
    else:
        title = input("Enter title of the film: ")
        director = input("Enter director of the film: ")
        genre = input("Enter genre of the film: ")
        ratings = input("Enter ratings of the film: ")
        keywords = input("Enter keywords of the film: ")

        new_row = pd.DataFrame({
            'title': title,
            'director': director,
            'genre': genre,
            'ratings': ratings,
            'keywords': keywords
        }, index=[0])

        movies = pd.concat([new_row, movies]).reset_index(drop=True)


def list_movies():
    quantity = len(movies.index)

    if quantity:
        titles = movies['title'].to_list()
        titles = ', '.join(titles)
        print(
            f'You have following movies in collection: {titles}. \nIn total you have {quantity} {"movie" if quantity == 1 else "movies"}.')
    else:
        print('There are no movies in you collection.')


def print_movie_info(movies_details):
    print('Here is information about requested title')
    print(f'Title: {movies_details["title"].values},')
    print(f'Director: {movies_details["director"].values},')
    print(f'Genre: {movies_details["genre"].values}.')
    print(f'Year: {movies_details["ratings"].values},')
    print(f'Genre: {movies_details["keywords"].values}.')

def find_title():
    search_title = input('Enter title you are looking for: ')
    movies_details = pd.DataFrame(movies.loc[movies['title'] == search_title])

    if len(movies_details.index) >= 1:
        print_movie_info(movies_details)
    else:
        print('Requested title was not found in the collection.')
"""
    for i in range(len(movies.title)):

        if search_title == movies.title[i]:
            index = i
            print_movie_info(index)
        else:
            print('Requested title was not found in the collection.')
"""
user_selection = {
    'a': add_movie,
    'l': list_movies,
    'f': find_title
}


def menu():
    selection = input(START).lower()
    while selection != 'q':
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: 'a', 'f', 'l' or 'q' to close the app.")
        selection = input(START)
    print('Thank you for using the app. See you next time!')


if __name__ == '__main__':
    menu()
