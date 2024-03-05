max_games = 10


class GameDetails:
    def __init__(self, details):
        self.details = details
        self.names = []
        self.desciption = []

    def fill_names_details(self):
        for i, (game_name, tags) in enumerate(self.details.items()):
            if i == max_games:
                break
            self.names.append(game_name)
            self.desciption.append(tags["Info"])

    def print_details(self):
        print("\nList of 10 first games:")
        for name, description in zip(self.names, self.desciption):
            print("Game Name:", name)
            print("Info:", description)
            print()

    def generate_tag_counts(self):
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