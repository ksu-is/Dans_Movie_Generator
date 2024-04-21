import random 

# Initialize the genres to choose from
action = ["Baby Driver", "The Matrix", "Bullet Train", "Everything Everywhere All at Once", "Top Gun", "Casino Royale"]
comedy = ["Austin Powers", "The Hangover", "Monty Python's Life of Brian", "Pineapple Express", "Smokey and The Bandit"]
romance = ["The Notebook", "Casablanca", "Breakfast at Tiffany's", "Titanic", "In the Mood for Love"]
horror = ["The Exorcist", "The Shining", "A Quiet Place", "Halloween", "The Menu"]
drama = ["Poor Things", "Forrest Gump", "The Shawshank Redemption", "The Truman Show", "Little Miss Sunshine"]

# Create the movie_picker function that takes genre as an input
def movie_picker(genre):
    if genre.lower() == "action":
        return random.choice(action)
    elif genre.lower() == "comedy":
        return random.choice(comedy)
    elif genre.lower() == "horror":
        return random.choice(horror)
    elif genre.lower() == "drama":
        return random.choice(drama)
    elif genre.lower() == "romance":
        return random.choice(romance)
    else: 
        return "Invalid Input"

user_genre = input("What movie genre do you feel like watching? ")

print("I think you'd like", '"' + str(movie_picker(user_genre)) + '"')
