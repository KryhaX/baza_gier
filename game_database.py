import ast

menu = """
1. Display the names of all games in the database
2. Display all games in the database
3. Display the TOP 5 games in the database
4. Display games from a genre
5. Add a game to the database
6. Edit a game in the database
7. Remove a game from the database
8. Display information about a game
9. Rate a game
10. Save data to file
11. Read data from file
12. Exit
"""
while True:

    game_database = [
        {"title": "Cyberpunk 2077", "release_year": "2020", "genre": "RPG", "user_rating": 2},
        {"title": "The Legend of Zelda: Breath of the Wild", "release_year": "2017", "genre": "Adventure", "user_rating": 3},
        {"title": "FIFA 22", "release_year": "2021", "genre": "Sports", "user_rating": 4},
        {"title": "Among Us", "release_year": "2018", "genre": "Party", "user_rating": 5},
        {"title": "Assassin's Creed Valhalla", "release_year": "2020", "genre": "Action", "user_rating": 11},
        {"title": "Minecraft", "release_year": "2011", "genre": "Sandbox", "user_rating": 10},
        {"title": "Fall Guys: Ultimate Knockout", "release_year": "2020", "genre": "Battle Royale", "user_rating": 9},
        {"title": "The Witcher 3: Wild Hunt", "release_year": "2015", "genre": "RPG", "user_rating": 8},
        {"title": "Super Mario Odyssey", "release_year": "2017", "genre": "Platformer", "user_rating": 7},
    ]

    choice = input("Enter option:  ")
    available_choices = list(i for i in range(1, 13))

    if not choice.isnumeric() or int(choice) not in available_choices:
        continue
    else:
        choice = int(choice)
        if choice == 1:
            sorted_titles = sorted(game_database, key=lambda x: x["title"])

            for i in range(len(sorted_titles)):
                for k, v in sorted_titles[i].items():
                    if k == "title":
                        print(v)

            print(menu)
            choice = input("Enter option:  ")

        elif choice == 2:
            sorted_titles = sorted(game_database, key=lambda x: x["title"])

            for titles in sorted_titles:
                print(titles)

            print(menu)
            choice = input("Enter option:  ")

        elif choice == 3:
            sorted_ratings = sorted(game_database, key=lambda x: x['user_rating'])
            top_5 = sorted_ratings[:3:-1]
            alphabetical_top_5 = sorted(top_5, key=lambda x: x["title"])
            print(alphabetical_top_5)

            print(menu)
            choice = input("Enter option:  ")

        elif choice == 4:
            search_genre = input("Enter the genre of the game you are searching for: ")
            found_titles_by_genre = []
            for i in range(len(game_database)):
                database = game_database[i]
                for k, v in database.items():
                    if k == "genre" and v == search_genre:
                        found_titles_by_genre.append(database)

            sorted_titles_by_genre = sorted(found_titles_by_genre, key=lambda x: x["title"])
            for i in range(len(sorted_titles_by_genre)):
                for k, v in sorted_titles_by_genre[i].items():
                    if k == "title":
                        print(v)

        elif choice == 5:
            title_to_add = input("Enter the title of the game: ")
            while not title_to_add.isalpha():
                title_to_add = input("Enter the title of the game: ")

            release_year_to_add = input("Enter the release year of the game: ")
            while not release_year_to_add.isnumeric():
                release_year_to_add = input("Enter the release year of the game: ")

            genre_to_add = input("Enter the genre of the game: ")
            while not genre_to_add.isalpha():
                genre_to_add = input("Enter the genre of the game: ")

            default_user_rating = 0.0

            game_database.append({"title": {title_to_add}, "release_year": {release_year_to_add}, "genre": {genre_to_add}, "user_rating": default_user_rating})
            print(game_database)
            print(menu)
            choice = input("Enter option:  ")

        elif choice == 6:
            title_to_edit = input("Enter the title of the game to edit: ")
            edited_game = []
            for i in range(len(game_database)):
                database = game_database[i]
                for k, v in database.items():
                    if k == "title" and v == title_to_edit:
                        edited_game.append(database)
                    else:
                        print("The specified game does not exist in the database")
                        print(menu)
                        choice = input("Enter option:  ")

            title_to_add = edited_game[0]["title"]
            user_rating = edited_game[0]["user_rating"]
            while not title_to_add.isalpha():
                title_to_add = input("Enter the title of the game: ")

            release_year_to_add = input("Enter the release year of the game: ")
            while not release_year_to_add.isnumeric():
                release_year_to_add = input("Enter the release year of the game: ")

            genre_to_add = input("Enter the genre of the game: ")
            while not genre_to_add.isalpha():
                genre_to_add = input("Enter the genre of the game: ")

            new_game = {"title": {title_to_add}, "release_year": {release_year_to_add}, "genre": {genre_to_add}}
            for game in game_database:
                if game[title_to_add] == edited_game["title"]:
                    game["release_year"] = new_game["release_year"]
                    game["genre"] = new_game["genre"]

            print(game_database)
            print(menu)
            choice = input("Enter option:  ")
        elif choice == 7:
            title_to_delete = input("Enter the title of the game to delete from the database: ")
            deleted_element = None
            for i in range(len(game_database)):
                database = game_database[i]
                for k, v in database.items():
                    if k == "title" and v == title_to_delete:
                        deleted_element = database
                        game_database.remove(deleted_element)

            if deleted_element == None:
                print("There is no such element in the database ")
                continue

            print(menu)
            choice = input("Enter option:  ")

        elif choice == 8:
            title_to_edit = input("Enter the title of the game to display: ")
            exists = False
            for i in range(len(game_database)):
                for k, v in game_database[i].items():
                    if k == "title" and v == title_to_edit:
                        print(game_database[i])
                        exists = True
                        break

            if not exists:
                print("There is no such record in the database")
                continue

            print(menu)
        elif choice == 9:

            title_to_edit = input("Enter the title of the game to edit: ")
            exists = False
            for i in range(len(game_database)):
                for k, v in game_database[i].items():
                    if k == "title" and v == title_to_edit:
                        exists = True
                        break

            if not exists:
                print("There is no such record in the database")
                continue
            else:

                new_rating = input("Enter the rating: ")
                while not new_rating.isnumeric():
                    new_rating = input("Enter the rating: ")

            for game in game_database:
                if game["title"] == title_to_edit:
                    game["user_rating"] = new_rating
                    print("Successfully edited")

            print(menu)
        elif choice == 10:
            with open("games.txt",'w') as file:
                for i in range(len(game_database)):
                    file.write(str(game_database[i]))
                    file.write('\n')

            continue

        elif choice == 11:

            if game_database:
                game_database.clear()
            with open("games.txt", 'r') as file:
                for x in file:
                    game_database.append(x.strip())
            game_database = [ast.literal_eval(game_database) for game_database in game_database]

            print("Data loaded from file successfully")
            print(game_database)

            print(menu)
        elif choice == 12:
            break
