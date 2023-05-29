import datetime
from pymongo import MongoClient
client = MongoClient()
db=client.test

while True:    
    movies = db.Filme
    user = input("What to do? Choose one:\n 1. Insert a movie\n 2. Show database\n")
    if user == "1":
        try:
            title = input("Enter movie title: \n")
            genre = input("Enter movie genre: \n")
            year = int(input("Enter movie year: \n"))
        except:
            print('Wrong insert! Try again!')
            continue
                
        movie_details = {
            'title': title,
            'genre': genre,
            'year' : year
        }

        current_year = datetime.datetime.now().year
        if year <= current_year:
            movies.insert_one(movie_details)
        else:
            print(f"The book's year can't be greater than {current_year}")

    elif user == "2":   
        result = movies.find()
    
        for r in result:
            print(f"Movie: {r['title'].capitalize()}, Genre: {r['genre']}, Year: {r['year']}")
    else:
        print('Choose 1 or 2, please!')
        continue