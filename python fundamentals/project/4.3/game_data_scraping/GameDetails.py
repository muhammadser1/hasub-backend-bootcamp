max_games = 10


class GameDetails:
    def __init__(self, details):
        self.details = details #dictionary contains details of several games. Each game entry consists of a game title as the key and a nested dictionary as the value(tags)
        self.names = [] #name games
        self.desciption = [] # tags

    def fill_names_details(self):# populates the names and descriptions lists with game names and their corresponding descriptions (tags) from the details dictionary.
        for i, (game_name, tags) in enumerate(self.details.items()):
            if i == max_games:
                break
            self.names.append(game_name)
            self.desciption.append(tags["Info"])

    def print_details(self): # printing the details (name and description) of the first 10 games
        print("\nList of 10 first games:")
        for name, description in zip(self.names, self.desciption):
            print("Game Name:", name)
            print("Info:", description)
            print()

    def generate_tag_counts(self):#Generate a count of tags from the game descriptions and save the result in a dictionary, where the keys represent tags and the values represent the counts.
        c=0
        tag_counts={}
        while c<2:
            for tags in self.desciption:
                words = tags.split(", ")
                for word in words:
                    if c == 0:
                        tag_counts[word] = 0
                    else:
                        tag_counts[word] += 1
            c+=1
        return tag_counts